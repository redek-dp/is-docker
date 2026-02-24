# Usa a imagem oficial do Nginx
FROM nginx:alpine

# Copia os arquivos HTML locais para a pasta padrão do Nginx no container
COPY . /usr/share/nginx/html

# Expõe a porta 80
EXPOSE 80