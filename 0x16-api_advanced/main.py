#!/usr/bin/python3
import requests

# Make a GET request to a web page
response = requests.get("https://www.w3schools.com/python/python_user_input.asp")

# Print the status code of the response
print(response.status_code)

# Print the headers of the response
print(response.headers)
