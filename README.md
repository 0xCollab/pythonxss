This repository contains a Python script and a Dockerfile for checking URLs for cross-site scripting (XSS) vulnerabilities. The script prompts the user for a URL to check, the request method (GET or POST), and the parameter to check. It then sends requests to the URL with payloads from a payload.txt file and checks the responses for the payloads to identify potential XSS vulnerabilities.

#Usage
Running the script
To run the script, first make sure you have Python installed on your system. Then, run the following command in a terminal window:

python script.py

The script will prompt you for the URL, request method, and parameter to check. It will also prompt you for authentication credentials if needed. Once you have entered the necessary information, the script will check the URL for XSS vulnerabilities and print the results to the terminal.

#Building the Docker image
To build a Docker image from the provided Dockerfile, run the following command in a terminal window:

docker build -t xss-checker .

This will create a Docker image called xss-checker that you can use to run the script in a Docker container.

Running the Docker container

docker run -it xss-checker

This will start a Docker container based on the xss-checker image, run the script.py script, and print the results to the terminal.

#Customizing the payloads
The payload.txt file contains a list of payloads that will be used to test for XSS vulnerabilities. You can customize this list by editing the file and adding or removing payloads as needed. The script will use each payload in the list to test the specified URL.
