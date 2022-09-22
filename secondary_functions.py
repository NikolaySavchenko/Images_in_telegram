import requests
import os
from urllib.parse import urlsplit
from pathlib import Path


def file_extension(url):
    split_url = os.path.splitext(url)
    return urlsplit(split_url[1]).path


def getting_page(url, file_name, playload=None, folder_name='images'):
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    response = requests.get(url, params=playload)
    response.raise_for_status()
    with open(f'{folder_name}/{file_name}{file_extension(url)}', 'wb') as file:
        file.write(response.content)
