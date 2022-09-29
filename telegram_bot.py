import telegram
from dotenv import load_dotenv
from random import shuffle
from pathlib import Path
import argparse
import os
from time import sleep
from secondary_functions import walk_for_files
from secondary_functions import retry_bot_action


def post_bot(token, chat_id, delay_time_sec=14400):
    tele_bot = telegram.Bot(token=token)
    while True:
        images_collection = walk_for_files('images')
        shuffle(images_collection)
        for image in images_collection:
            with open(Path(f'images/{image}'), 'rb') as file:
                retry_bot_action(tele_bot, chat_id, file)
            sleep(delay_time_sec)

if __name__ == '__main__':
    load_dotenv()
    bot_token = os.environ['TG_BOT_TOKEN']
    parser = argparse.ArgumentParser('Input chat ID, delay time sec')
    parser.add_argument('chat_id')
    parser.add_argument('delay', nargs='?', default=14400)
    delay_time = int(parser.parse_args().delay)
    chat_id = parser.parse_args().chat_id
    post_bot(bot_token, chat_id, delay_time)
