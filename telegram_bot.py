import telegram
from dotenv import load_dotenv
from random import shuffle
from pathlib import Path
import argparse
import os
from secondary_functions import walking_for_files
from secondary_functions import retrying_bot_action


def reporter_bot(bot_token, chat_id, delay_time_sec=14400):
    space_view_bot = telegram.Bot(token=bot_token)
    while True:
        images_list = walking_for_files('images')
        shuffle(images_list)
        for image in images_list:
            with open(Path(f'images/{image}'), 'rb') as file:
                retrying_bot_action(space_view_bot, chat_id, file, delay_time_sec)


if __name__ == '__main__':
    load_dotenv()
    bot_token = os.environ['TG_BOT_TOKEN']
    parser = argparse.ArgumentParser('Input chat ID, delay time sec')
    parser.add_argument('chat_id')
    parser.add_argument('delay', nargs='?', default=14400)
    delay_time = int(parser.parse_args().delay)
    chat_id = parser.parse_args().chat_id
    reporter_bot(bot_token, chat_id, delay_time)
