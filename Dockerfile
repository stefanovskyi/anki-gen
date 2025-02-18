# Use Python 3.8 or higher base image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY src/ ./src/

# Expose port 8000 for FastAPI
EXPOSE 8000

# Command to run the application
CMD ["python", "src/run_api.py"] 