import uuid
from datetime import date
import requests
from pydantic import BaseModel

# import pydantic

url = 'https://raw.githubusercontent.com/bugbytes-io/datasets/master/students_v1.json'
data = requests.get(url).json()

# define Pydantic model class
class Student(BaseModel):
    # def __init__(self,s):
    #     super(Student,self).__init__(s)


    id: uuid.UUID
    name: str
    date_of_birth: date
    GPA: float
    course: str
    department: str
    fees_paid: bool

    

for s in data:
    # create Pydantic model object by unpacking key/val pairs from our JSON dict as arguments 
    model = Student(**s)
    print(model)