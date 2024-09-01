from .extensions import db


class Course(db.Model):
    """
    Define the Course model with the following columns:
    - id: primary key of the Course model.
    - name: name of the course.
    - students: relationship with the Student model.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    students = db.relationship("Student", back_populates="course")


class Student(db.Model):
    """
    Define the Student model with the following columns:
    - id: primary key of the Student model.
    - name: name of the student.
    - course_id: foreign key to the Course model.
    - course: relationship with the Course model.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    course_id = db.Column(db.ForeignKey("course.id"))

    course = db.relationship("Course", back_populates="students")
