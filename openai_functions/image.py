import json
import os

import requests

import config

def create_images_generation(prompt: str, n: int = 1, size: str = '256x256') -> dict:
    '''Create images using Openai APIs.

    Parameters:
        - prompt (str): user query
        - n (int): number of generation
        - size (str): size of the generation, must be square, and the number must be divisible by 8

    Returns: dictionary with information from Openai API call
    '''
    try:
        url = f"{config.BASE_URL}/images/generations"
        payload = {
            "prompt": prompt,
            "n": n,
            "size": size
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
    

def create_images_edit(image_path: str, mask_path: str, prompt: str) -> dict:
    '''Create images edits from image and mask file, both files must be png.

    Parameters:
        - image_path (str): image file path
        - mask_path (str): mask file path
        - prompt (str): a prompt that will replace the mask in the original image

    Returns: dictionary with information from Openai API call
    '''
    try:
        image_file_name = os.path.basename(image_path)
        image_extention = image_path.split('.', 1)[-1]
        mask_file_name = os.path.basename(mask_path)
        mask_extention = mask_path.split('.', 1)[-1]
        url = f"{config.BASE_URL}/images/edits"
        files = [
            ('image', (image_file_name, open(image_path, 'rb'), f'image/{image_extention}')),
            ('mask', (mask_file_name, open(mask_path, 'rb'), f'image/{mask_extention}'))
        ]
        headers = {
            "Authorization": config.AUTHORIZATION
        }
        payload = {
            "prompt": prompt
        }
        response = requests.request(
            "POST", url, files=files, headers=headers, data=payload)
        response = json.loads(response.text)
        return response
    except:
        return {}
    

def create_images_variation(image_path: str, n: int = 1, size: str = '256x256') -> dict:
    '''Create variations of an image.

    Parameters:
        - image_path (str): image file path
        - n (int): number of generation
        - size (str): size of the generation, must be square, and the number must be divisible by 8

    Returns: dictionary with information from Openai API call
    '''
    try:
        file_name = os.path.basename(image_path)
        extention = image_path.split('.', 1)[-1]
        url = f"{config.BASE_URL}/images/variations"
        files = [
            ('image', (file_name, open(image_path, 'rb'), f'image/{extention}'))
        ]
        headers = {
            "Authorization": config.AUTHORIZATION
        }
        payload = {
            "n": n,
            "size": size
        }
        response = requests.request(
            "POST", url, files=files, headers=headers, data=payload)
        response = json.loads(response.text)
        return response
    except:
        return {}
