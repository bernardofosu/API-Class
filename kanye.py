# Import the necessary libaries
import requests 

API_ENDPOINT = "https://api.kanye.rest/"

response = requests.get(API_ENDPOINT)

data = response.json()

print(data)