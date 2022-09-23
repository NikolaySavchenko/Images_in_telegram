from fetch_spacex_images import fetch_spacex_launch
from fetch_NASA_images import fetch_nasa_images, fetch_EPIC_images
from telegram_bot import reporter_bot
from dotenv import load_dotenv
import argparse
import os


def main():
    load_dotenv()
    # fetch_spacex_launch()
    nasa_token = os.environ['NASA_TOKEN']
    # fetch_nasa_images(nasa_token)
    # fetch_EPIC_images(nasa_token)
    parser = argparse.ArgumentParser('Input delay time sec, chat ID')
    parser.add_argument('delay', nargs='?', default='14400')
    parser.add_argument('chat_id', nargs='?', default='@space_view')
    delay_time = int(parser.parse_args().delay)
    chat_id = parser.parse_args().chat_id
    bot_token = os.environ['TG_BOT_TOKEN']
    reporter_bot(bot_token, delay_time, chat_id)


if __name__ == '__main__':
    main()
