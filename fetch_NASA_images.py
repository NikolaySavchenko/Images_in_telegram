import requests
from secondary_functions import getting_page
from dotenv import load_dotenv
import os
import argparse
from datetime import datetime


def fetch_nasa_images(nasa_token, images_count=10):
    nasa_dayfoto_url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': nasa_token, 'count': images_count}
    response = requests.get(nasa_dayfoto_url, params=payload)
    response.raise_for_status()
    links = response.json()
    for pictere_number, link in enumerate(links):
        getting_page(link['url'], f'nasa{pictere_number}')


def fetch_EPIC_images(nasa_token):
    EPIC_url = 'https://api.nasa.gov/EPIC/api/natural'
    payload = {'api_key': nasa_token}
    response = requests.get(EPIC_url, params=payload)
    response.raise_for_status()
    links = response.json()
    for picture_number, link in enumerate(links):
        date_link = datetime.strptime(link['date'],
                                      "%Y-%m-%d %H:%M:%S").strftime("%Y/%m/%d")
        earth_url = f'https://api.nasa.gov/EPIC/archive/natural/{date_link}/png/{link["image"]}.png'
        getting_page(earth_url, f'EPIC{picture_number}', playload)


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser('Input images count')
    parser.add_argument('count', nargs='?', default=10)
    images_count = parser.parse_args().count
    nasa_token = os.environ['NASA_TOKEN']
    fetch_nasa_images(nasa_token, images_count)
    fetch_EPIC_images(nasa_token)
