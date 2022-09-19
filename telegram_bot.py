import telegram
from dotenv import load_dotenv
from random import shuffle
from time import sleep
import os


def reporter_bot(delay_time_sec=14400):
    space_view_bot = telegram.Bot(token=os.getenv('BOT_TOKEN'))
    images = os.walk('images/')
    while True:
        for images_list in images:
            shuffle(images_list[2])
            for image in images_list[2]:
                space_view_bot.send_photo(chat_id='@space_view', photo=open(f'images/{image}', 'rb'))
                sleep(delay_time_sec)


if __name__ == '__main__':
    load_dotenv()
    reporter_bot()
