import telegram
from dotenv import load_dotenv
from random import shuffle
from pathlib import Path
import argparse
import os
from time import sleep
from secondary_functions import walk_for_files
from secondary_functions import posting_images


def posting_bot(folder_name, token, chat_id, delay_time_sec=14400):
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    tele_bot = telegram.Bot(token=token)
    while True:
        images_collection = walk_for_files('images')
        shuffle(images_collection)
        for image in images_collection:
            posting_images(tele_bot, chat_id, image)
            sleep(delay_time_sec)

if __name__ == '__main__':
    load_dotenv()
    bot_token = os.environ['TG_BOT_TOKEN']
    parser = argparse.ArgumentParser('Input chat ID, delay time sec, folder name')
    parser.add_argument('chat_id')
    parser.add_argument('delay', nargs='?', default=14400)
    parser.add_argument('folder', nargs='?', default='images')
    delay_time = int(parser.parse_args().delay)
    chat_id = parser.parse_args().chat_id
    folder_name = parser.parse_args().folder
    posting_bot(folder_name, bot_token, chat_id, delay_time)
