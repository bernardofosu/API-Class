import re
import requests 
from datetime import datetime
import json
import os

MY_LAT = 6.205040
MY_LON = -2.486490

# API From Open Weather
api_key = "Your API KEY or TOKEN"
apiURL = "https://api.openweathermap.org/data/2.5/weather"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": api_key
}

response = requests.get(url=apiURL, params=parameters)

data = json.dumps(json.loads(response.text))
# data = response.json()
# print(data)

# API From Open Weather Using Function
api_key = os.environ.get("OWM_API_KEY")
apiURL = "https://api.openweathermap.org/data/2.5/weather"

def send_request(apiURl=apiURL, api_key=api_key):
    parameters = {
        "lat": MY_LAT,
        "lon": MY_LON,
        "appid": api_key
    }

    response = requests.get(url=apiURL, params=parameters)
    response.raise_for_status()

    data = json.dumps(json.loads(response.text))
    # data = response.json()
    return data
received_req = send_request(apiURl=apiURL, api_key=api_key)
print(received_req)

# API Requests From International Space Station (ISS)
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
iss_lat = data["iss_position"]["latitude"]
iss_lon = data["iss_position"]["longitude"]

iss_position = (iss_lat, iss_lon)
print(iss_position)


# API Requests From sunrise and Sun Rise
parameters = {
    "lat": MY_LAT,
    "lng": MY_LON,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
#print(data)

# Data breakdown
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(type(sunrise))
print(sunset)

time_now = datetime.now()
print(time_now.hour)

#Trivia Questions API
response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")

response.raise_for_status()

data = response.json()["results"]
# Checking the correct answers
for each_question in data:
    types = each_question["correct_answer"]
    print(types)


parameters = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
#response.raise_for_status
#print(response.status_code)

data = response.json()
print(data)

# Regex
pattern = re.compile(r"^(\+\d{2,4})-(\d{3})-(\d{3})-(\d{3})(\d{1})?$")
# pattern = re.compile(r"^\+\d{1,3}-\d{4}-\d{3}-\d{3}$")

# pattern = re.compile(r"^.{8,15}$")
# user = input("Enter Your Password: ")
user = input("Enter Your Phone Number: ")

# print(pattern.search("H"))
# print(pattern.search("Hello"))
print(pattern.search(user))

