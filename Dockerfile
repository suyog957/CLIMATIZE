# Use a lightweight official Python image
FROM python:3.10-slim

# Prevent Python from buffering stdout
ENV PYTHONUNBUFFERED=1

# Create working directory
WORKDIR /app

# Copy dependency list and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Default command
CMD ["python", "-m", "app.orchestrator"]
