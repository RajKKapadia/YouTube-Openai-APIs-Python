import json

import requests

import config

def create_chat_completion(prompt: str) -> dict:
    '''Create chat completion using Openai APIs.

    Parameters:
        - prompt (str): user query

    Returns: dictionary with information from Openai API call
    '''
    try:
        url = f"{config.BASE_URL}/chat/completions"
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
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
    