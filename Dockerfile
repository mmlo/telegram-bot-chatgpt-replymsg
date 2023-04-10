# Imagem base do Python 3
FROM python:3

# Copia o código para o diretório de trabalho do container
COPY src /app

# Define o diretório de trabalho
WORKDIR /app

# Instala as dependências
RUN pip install -r requirements.txt

# Executa o código
CMD ["python", "bot.py"]