import requests
from secondary_functions import getting_page
from dotenv import load_dotenv
import os
from datetime import datetime


def fetch_nasa_images(count_img=10):
    nasa_dayfoto_url = 'https://api.nasa.gov/planetary/apod'
    playload = {'api_key': os.getenv('NASA_TOKEN'), 'count': count_img}
    response = requests.get(nasa_dayfoto_url, params=playload)
    response.raise_for_status()
    links = response.json()
    for pictere_number, link in enumerate(links):
        getting_page(link['url'], f'nasa{pictere_number}')


def fetch_EPIC_images():
    EPIC_url = 'https://api.nasa.gov/EPIC/api/natural'
    playload = {'api_key': os.getenv('NASA_TOKEN')}
    response = requests.get(EPIC_url, params=playload)
    response.raise_for_status()
    links = response.json()
    for pictere_number, link in enumerate(links):
        date_link = datetime.strptime(link['date'],
                                      "%Y-%m-%d %H:%M:%S").strftime("%Y/%m/%d")
        earth_url = f'https://api.nasa.gov/EPIC/archive/natural/{date_link}/png/{link["image"]}.png'
        getting_page(earth_url, f'EPIC{pictere_number}', playload)


if __name__ == '__main__':
    load_dotenv()
    fetch_nasa_images(10)
    fetch_EPIC_images()
