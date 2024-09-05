# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install the dependencies for the virtual environment
RUN apt-get update && apt-get install -y python3-venv && \
    rm -rf /var/lib/apt/lists/*

# Create a virtual environment
RUN python3 -m venv venv

# Upgrade pip within the virtual environment
RUN venv/bin/pip install --upgrade pip

# Copy the current directory contents into the container at /app
COPY . .

# Install dependencies within the virtual environment using requirements.txt
RUN venv/bin/pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Set the environment variable to use the virtual environment's Python
ENV PATH="/app/venv/bin:$PATH"

# Run app.py using the virtual environment's Python
CMD ["python", "app.py"]
