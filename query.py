import requests
from pprint import pprint

payload = {
    "image_url": "https://www.reuters.com/resizer/NLk9k89J1tfmH-B7XKd598-6j_Y=/960x0/filters:quality(80)/cloudfront-us-east-2.images.arcpublishing.com/reuters/AHF2FYISNJO55J6N35YJBZ2JYY.jpg",
    "prompt": "Describe this image precisely."
}

response = requests.post(
    f"http://localhost:8000/action",
    json=payload,
).json()

pprint(response)
