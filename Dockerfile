# Use an official Python runtime as the parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Tkinter
RUN apt-get update \
    && apt-get install -y --no-install-recommends tk \
    && rm -rf /var/lib/apt/lists/*
    

# Copy the Tkinter application files to the container
COPY . .

# Specify the command to run when the container starts
CMD [ "python", "UserInterface.py" ]
