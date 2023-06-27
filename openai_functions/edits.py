import json
from typing import List

import requests

import config

def create_edits(input: str, instruction: str) -> dict:
    '''Create NLP edit using Openai APIs. \
    This can be used to complete any NPL taks.

    Parameters:
        - input (str): input query of the user
        - instruction (str): instruction to apply on the input

    Returns: dictionary with information from Openai API call
    '''
    try:
        url = f"{config.BASE_URL}/edits"
        payload = {
            "model": "text-davinci-edit-001",
            "input": input,
            "instruction": instruction
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": config.AUTHORIZATION
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        response = json.loads(response.text)
        return response
    except:
        return {}
