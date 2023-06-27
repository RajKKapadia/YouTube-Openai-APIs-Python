import json

import requests

import config

def create_embeddings(prompt: str) -> dict:
    '''Create embeddings of a piece of text using Openai APIs.

    Parameters:
        - prompt (str): user query

    Returns: dictionary with information from Openai API call
    '''
    try:
        url = f"{config.BASE_URL}/embeddings"
        payload = {
            "model": "text-embedding-ada-002",
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
    