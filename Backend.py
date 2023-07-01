from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student_results.db'
db = SQLAlchemy(app)

# Student modelpip 
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.String(10), nullable=False)

# Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)

# Result model
class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    score = db.Column(db.String(1), nullable=False)

# Home page
@app.route('/')
def home():
    return 'Welcome to Student Result Management System'

# Students page
@app.route('/students', methods=['GET', 'POST'])
def students():
    if request.method == 'POST':
        data = request.json
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        date_of_birth = data.get('date_of_birth')

        # Validate data
        if not first_name or not last_name or not date_of_birth:
            return jsonify({'error': 'Please provide all student details'}), 400

        # Create new student
        student = Student(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth)

        # Add student to the database
        db.session.add(student)
        db.session.commit()

        return jsonify({'message': 'Student added successfully'}), 200

    # Retrieve all students
    students = Student.query.all()
    students_data = [{'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name,
                      'date_of_birth': student.date_of_birth} for student in students]
    return jsonify({'students': students_data}), 200

# Courses page
@app.route('/courses', methods=['GET', 'POST'])
def courses():
    if request.method == 'POST':
        data = request.json
        course_name = data.get('course_name')

        # Validate data
        if not course_name:
            return jsonify({'error': 'Please provide course name'}), 400

        # Create new course
        course = Course(course_name=course_name)

        # Add course to the database
        db.session.add(course)
        db.session.commit()

        return jsonify({'message': 'Course added successfully'}), 200

    # Retrieve all courses
    courses = Course.query.all()
    courses_data = [{'id': course.id, 'course_name': course.course_name} for course in courses]
    return jsonify({'courses': courses_data}), 200

# Results page
@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        data = request.json
        course_id = data.get('course_id')
        student_id = data.get('student_id')
        score = data.get('score')

        # Validate data
        if not course_id or not student_id or not score:
            return jsonify({'error': 'Please provide all result details'}), 400

        # Create new result
        result = Result(course_id=course_id, student_id=student_id, score=score)

        # Add result to the database
        db.session.add(result)
        db.session.commit()

        return jsonify({'message': 'Result added successfully'}), 200

    # Retrieve all results
    results = Result.query.join(Student, Result.student_id == Student.id) \
        .join(Course, Result.course_id == Course.id) \
        .add_columns(Course.course_name, Student.first_name, Result.score) \
        .all()

    results_data = [{'course_name': result.course_name, 'student_name': result.first_name, 'score': result.score}
                    for result in results]

    return jsonify({'results': results_data}), 200


if __name__ == '__main__':
    # Create the database tables (if they don't exist)
    db.create_all()
    app.run(debug=True)
