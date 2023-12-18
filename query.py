import requests
from pprint import pprint

PORT_NUMBER = 8000

image_path = "images/observation_0.jpg"

payload = {
    "continue_chat": True,
    "image_path": image_path,
    "prompt": "How many fridge doors are there?", ## "Describe this image precisely."
}

response = requests.post(
    f"http://localhost:{PORT_NUMBER}/action",
    json=payload,
).json()

if 'status' in response and response['status'] == 'Success':
    response = response['result']['answer']
    print('Answer:', response)
else:
    pprint(response)
