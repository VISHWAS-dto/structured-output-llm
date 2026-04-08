"""Pydantic try to understand by itself the type of data and validate it."""


from pydantic import BaseModel, Field
from typing import Optional




class Student(BaseModel):
    name: str
    age : Optional[int] = None
    cgpa : float = Field(gt = 0 , lt = 10)


#new_student = {"name" : "Vishwas" , "age" : 22}
 # If i write number in str so pydant understand it is a number and convert it into int

another_student = {"name" : "Vishwas" , "age" : "21" , "cgpa" : 8.5}
student = Student(**another_student)

#student1 = Student(**new_student)
print(student)
#print(student1)


student_dict = dict(student)
print(student_dict['age'])


student_json = student.model_dump_json()
print(student_json)