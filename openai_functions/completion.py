import json
from typing import List

import requests

import config

def create_completion(prompt: str, stop: List[str] = ['\n']) -> dict:
    '''Create completion using Openai APIs. \

    Parameters:
        - prompt (str): user query

    Returns: dictionary with information from Openai API call
    '''
    try:
        url = f"{config.BASE_URL}/completions"
        payload = {
            "model": "text-davinci-003",
            "prompt": prompt,
            "max_tokens": 7,
            "temperature": 0,
            "top_p": 1,
            "n": 1,
            "stream": False,
            "logprobs": None,
            "stop": stop
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
