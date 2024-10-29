# Import the necessary libaries
import requests

# Constants Variables
STOCK_NAME = "TSLA"
# Replace TOKEN with your free token From Alpha vantage
API_KEY = "Your API KEY or TOKEN"

# API Endpoint
API_ENDPOINT = "https://www.alphavantage.co/query"

def send_request(api_url=API_ENDPOINT, api_key=API_KEY):
    
    # API required parameters
    parameters = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol":STOCK_NAME,
        "apikey": API_KEY,
        "interval": "5min"
    }
    # Handling the client side errors
    try:
        response = requests.get(url=API_ENDPOINT, params=parameters, verify=True)
        response.raise_for_status()
        data = response.json()
    # Catch client side error and Assign to a variable
    except requests.exceptions.HTTPError as error:
        # printing the error
        print(f"Error has occured 💔 \n{error}")
    
    # Return the json response
    return data

# Submit a GET request and catch it back into the received_req variable
received_req = send_request(api_url=API_ENDPOINT, api_key=API_KEY)

# Displaying the Response
print(received_req)
