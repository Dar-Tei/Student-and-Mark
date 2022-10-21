import json


class Student:

    def __init__(self, name: str = "noname", age=0, assessment=0):
        self.student_data = {}
        self.dict_student_data = {}
        self.f = None
        self.name = name
        self.age = age
        self.assessment = assessment

    def display(self):
        if not self.name:
            raise ValueError("name attribute is not set")
        return f"name: {self.name}\nage: {self.age}\nassessment: {self.assessment}"

    def write(self):
        self.student_data = {
            "s_name": self.name,
            "s_age": self.age,
            "s_assessment": self.assessment
        }
        with open("student_data.json", "w") as outfile:
            json.dump(self.student_data, outfile)

    def read(self):
        self.f = open("student_data.json", "r")
        self.dict_student_data = json.load(self.f)
        return self.dict_student_data


class Mark(Student):
    name = "student"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.assessment: dict = {}


if __name__ == '__main__':
    m = Mark(name="Mark", age=19, assessment=50)
    m.assessment.update({"OOP": 87, "KPZ": 74, "OPI": 79})
    m.write()
    print(m.display())
    print(m.read())

