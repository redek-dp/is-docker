## Esta é uma rota rápida para colocar uma aplicação Python Flask rodando dentro de um container Docker.

# 1. Estrutura do Projeto
Crie uma pasta para o projeto com os seguintes arquivos:

```bash
text
meu-app-flask/
├── app.py
├── requirements.txt
└── Dockerfile
```
--------

# 2. Crie o Código da Aplicação (app.py) 
Um servidor básico que responde "Hello, Docker!".

```bash
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Olá! Este Flask está rodando no Docker."

if __name__ == '__main__':
    # host='0.0.0.0' é essencial para que o container seja acessível externamente
    # app.run(host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0', port=5000, debug=True)
```
--------

# 3. Liste as Dependências (requirements.txt) 
Informe ao Docker o que instalar.

```bash
flask==3.0.1
```
--------

# 4. Escreva o Dockerfile 
Este arquivo contém as instruções de montagem da imagem.

```bash
# Usa uma imagem oficial leve do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos locais para o container
COPY . /app

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta que o Flask usará
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
```
--------

# 5. Construa e Rode o Container 
Abra o terminal na pasta do projeto e execute os comandos:
### 1. Build da Imagem: Crie a imagem chamada flask-app.

```bash
docker build -t flask-app .
```
--------

### 2. Rodar o Container: Mapeia a porta 5000 do seu PC para a 5000 do container.

```bash
docker run -p 5000:5000 flask-app
```
--------

### Para atualizar sua aplicação após editar o código, você tem duas opções principais: a manual (reconstruir a imagem) ou a automática (usar volumes para desenvolvimento).

--------

# 1. Método Manual (Reconstruir)

Sempre que alterar o app.py, você precisa criar uma nova versão da imagem para incluir o novo código. 
#### 1. Pare o container atual: CTRL+C no terminal ou docker stop <nome>.
#### 2. Reconstrua a imagem:

```bash
docker build -t flask-app .
```
--------

#### 3. Rode o container novamente:

```bash
docker run -p 5000:5000 flask-app
```
--------

# 2. Método Automático (Hot Reload)
Para não precisar reconstruir a imagem a cada ponto e vírgula, você pode montar sua pasta local dentro do container usando um volume. Isso reflete as mudanças instantaneamente.

## Passo A: Ative o modo Debug no app.py
#### O Flask só reinicia sozinho se o debug=True estiver ativo.

```bash
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```
--------

## Passo B: Rode com Volume
#### Use a flag -v para conectar sua pasta atual (pwd) ao diretório /app do container.

```bash
# No Linux/Mac:
docker run -p 5000:5000 -v $(pwd):/app flask-app

# No Windows (PowerShell):
docker run -p 5000:5000 -v ${PWD}:/app flask-app
```
--------

## Agora, ao salvar o app.py, o Flask detectará a mudança e reiniciará o servidor dentro do container automaticamente. 
# Resumo de Comandos Úteis

- Docker Docs: Bind Mounts: Guia oficial sobre como sincronizar arquivos locais com containers.

- Flask: Debug Mode: Documentação sobre o comportamento do reloader automático. 

## Você prefere continuar usando comandos individuais do Docker ou quer aprender a configurar um arquivo docker-compose.yml para facilitar esse processo?


