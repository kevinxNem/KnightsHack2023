#pip install this: pip install requests

import os
import requests
import json
import subprocess
import time

from googleforms import user_dict 

url = "https://exercises-by-api-ninjas.p.rapidapi.com/v1/exercises"

# Load API key from environment variable
api_key = "05fa6f04eamsh4d82ced5e1ad334p14cf70jsnb2e9c8d2af97"
headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "exercises-by-api-ninjas.p.rapidapi.com"
}

# Run googleforms.pykevin
subprocess.run(["python", "googleforms.py"])

# Optionally, wait for a moment to ensure googleforms.py has finished
# and data is stored before continuing.
time.sleep(1)

# Now load the data into workout.py (e.g., from a file or database)

print(user_dict)

#response = requests.get(url, headers=headers)
querystring = {"muscle":user_dict["muscles"], "type":user_dict["goals"]}


try:
    response = requests.get(url, headers=headers, params=querystring)
    response.raise_for_status()  # Check if the request was successful
    parsed_json = response.json()
    print(json.dumps(parsed_json, indent=4, sort_keys=True))
except requests.RequestException as e:
    print(f"HTTP Request failed: {e}")
except json.JSONDecodeError:
    print("Failed to decode JSON response")
except Exception as e:
    print(f"An error occurred: {e}")

