# Use the Python 3.12.5 base image
FROM python:3.12.5

# Set the working directory in the container
WORKDIR /home

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any dependencies if required (uncomment the following line)
RUN pip install -r requirements.txt

# Command to run the application
CMD ["python", "app.py"]
