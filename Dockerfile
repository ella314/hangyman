# Use a specific version of Python
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /main

# Copy the application files into the container
COPY . /main

# Install only the necessary dependencies for Flask
RUN pip install flask

# Command to run the application using the Flask development server
CMD ["python", "main.py"]