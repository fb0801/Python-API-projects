from fastapi import FastAPI, Path
from typing import Optional


app = FastAPI()

students = {
    1:{
    "name":"john",
    "age": 17,
    "class": "yr 18"
    }
}


@app.get("/")

def index():
    return {"name": "first data"}

#path
@app.get("/get-student/{student_id}")
def get_student(student_id: int =Path(None, description="The ID of student you want to view")):
    return students[student_id]


#query
@app.get("/get-by-name")
def get_student(*, name : Optional[str]=None, test : int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]    
    return {"data: not found"}