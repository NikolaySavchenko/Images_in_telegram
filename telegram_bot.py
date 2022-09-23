import telegram
from dotenv import load_dotenv
from random import shuffle
from time import sleep
from pathlib import Path
import argparse
import os


def reporter_bot(bot_token, delay_time_sec=14400, chat_id='@space_view'):
    space_view_bot = telegram.Bot(token=bot_token)
    images = os.walk('images')
    while True:
        for images_list in images:
            shuffle(images_list[2])
            for image in images_list[2]:
                space_view_bot.send_photo(chat_id=chat_id, photo=open(Path(f'images/{image}'), 'rb'))
                sleep(delay_time_sec)


if __name__ == '__main__':
    load_dotenv()
    bot_token = os.environ['BOT_TOKEN']
    parser = argparse.ArgumentParser('Input delay time sec, chat ID')
    parser.add_argument('delay', nargs='?', default=14400)
    parser.add_argument('chat_id', nargs='?', default='@space_view')
    delay_time = int(parser.parse_args().delay)
    chat_id = parser.parse_args().chat_id
    reporter_bot(bot_token, delay_time, chat_id)
