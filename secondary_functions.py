import requests
import os
from urllib.parse import urlsplit
from pathlib import Path
from time import sleep
import telegram


def file_extension(url):
    split_url = os.path.splitext(url)
    return urlsplit(split_url[1]).path


def getting_page(url, file_name, payload=None, folder_name='images'):
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    response = requests.get(url, params=payload)
    response.raise_for_status()
    with open(Path(f'{folder_name}/{file_name}{file_extension(url)}'), 'wb') as file:
        file.write(response.content)


def walking_for_files(folder_adress):
    files = os.walk(folder_adress)
    for file_list in files:
        return file_list[2]

def retrying_bot_action(bot_name, chat_id, file, delay_time_sec, Error_sleep=10):
    try:
        bot_name.send_photo(chat_id=chat_id, photo=file)
        sleep(delay_time_sec)
    except telegram.error.NetworkError:
        print(f'NetworkError, Resend after {Error_sleep} sec')
        sleep(Error_sleep)
        try:
            bot_name.send_photo(chat_id=chat_id, photo=file)
            sleep(delay_time_sec)
        except telegram.error.NetworkError:
            print(f'NetworkError, Resend after {Error_sleep*15} sec')
            sleep(Error_sleep*15)
            return
