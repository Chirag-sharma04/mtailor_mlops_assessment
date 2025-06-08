import requests
import json
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Read Bearer token from .env
bearer_token = os.getenv("BEARER_TOKEN")

url = "https://api.cortex.cerebrium.ai/v4/p-591fc243/my-project/run"

payload = json.dumps({
    "param_1": "Hello",    
    "param_2":"World"  
})

headers = {
    'Authorization': f'Bearer {bearer_token}',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)