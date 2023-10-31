# GPT4 Image Recognition API

Small tool using selenium to get a temporary API endpoint for the ChatGPT Image Input / image recognition feature.  
Very quickly made, you should not rely on this on prod.  
Should be deprecated as soon as we have access to official OpenAI endpoints.  
Works with google authentification. If you use a different login method, please modify the code for your usecase.  

# Requirements

- Chrome version is 118.xx.xx 
- A paid OpenAI API associated with a Google account

# Installation

- Create venv, then clone the repo  
- Install requirements:  
`pip install -r requirements.txt`
- Define a `.env` file with your OpenAI Google credentials (or whatever but make sure to modiy the code appropriately), for example,
```
GOOGLE_EMAIL={GOODLE.ACCOUNT}@gmail.com
GOOGLE_PASSWORD={PASSWORD}
```

# Usage

- Run FastAPI server in one terminal window. You'll see a Chrome window pop up
`python main.py`
- Open another Chrome window and go to https://0.0.0.0:8000/start
- In the first Chrome window, you'll see ChatGPT being automaticly logged in. Manually click "Ok, let's go"
- In the first terminal window, press ENTER
- Ran example queries in another terminal window
`python query.py`


# Endpoints

## GET
`https://0.0.0.0:8000/start`  
Start a new session. Complete manually the login steps and press enter when asked.  
Wait for the OpenAI popup to display before pressing enter.  

`https://0.0.0.0:8000/stop`  
Stop the current session.  

## POST
`https://0.0.0.0:8000/action/`  
Post an image URL with a prompt. Example:  
```
Request:
{
    "image_url": "https://www.reuters.com/resizer/NLk9k89J1tfmH-B7XKd598-6j_Y=/960x0/filters:quality(80)/cloudfront-us-east-2.images.arcpublishing.com/reuters/AHF2FYISNJO55J6N35YJBZ2JYY.jpg",
    "prompt": "Describe this image precisely."
}

Response:
{
    "status": "Success",
    "result": {
        "answer": "A night view of the Eiffel Tower illuminated, with its reflection visible in calm water in the foreground. The sky is dark blue, and there are two streetlights on either side of the scene."
    }
}
```
