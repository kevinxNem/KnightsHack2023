#pip install this: pip install requests

import os
import requests

url = "https://exercises-by-api-ninjas.p.rapidapi.com/v1/exercises"

# Load API key from environment variable
api_key = "05fa6f04eamsh4d82ced5e1ad334p14cf70jsnb2e9c8d2af97"
headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "exercises-by-api-ninjas.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

# Handle the response
if response.status_code == 200:
    print(response.json() )
else:
    print(f"Failed to fetch data: {response.status_code}")

