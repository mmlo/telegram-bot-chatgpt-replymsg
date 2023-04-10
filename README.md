# Bot de Resposta Automática em Telegram

Este é um projeto de um bot de resposta automática em Telegram que utiliza a API da OpenAI para gerar uma resposta com base em uma mensagem citada. O bot é capaz de decodificar a mensagem citada utilizando a biblioteca `urllib` e enviar uma solicitação para a API da OpenAI para gerar uma resposta.

![Exemplo](print.png)

## Como utilizar

1. Clone o repositório
2. Crie um arquivo `.env` na raiz do projeto src/ com as seguintes informações:
```
TELEGRAM_BOT_TOKEN=<seu_token_do_telegram>
OPENAI_API_KEY=<sua_chave_da_api_da_openai>
```

3. Inicie o bot utilizando o Docker Compose:
```
docker compose up -d
```

O bot agora estará online e pronto para receber mensagens. Para citar uma mensagem e receber uma resposta, basta responder a uma mensagem enviada com uma mensagem que comece com `@nomedobot`, seguida de um texto opcional(prefixo). O bot irá gerar uma resposta com base no prefixo e na mensagem citada e enviá-la como uma resposta à mensagem original.

## Tecnologias utilizadas

- Python 3
- Biblioteca `telebot` para Python
- API da OpenAI
- Docker e Docker Compose

# ENG:

# Telegram Auto-Reply Bot 

This is a project of a Telegram auto-reply bot that uses the OpenAI API to generate a response based on a quoted message. The bot is capable of decoding the quoted message using the `urllib` library and sending a request to the OpenAI API to generate a response.

## How to use

1. Clone the repository
2. Create a `.env` file at the root of the src/ directory with the following information:
```
TELEGRAM_BOT_TOKEN=<your_telegram_token>
OPENAI_API_KEY=<your_openai_api_key>
```

3. Start the bot using Docker Compose:
```
docker compose up -d
```

The bot is now online and ready to receive messages. To quote a message and receive a response, simply reply to a message sent with a message that starts with `@botname`, followed by an optional prefix text. The bot will generate a response based on the prefix and the quoted message and send it as a reply to the original message.

## Technologies used

- Python 3
- `telebot` library for Python
- OpenAI API
- Docker and Docker Compose