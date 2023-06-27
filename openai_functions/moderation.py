import json

import requests

import config

def create_moderation(prompt: str) -> dict:
    '''Create moderations of a piece of text using Openai APIs. \
    This will help in checking the toxicity of the text.

    Parameters:
        - prompt (str): user query

    Returns: dictionary with information from Openai API call
    '''
    try:
        url = f"{config.BASE_URL}/moderations"
        payload = {
            "input": prompt
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
