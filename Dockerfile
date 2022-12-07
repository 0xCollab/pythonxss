FROM python:3.9

# Install the requests and urllib3 modules
RUN pip install requests urllib3

# Copy the script and payload file to the image
COPY script.py /
COPY payload.txt /

# Set the script as the entrypoint
ENTRYPOINT ["python", "/script.py"]
