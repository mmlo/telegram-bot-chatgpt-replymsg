import telebot
import re
import requests
import logging
import openai
import urllib.parse
import unicodedata
from dotenv import load_dotenv
import os

load_dotenv()

# Set up telebot logger
telebot.logger.addHandler(logging.StreamHandler())
telebot.logger.setLevel(logging.INFO)

# Set up logging format
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
    ],
)

# Set up telebot
bot = telebot.TeleBot(os.getenv('TELEGRAM_BOT_TOKEN'))

# Set up OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

allowed_user_ids = [536802734]

# Define message handler for quoting messages
@bot.message_handler(
    func=lambda message: (
        not message.from_user.is_bot and
        message.reply_to_message is not None and
        message.from_user.id in allowed_user_ids and
        message.from_user.id != bot.get_me().id
    )
)
def quote_message(message):
    # Get original message and bot username
    original_message = message.reply_to_message
    bot_username = bot.get_me().username
    
    # Check if bot was mentioned at the beginning of the message
    if re.match(fr"@{bot_username}\b", message.text):
        # Get prefix and original text of message
        match = re.match(fr"@{bot_username}\b(.*)", message.text)
        prefix = match.group(1).strip()
        original_text = original_message.text.strip()
        
        # Encode prefix and original text using urllib.parse.quote_plus()
        prefix = urllib.parse.quote_plus(prefix)
        original_text = urllib.parse.quote_plus(original_text)
        
        # Decode prefix and original text using urllib.parse.unquote_plus()
        prefix = urllib.parse.unquote_plus(prefix)
        original_text = urllib.parse.unquote_plus(original_text)
        
        # Concatenate prefix, a whitespace, and original text
        quote_text = f"{prefix} {original_text}" if prefix else original_text
        
        try:
            # Send "typing" chat action to Telegram
            bot.send_chat_action(message.chat.id, 'typing')
            
            # Generate response using OpenAI API
            prompt = f"Responda a mensagem citada: {quote_text}"
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=200,
                n=1,
                stop=None,
                temperature=0.7,
            )

            # Get generated text
            generated_text = response.choices[0].text.strip()
            
            # Reply with generated text and "typing" chat action to Telegram
            bot.send_chat_action(message.chat.id, 'typing')
            bot.reply_to(original_message, generated_text)
            
        except requests.exceptions.ConnectionError:
            logging.exception("Error sending message")
            bot.send_message(message.chat.id, "There was a temporary error sending the message. Please try again later.")


try:
    # Set up bot polling
    logging.info(f"Bot {bot.get_me().username} is online and connected to Telegram.")
    bot.polling()
except Exception as e:
    # Send error message if bot polling fails
    logging.exception(e)
    bot.send_message(message.chat.id, f"An error occurred: {str(e)}")
