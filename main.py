import requests
import urllib.parse

def check_xss():
  # Prompt the user for the URL, request method, and parameter
  url = input("Enter the URL to check: ")
  method = input("Enter the request method (GET or POST): ")
  param = input("Enter the parameter to check: ")

  # Parse the URL and validate it
  parsed_url = urllib.parse.urlparse(url)

  # Prompt the user for authentication credentials, if needed
  username = input("Enter username (leave blank if not needed): ")
  password = input("Enter password (leave blank if not needed): ")
  if username and password:
    auth = (username, password)
  else:
    auth = None

  # Set the timeout for the requests
  timeout = 10

  # Read the payload file
  with open("payload.txt") as f:
    payloads = f.read().splitlines()

  # Check if the URL is reachable
  try:
    requests.head(url, timeout=timeout)
  except requests.ConnectionError:
    print("Error: Could not connect to the specified URL.")
    return

  # Send a request to the URL without the payload
  if method == "GET":
    response = requests.get(url, auth=auth, timeout=timeout)
  elif method == "POST":
    response = requests.post(url, auth=auth, timeout=timeout)
  else:
    raise ValueError("Invalid request method: must be GET or POST")

  # Check if the parameter is present in the response
  if param not in response.text:
    print("The specified parameter was not found in the response.")
  else:
    # Loop through the payloads
    for payload in payloads:
      # Encode the payload for use in the request
      encoded_payload = urllib.parse.quote(payload)

      # Send the request to the URL with the payload in the specified parameter
      if method == "GET":
        response = requests.get(url, params={param: encoded_payload}, auth=auth, timeout=timeout)
      elif method == "POST":
        data = {param: encoded_payload}
        response = requests.post(url, data=data, auth=auth, timeout=timeout)

      # Check the response for the payload
      if payload in response.text:
        print("Possible XSS vulnerability found with payload: {}".format(payload))
        break

# Test the function
check_xss()
