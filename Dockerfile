# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create data directory for database
RUN mkdir -p /app/data

# Expose app port
EXPOSE 8080

# Initialize DB then start server
CMD ["sh", "-c", "python init_db.py && gunicorn --bind 0.0.0.0:8080 app:app"]