# ✅ Base image compatible with amd64 architecture (no GPU)
FROM --platform=linux/amd64 python:3.9-slim

# ✅ Set working directory inside the container
WORKDIR /app

# ✅ Copy the main application script to the container
COPY app.py .

# ✅ Create required folders for input and output
RUN mkdir -p input output

# ✅ Install required Python libraries (lightweight, offline)
RUN pip install --no-cache-dir PyPDF2

# ✅ Disable internet access inside the container runtime (handled externally via --network none)
# This image is fully offline-compatible. No network calls are made in the app.

# ✅ Final command: Run the app
CMD ["python", "app.py"]
