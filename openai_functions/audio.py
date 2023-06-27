import json
import os

import requests

import config


def create_transcript(file_path: str) -> dict:
    '''Create transcript from a audio file.

    Parameters:
        - file_path (str): file path of the audio file.

    Returns: dictionary with information from Openai API call
    '''
    try:
        file_name = os.path.basename(file_path)
        extention = file_name.split('.', 1)[-1]
        url = f"{config.BASE_URL}/audio/transcriptions"
        files = [
            ('file', (file_name, open(file_path, 'rb'), f'audio/{extention}'))
        ]
        headers = {
            "Authorization": config.AUTHORIZATION
        }
        payload = {
            "model": "whisper-1"
        }
        response = requests.request(
            "POST", url, files=files, headers=headers, data=payload)
        response = json.loads(response.text)
        return response
    except:
        return {}


def create_translation(file_path: str) -> dict:
    '''Create translation from a audio file. \
    You can provide additional instruction prompt to this request. \
    Read more here: https://platform.openai.com/docs/api-reference/audio/create

    Parameters:
        - file_path (str): file path of the audio file.

    Returns: dictionary with information from Openai API call
    '''
    try:
        file_name = os.path.basename(file_path)
        extention = file_name.split('.', 1)[-1]
        url = f"{config.BASE_URL}/audio/translations"
        files = [
            ('file', (file_name, open(file_path, 'rb'), f'audio/{extention}'))
        ]
        headers = {
            "Authorization": config.AUTHORIZATION
        }
        payload = {
            "model": "whisper-1"
        }
        response = requests.request(
            "POST", url, files=files, headers=headers, data=payload)
        response = json.loads(response.text)
        return response
    except:
        return {}


print(create_translation('samples/multilingual.mp3'))
