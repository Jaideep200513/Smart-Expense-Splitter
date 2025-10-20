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