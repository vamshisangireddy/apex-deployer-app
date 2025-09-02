# Start with a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the dependency file and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose port 5000 to the outside world
EXPOSE 5000

# The command to run when the container starts
CMD ["python", "app.py"]
