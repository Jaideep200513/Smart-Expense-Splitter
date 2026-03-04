<<<<<<< HEAD
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
=======
# 1. Use an official Python 3.10 image
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the requirements file first and install
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy all your project files into the container
COPY . .

# 5. Run your init_db.py script to create the database with sample members
RUN python init_db.py

# 6. Tell Docker the app will listen on port 8080
EXPOSE 8080

# 7. The command to run your app using gunicorn
# This binds to port 8080 and runs your 'app' object from your 'app.py' file
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
>>>>>>> 5a3c44767c4b2af7b056bb81d56323b88a9f23ae
