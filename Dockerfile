# Use a imagem oficial do Python 3.8 como base
FROM python:3.8

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie todos os arquivos do diretório atual para o diretório de trabalho no contêiner
COPY . /app

# Instale as dependências necessárias para o seu chatbot
RUN pip install --no-cache-dir tensorflow torch transformers flask

# Exponha a porta 5000 para a aplicação Flask
EXPOSE 5000

# Defina o comando padrão para executar o aplicativo
CMD ["python", "app.py"]
