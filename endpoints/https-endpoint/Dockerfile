# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Install dependencies for virtual environments and system utilities
RUN apt-get update && apt-get install -y \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Create a virtual environment
RUN python3 -m venv /app/venv

# Activate the virtual environment and upgrade pip
RUN /app/venv/bin/pip install --upgrade pip

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt using the virtual environment's pip
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Set the environment variable to use the virtual environment's Python and Flask app
ENV PATH="/app/venv/bin:$PATH"
ENV FLASK_APP=app.py

# Run app.py when the container launches using the virtual environment's Python
CMD ["python", "app.py"]
