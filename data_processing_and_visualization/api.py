from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

api = Api(app)

# data for the API
STUDENTS = {
    '1': {'name': 'Ojas', 'math':98, 'physics': 97, 'chemistry': 95},
    '2': {'name': 'Nikhil', 'math':46, 'physics': 94, 'chemistry': 90},
    '3': {'name': 'Sparsh', 'math':90, 'physics': 98, 'chemistry': 90},
    '4': {'name': 'Ashish', 'math':85, 'physics': 73, 'chemistry': 87},
    '5': {'name': 'Tushar', 'math':88, 'physics': 92, 'chemistry': 67},
    '6': {'name': 'Sachin', 'math':90, 'physics': 84, 'chemistry': 95},
    '7': {'name': 'Saurabh', 'math':64, 'physics': 52, 'chemistry': 45},
    '8': {'name': 'Archit', 'math':78, 'physics': 66, 'chemistry': 53},
    '9': {'name': 'Shubh', 'math':76, 'physics': 71, 'chemistry': 82},
    '10': {'name': 'Rishi', 'math':48, 'physics': 42, 'chemistry': 47},
}

class StudentsList(Resource):
    # GET request for the API
    def get(self):
        return STUDENTS
    # POST request for the API
    def post(self):
        pass

# route for the API
api.add_resource(StudentsList, '/students/')

if __name__ == "__main__":
    app.run(debug=True)