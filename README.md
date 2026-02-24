# SERVER HTML DOCKER

## Para criar um servidor HTML usando Docker, o método mais rápido e comum é utilizar o Nginx, um servidor web leve e eficiente. Siga este tutorial passo a passo:

# 1. Prepare seus arquivos

Crie uma pasta para o projeto e, dentro dela, salve o seu arquivo HTML principal como index.html.

```bash
<!-- index.html -->
<!DOCTYPE html>
<html>
<body>
    <h1>Meu Site no Docker!</h1>
</body>
</html>
```
--------

# 2. Crie o Dockerfile 
No mesmo diretório, crie um arquivo chamado Dockerfile (sem extensão) com o seguinte conteúdo:

```bash
# Usa a imagem oficial do Nginx
FROM nginx:alpine

# Copia os arquivos HTML locais para a pasta padrão do Nginx no container
COPY . /usr/share/nginx/html

# Expõe a porta 80
EXPOSE 80
```
--------

# 3. Construa a Imagem
Abra o terminal na pasta do projeto e execute o comando abaixo para gerar a imagem:

```bash
docker build -t meu-servidor-html .
```
--------

# 4. Execute o Container
Agora, inicie o servidor mapeando uma porta do seu computador (ex: 8080) para a porta 80 do container:

```bash
docker run -d -p 8080:80 --name meu-site meu-servidor-html
```
--------

- -d: Roda em segundo plano (detached mode).
- -p 8080:80: Mapeia a porta 8080 do seu host para a 80 do container.

# 5. Acesse seu site 

```bash
Abra o navegador e acesse http://localhost:8080
```
--------

## Dica Pro (Sem Dockerfile): Se você quiser apenas testar o HTML rapidamente sem criar uma imagem customizada, pode usar um bind mount diretamente no terminal:

```bash
docker run -d -p 8080:80 -v $(pwd):/usr/share/nginx/html nginx:alpine
```
--------

# 6. Para atualizar o seu site após editar o arquivo index.html, o método depende de como você iniciou o container:

- Opção 1: Se você usou um Dockerfile (Rebuild)
Se você seguiu o passo a passo de criar uma imagem customizada, precisará reconstruir a imagem para incluir a nova versão do arquivo:

- Pare e remova o container antigo:

```bash
docker stop meu-site
docker rm meu-site
```
--------


# 7. Gere a imagem novamente:

```bash
docker build -t meu-servidor-html .
```
--------

# 8. Inicie o novo container:

```bash
docker run -d -p 8080:80 --name meu-site meu-servidor-html
```
--------

- Opção 2: Se você usou o comando rápido (Bind Mount)
Se você utilizou o comando com -v $(pwd):/usr/share/nginx/html, a atualização é automática. 

- Basta salvar o arquivo index.html no seu computador e atualizar a página (F5) no navegador.

- O Nginx lerá o arquivo alterado instantaneamente no container. 
- Stack Overflow Stack Overflow +2
- Opção 3: Atualizar sem reiniciar (Docker CP)
Se o container já está rodando e você não quer reiniciá-lo, pode "copiar" o arquivo editado diretamente para dentro dele:

```bash
docker cp index.html meu-site:/usr/share/nginx/html/index.html
```
--------



## Recomendação para Desenvolvimento:
Para evitar ter que reconstruir a imagem a cada pequena alteração de texto ou cor, utilize sempre o Bind Mount (Opção 2) enquanto estiver criando o site. Deixe o Dockerfile apenas para quando o site estiver pronto para ser publicado ou enviado para outra pessoa.


