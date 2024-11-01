# Student REST API

This project demonstrates a simple REST API built with Python's Flask framework. The API supports CRUD (Create, Read, Update, Delete) operations on student data, which can be tested locally and deployed to Azure App Service for cloud hosting.

## Features

- Retrieve all students
- Retrieve a specific student by ID
- Create a new student
- Update an existing student
- Delete a student

## Prerequisites

Before you can run or deploy this app, ensure the following are installed:

- Python 3.x
- pip (Python package manager)
- Flask (`pip install Flask`)
- gunicorn (`pip install gunicorn`)
- Azure CLI (optional, for deployment)

## Project Structure

- `app.py`: Main Flask application containing API logic
- `requirements.txt`: List of Python dependencies
- `test-api.http`: File to test the REST API using the REST Client extension in Visual Studio Code
- `README.md`: Documentation

## Running Locally

To run the Flask API on your local machine:

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/student-rest-api.git
2. Navigate to the project directory:
   ```bash
   cd student-rest-api
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the application:
   ```bash
   python app.py
5. The API will be running at http://127.0.0.1:8000
6. Use **test.http** to test the REST API using the REST Client extension in Visual Studio Code.
