import streamlit as st

import requests
API="http://127.0.0.1:5000/students"

st.title("Student Management System")

option=st.selectbox("Select Operation",["GET","POST","PUT","DELETE"])

if option=="GET":
    response=requests.get(API)
    if response.status_code==200:
      st.json(response.json())

elif option=="POST":
    student_id=st.number_input("Enter Student ID",
                               min_value=1,
                               step=1)
    name=st.text_input("Enter Student Name")
    course=st.text_input("Enter Course Name")
    if st.button("Add Student"):
        student={
            "Id": student_id,
            "Name": name,
            "Course": course
        }
        response=requests.post(API,json=student)
        if response.status_code==200:
           st.success("Student Added")
#Put
elif option=="PUT":
    student_id=st.number_input(
        "Enter Student ID",
        min_value=1,
        step=1)

    name=st.text_input("Enter Student Name")

    course=st.text_input("Enter Course Name :")

    if st.button("Update Student"):
        response=requests.put(
            f"{API}/{student_id}",
             json={
                    "Name": name,
                     "Course": course
                 })
        if response.status_code==200:
             st.success("Student Updated")
        else:
             st.error("Student Not Updated")
elif option=="DELETE":
    student_id=st.number_input(
        "Enter Student ID",
        min_value=1,
        step=1)
    if st.button("Delete Student"):
        response=requests.delete(
            f"{API}/{student_id}",
        )
        if response.status_code==200:
           st.success("Student Deleted Successfully")
        else:
            st.error("Student Not Found")
