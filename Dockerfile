# Use the official Python image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install requests

# Run main.py when the container launches
CMD ["python", "app.py"]