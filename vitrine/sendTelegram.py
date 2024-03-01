from telegram import Bot
import dotenv
import os

dotenv.load_dotenv(".env")

api_key = os.getenv('TELEGRAM_API_KEY')
user_id = os.getenv('TELEGRAM_USER_ID')

# myBot = Bot(token=api_key)

def send(message="Ton gp le tracteur"):
    pass
    #myBot.send_message(chat_id=user_id, text=message)

if __name__ == "__main__":
    send()  