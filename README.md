# Adobe-India-Hackathon25-Challenge_1a
# Use a lightweight Python image compatible with AMD64
FROM --platform=linux/amd64 python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the main application file into the container
COPY app.py .

# Create input and output directories
RUN mkdir -p input output

# Install required Python dependencies
RUN pip install --no-cache-dir PyPDF2

# Define the command to run when the container starts
CMD ["python", "app.py"]
