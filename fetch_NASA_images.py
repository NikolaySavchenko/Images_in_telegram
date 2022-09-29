import requests
from secondary_functions import get_image
from dotenv import load_dotenv
import os
import argparse
from datetime import datetime


def fetch_nasa_images(nasa_token, images_count=10):
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': nasa_token, 'count': images_count}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    links = response.json()
    for number, link in enumerate(links):
        get_image(link['url'], f'nasa{number}')


def fetch_EPIC_images(nasa_token):
    url = 'https://api.nasa.gov/EPIC/api/natural'
    payload = {'api_key': nasa_token}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    links = response.json()
    for number, link in enumerate(links):
        date_link = datetime.strptime(link['date'],
                                      "%Y-%m-%d %H:%M:%S").strftime("%Y/%m/%d")
        earth_url = f'https://api.nasa.gov/EPIC/archive/natural/{date_link}/png/{link["image"]}.png'
        get_image(earth_url, f'EPIC{number}', payload)


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser('Input images count')
    parser.add_argument('count', nargs='?', default=10)
    images_count = parser.parse_args().count
    nasa_token = os.environ['NASA_TOKEN']
    fetch_nasa_images(nasa_token, images_count)
    fetch_EPIC_images(nasa_token)
