import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

url = "https://api.heygen.com/v2/video/generate"

payload = {
    "video_inputs": [
        {
            "character": {
                "type": "avatar",
                "avatar_id": "Daisy-inskirt-20220818",
                "avatar_style": "normal"
            },
            "voice": {
                "type": "text",
                "input_text": "Hello Daniel",
                "voice_id": "2d5b0e6cf36f460aa7fc47e3eee4ba54"
            },
            "background": {
                "type": "color",
                "value": "#008000"
            }
        }
    ],
    "dimension": {
        "width": 1280,
        "height": 720
    }
}

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "x-api-key": os.getenv("HEY_GEN_API")
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)