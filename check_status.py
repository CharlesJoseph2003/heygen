import requests
import time

# Your API key
api_key = "OWEyYmMyYTc5Yzk1NGViNTkwZWJjMzA1MzBlMjhlMGEtMTc1MTIyNjUzMw=="

# The video ID you received from the generation request
video_id = "a0a90fc7f587465d84ce0ab6a4406242"

# Endpoint URL for checking video status
url = f"https://api.heygen.com/v1/video_status.get?video_id={video_id}"

headers = {
    "accept": "application/json",
    "x-api-key": api_key
}

def check_video_status():
    response = requests.get(url, headers=headers)
    return response.json()

# Check status repeatedly until the video is ready
def wait_for_video_completion(max_attempts=30, delay_seconds=5):
    print("Checking video status...")
    
    for attempt in range(max_attempts):
        status_data = check_video_status()
        print(f"Attempt {attempt + 1}/{max_attempts} - Status: {status_data}")
        
        # Check if video is ready - you'll need to interpret the status response
        if "data" in status_data and status_data["data"].get("status") == "completed":
            print("\nVideo is ready!")
            return status_data
            
        print(f"Video still processing. Checking again in {delay_seconds} seconds...")
        time.sleep(delay_seconds)
    
    print("Maximum attempts reached. Video may still be processing.")
    return check_video_status()

if __name__ == "__main__":
    result = wait_for_video_completion()
    print("\nFinal status:")
    print(result)
    
    # If completed, the response should include download URL
    if "data" in result and "url" in result["data"]:
        print(f"\nVideo URL: {result['data']['url']}")
    elif "data" in result and "video_url" in result["data"]:
        print(f"\nVideo URL: {result['data']['video_url']}")
