import dataclasses


@dataclasses.dataclass
class Student:
    name: str
    age: int
    group: str

    @classmethod
    def from_pickle(cls):
        pass


@dataclasses.dataclass
class Mark(Student):
    assessment: int
    discipline: str

    def __str__(self):
        return f"{self.name}, {self.age}, {self.group}, {self.assessment}, {self.discipline}"


class Ivanov(Mark):
    Name = "Aleksandr"


