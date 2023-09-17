import json
import logging
import telebot
from decouple import Config, RepositoryEnv
import requests


config = Config(RepositoryEnv(".env"))
BOT_TOKEN = config('BOT_TOKEN')
MODEL_IP = config('MODEL_IP')
MODEL_PORT = config('MODEL_PORT')
MODEL_ENDPOINT = f"http://{MODEL_IP}:{MODEL_PORT}/invocations"


def main():
    logging.basicConfig(level=logging.INFO)
    bot = telebot.TeleBot(BOT_TOKEN)

    @bot.message_handler(func=lambda message: True)
    def handle_reply(message):
        to_json = {
            "inputs": [f"{message.text}"]
        }
        response = requests.post(url=MODEL_ENDPOINT, json=json.dumps(to_json))
        if response.status_code == 200:
            logging.info(f"Success generation for {message.chat.id}")
            json_response = response.json()
            answer = json_response['predictions']
            bot.send_message(message.chat.id, str(answer))
        else:
            logging.warning(f"Failed answer from model: {response.status_code}")

    bot.infinity_polling()


if __name__ == "__main__":
    main()
