import base64
import requests
from django.conf import settings
from datetime import datetime, timedelta

def get_zoom_access_token():
    """
    Returns a Zoom OAuth access token using account_credentials grant
    """
    url = "https://zoom.us/oauth/token"

    credentials = f"{settings.ZOOM_CLIENT_ID}:{settings.ZOOM_CLIENT_SECRET}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "account_credentials",
        "account_id": settings.ZOOM_ACCOUNT_ID
    }

    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()

    token = response.json().get("access_token")
    if not token:
        raise Exception("Failed to get Zoom access token.")
    print("Zoom access token acquired:", token[:10], "...")  # debug
    return token


def create_zoom_meeting(topic):
    """
    Creates a Zoom meeting and returns the response JSON.
    Prints payload and Zoom response for debugging.
    """
    token = get_zoom_access_token()
    user_id = settings.ZOOM_HOST_USER_ID  # must be valid Zoom email or userId
    url = f"https://api.zoom.us/v2/users/{user_id}/meetings"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Start time 5 minutes from now, UTC ISO format
    start_time = (datetime.utcnow() + timedelta(minutes=5)).strftime("%Y-%m-%dT%H:%M:%SZ")

    payload = {
        "topic": topic,
        "type": 2,  # scheduled meeting
        "start_time": start_time,
        "duration": 30,
        "settings": {
            "host_video": True,
            "participant_video": True,
            "join_before_host": True
        }
    }

    print("Zoom API payload:", payload)  # debug
    response = requests.post(url, headers=headers, json=payload)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("Zoom API error response:", response.text)  # debug
        raise e

    return response.json()
