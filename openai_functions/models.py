import json

import requests

import config

def get_all_models() -> dict:
    '''Get all models from OpenAI.

    Returns: dictionary with information from Openai API call
    '''
    try:
        url = f"{config.BASE_URL}/models"
        payload = ""
        headers = {"Authorization": config.AUTHORIZATION}
        response = requests.request("GET", url, data=payload, headers=headers)
        response = json.loads(response.text)
        return response
    except:
        return {}
    
def retrive_a_models(model_name: str) -> dict:
    '''Get a model from OpenAI.

    Parameters:
        - model_name (str): a valid name of the model

    Returns: dictionary with information from Openai API call
    '''
    try:
        url = f"{config.BASE_URL}/models/{model_name}"
        payload = ""
        headers = {"Authorization": config.AUTHORIZATION}
        response = requests.request("GET", url, data=payload, headers=headers)
        response = json.loads(response.text)
        return response
    except:
        return {}
    