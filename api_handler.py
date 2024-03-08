import requests


def get_photos(api_key, sol):
    api_url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    parameters = {
        "api_key": api_key,
        "sol": sol
    }
    response = requests.get(api_url, params=parameters)
    response.raise_for_status()
    return response.json()["photos"]
