import requests
from pprint import pprint

# generate public links using https://www.labnol.org/embed/google/drive/

image_url = "https://www.reuters.com/resizer/NLk9k89J1tfmH-B7XKd598-6j_Y=/960x0/filters:quality(80)/cloudfront-us-east-2.images.arcpublishing.com/reuters/AHF2FYISNJO55J6N35YJBZ2JYY.jpg"
# image_url = "https://drive.google.com/file/d/1OcxQUuEsVbHbW7teJvRFXhbnCP2tSyCR/view"
# image_url = "https://lh3.googleusercontent.com/drive-viewer/AK7aPaD0sAw4XvuEn2l3vZUuty9g6sB5PgVdHhD6b6B0Q75Zlv6PwKJHrBgTiicxQjcH9IGG08RLGjX0jWR5ZUPpEub67WPrVQ=s2560"
# image_url = "https://uc1cd8b137a0f7f2093218299c39.previews.dropboxusercontent.com/p/thumb/ACFubi_HB2ie0-oKLsW7VqnHgWEqEA[…]Nm3ADiEO56EKjDWmQbIcPU8ikIg0IbQ/p.jpeg"

payload = {
    "image_url": image_url,
    "prompt": "Describe this image precisely."
}

response = requests.post(
    f"http://localhost:8000/action",
    json=payload,
).json()

if 'status' in response and response['status'] == 'Success':
    response = response['result']['answer']
    print('Answer:', response)
else:
    pprint(response)
