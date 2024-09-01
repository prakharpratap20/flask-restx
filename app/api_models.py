from flask_restx import fields

from .extensions import api

# Define the models for the API using the fields module from Flask-RESTx library
# (which is a fork of Flask-RESTPlus) and the api object from the extensions module.
student_model = api.model("Student", {
    "id": fields.Integer,
    "name": fields.String,
    # "course": fields.Nested(course_model)
})


# Define the course model using the fields module from Flask-RESTx library.
course_model = api.model("Course", {
    "id": fields.Integer,
    "name": fields.String,
    "students": fields.List(fields.Nested(student_model))
})

# Define the input models for the API using the fields module from Flask-RESTx library.
course_input_model = api.model("CourseInput", {
    "name": fields.String,
})

# Define the input models for the API using the fields module from Flask-RESTx library.
student_input_model = api.model("StudentInput", {
    "name": fields.String,
    "course_id": fields.Integer
})
