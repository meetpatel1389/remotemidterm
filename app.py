# Import necessary modules from Flask
from flask import Flask, jsonify, request, abort

# Initialize the Flask app
app = Flask(__name__)

# In-memory "database" of students
# This list holds a set of student dictionaries. In a real-world application, this would be replaced by a database.
students = [
    {"id": 1, "name": "Alice", "grade": "A", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "grade": "B", "email": "bob@example.com"},
]

# Define route to handle requests to the root URL ('/')
@app.route('/')
def index():
    return "Welcome to the Student REST API! Try accessing /students to see all students."

# Health check route (GET)
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

# Route to retrieve all students (GET request)
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students), 200

# Route to retrieve a single student by their ID (GET request)
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((student for student in students if student['id'] == student_id), None)
    if student is None:
        abort(404)
    return jsonify(student), 200

# Route to create a new student (POST request)
@app.route('/students', methods=['POST'])
def create_student():
    if not request.json or not 'name' in request.json or not 'grade' in request.json or not 'email' in request.json:
        abort(400)
    
    new_student = {
        'id': students[-1]['id'] + 1 if students else 1,
        'name': request.json['name'],
        'grade': request.json['grade'],
        'email': request.json['email']
    }
    students.append(new_student)
    return jsonify(new_student), 201

# Route to update an existing student (PUT request)
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = next((student for student in students if student['id'] == student_id), None)
    if student is None:
        abort(404)
    
    if not request.json:
        abort(400)
    
    student['name'] = request.json.get('name', student['name'])
    student['grade'] = request.json.get('grade', student['grade'])
    student['email'] = request.json.get('email', student['email'])
    return jsonify(student), 200

# Route to delete a student (DELETE request)
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    students = [student for student in students if student['id'] != student_id]
    return '', 204

# Entry point for running the Flask app
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
