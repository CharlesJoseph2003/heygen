from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Get API key from environment variable
API_KEY = os.getenv("HEY_GEN_API")

@app.route('/')
def index():
    return jsonify({"message": "HeyGen API server is running"})

@app.route('/check-status')
def check_status():
    video_id = request.args.get('videoId')
    if not video_id:
        return jsonify({"error": {"message": "No video ID provided"}})
    
    # Endpoint URL for checking video status
    url = f"https://api.heygen.com/v1/video_status.get?video_id={video_id}"
    
    headers = {
        "accept": "application/json",
        "x-api-key": API_KEY
    }
    
    try:
        response = requests.get(url, headers=headers)
        return response.json()
    except Exception as e:
        return jsonify({"error": {"message": str(e)}})

@app.route('/generate-video', methods=['POST'])
def generate_video():
    try:
        # Get payload from request
        payload = request.json
        
        # API endpoint
        url = "https://api.heygen.com/v2/video/generate"
        
        # Headers
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "x-api-key": API_KEY
        }
        
        # Make the API request
        response = requests.post(url, json=payload, headers=headers)
        return response.json()
    except Exception as e:
        return jsonify({"error": {"message": str(e)}})

if __name__ == '__main__':
    print("Starting HeyGen API server on http://localhost:5000")
    app.run(debug=True)
