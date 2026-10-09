<img src="https://www.svgrepo.com/show/354926/docker.svg" min-width="150px" max-width="150px" width="150px" align="right" alt="">

# PYTHON FLASK DOCKER | RODANDO DENTRO DE UM CONTAINER.

ESTA É UMA ROTA RÁPIDA PARA COLOCAR UMA APLICAÇÃO PYTHON FLASK RODANDO DENTRO DE UM CONTAINER DOCKER. BY DEVELOPER DAVIDSONBPE...

----------

## 1. Estrutura do Projeto
Crie uma pasta para o projeto com os seguintes arquivos:

```bash
text
meu-app-flask/
├── app.py
├── requirements.txt
└── Dockerfile
```
--------

## 2. Crie o Código da Aplicação (app.py) 
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

## 3. Liste as Dependências (requirements.txt) 
Informe ao Docker o que instalar.

```bash
flask==3.0.1
```
--------

## 4. Escreva o Dockerfile 
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

## 5. Construa e Rode o Container 
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

## 1. Método Manual (Reconstruir)

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

## 2. Método Automático (Hot Reload)
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
## Resumo de Comandos Úteis

- Docker Docs: Bind Mounts: Guia oficial sobre como sincronizar arquivos locais com containers.

- Flask: Debug Mode: Documentação sobre o comportamento do reloader automático. 

## Você prefere continuar usando comandos individuais do Docker ou quer aprender a configurar um arquivo docker-compose.yml para facilitar esse processo?


--------

### DOAR COM

[![DOAR COM](https://img.shields.io/badge/DOAR%20COM-PagBank-295.svg?logo=pagseguro&style=for-the-badge&logoColor=f5f5f5)](https://pag.ae/7Y3uUnhg8)

--------

### CONECTE-SE COM NÓS:

[<img height="30" src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="davidsonbpe | YouTube" />][youtube]
[<img height="30" src="https://img.shields.io/badge/DAV7.STORE-555?style=for-the-badge&logo=cloudways&logoColor=white" alt="DAV7.STORE" />][dav7]
[<img height="30" src="https://img.shields.io/badge/davidsonbpe-666?style=for-the-badge&logo=dash&logoColor=fff" alt="davidsonbpe" />][davidsonbpe]
[<img height="30" src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="davidsonbpe | Instagram" />][instagram]
[<img height="30" src="https://img.shields.io/badge/CodePen-003333?style=for-the-badge&logo=c&logoColor=white" alt="davidsonbpe | CodePen" />][CodePen]
[<img height="30" src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white" alt="davidsonbpe | Facebook" />][facebook]
[<img height="30" src="https://img.shields.io/badge/GitHub-003333?style=for-the-badge&logo=github&logoColor=white" alt="davidsonbpe | GitHub" />][github]
[<img height="30" src="https://img.shields.io/badge/huggingface-6C55C1?style=for-the-badge&logo=huggingface&logoColor=75CB22" alt="Kexel | HuggingFace" />][huggingface]
[<img height="30" src="https://img.shields.io/badge/stackblitz-A89BDA?style=for-the-badge&logo=stackblitz&logoColor=fff" alt="StackBlitz" />][stackblitz]
[<img height="30" src="https://img.shields.io/badge/Pinterest-C2464B?style=for-the-badge&logo=Pinterest&logoColor=white" alt="Pinterest" />][pinterest]
[<img height="30" src="https://img.shields.io/badge/Twitter-222?style=for-the-badge&logo=x&logoColor=white" alt="davidsonbpe | Twitter" />][twitter]
<a href="mailto:dev7.capital366@passinbox.com" alt="Email">
<img height="30" src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=Minutemailer&logoColor=white" /></a>

<br />

<a href="https://dav7.pages.dev/" align="right" alt="Visitor count">
<img height="30" src="https://raw.githubusercontent.com/davserv/d-framework/refs/heads/img-iso/count.svg" /></a>

<br />

[dav7]: https://dav7.pages.dev/
[davidsonbpe]: https://davidsonbpe.blogspot.com/
[youtube]: https://www.youtube.com/channel/UCHqvw9v2Fp6o006lUskoigg/
[instagram]: https://www.instagram.com/davidsonbpe/
[facebook]: https://www.facebook.com/decomrradio/
[CodePen]: https://codepen.io/davidsonbpe/
[github]: https://github.com/davidsonbpe/
[huggingface]: https://huggingface.co/kexel
[stackblitz]: https://stackblitz.com/@redek-dp
[pinterest]: https://br.pinterest.com/davidsonbpe/
[twitter]: https://twitter.com/davidsonbpe
