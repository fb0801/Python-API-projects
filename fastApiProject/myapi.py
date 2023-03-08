from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

students = {
    1:{
    "name":"john",
    "age": 17,
    "class": "yr 18"
    }
}

class Student(BaseModel):
    "name" : str
    "age" : int
    "year" : str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[str] = None
    year: Optional[str] = None

@app.get("/")

def index():
    return {"name": "first data"}

#path
@app.get("/get-student/{student_id}")
def get_student(student_id: int =Path(None, description="The ID of student you want to view")):
    return students[student_id]


#query
@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int , name : Optional[str]=None, test : int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]    
    return {"data: not found"}



@app.post("/create-student/{student_id}")
def create_student(student_id : int, student : Student):
    if student_id in students:
        return {"Error": "studnt exists"}
    
    students[student_id] = student
    return students[student_id]



#put method
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in student:
        return {"Error": "Student does not exist"}

    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year


    return students[student_id]
    

    #delete method 
    