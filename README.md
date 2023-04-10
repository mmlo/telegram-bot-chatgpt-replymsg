# Bot de Resposta Automática em Telegram

Este é um projeto de um bot de resposta automática em Telegram que utiliza a API da OpenAI para gerar uma resposta com base em uma mensagem citada. O bot é capaz de decodificar a mensagem citada utilizando a biblioteca `urllib` e enviar uma solicitação para a API da OpenAI para gerar uma resposta.

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

![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](print.png)

## Tecnologias utilizadas

- Python 3
- Biblioteca `telebot` para Python
- API da OpenAI
- Docker e Docker Compose
