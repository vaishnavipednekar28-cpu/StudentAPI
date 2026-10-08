from flask import Flask,request,jsonify
app = Flask(__name__)
students=[]

#GET API
@app.route("/students",methods=['GET'])
def get_students():
    return jsonify(students)


#POST API
@app.route("/students",methods=['POST'])
def add_student():
    student=request.json
    students.append(student)

    return jsonify({
        "message": "Student added successfully",
    "student": student})

#PUT API
@app.route("/students/<int:Id>",methods=['PUT'])
def update_student(Id):
    for student in students:
        if student['Id']==Id:
          student['Name']=request.json['Name']
          student['Course']=request.json['Course']

          return jsonify({"message":'Updated successfully',
                          "student": student})
    return jsonify({
        "message": "Student not fount",
    }),404

#DELETE API
@app.route("/students/<int:Id>",methods=['DELETE'])
def delete_student(Id):
    for student in students:
        if student['Id']==Id:
            students.remove(student)

            return jsonify({"message":'Student deleted successfully'})
    return jsonify({"message":'Student with Id does not exist'}),404


if __name__ == "__main__":
   app.run(debug=True)

#Note : Inside url write : http://127.0.0.1:5000/students
