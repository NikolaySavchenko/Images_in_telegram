from fetch_spacex_images import fetch_spacex_launch
from fetch_NASA_images import fetch_nasa_images, fetch_EPIC_images
from telegram_bot import reporter_bot
from dotenv import load_dotenv
import argparse


def main():
    load_dotenv()
    fetch_spacex_launch()
    fetch_nasa_images()
    fetch_EPIC_images()
    parser = argparse.ArgumentParser('Input delay time sec')
    parser.add_argument('delay', nargs='?', default='14400')
    delay_time = parser.parse_args().delay
    reporter_bot(int(delay_time))


if __name__ == '__main__':
    main()
