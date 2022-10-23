import pickle
from abc import ABC, abstractmethod
from Class2 import Student, Ivanov


class AbstractIOStudent(ABC):

    def __init__(self, filepath: str):
        self.filepath = filepath

    @abstractmethod
    def save(self, student: Student):
        pass

    @abstractmethod
    def restore(self) -> Student:
        pass


class PickleIOStudent(Student):

    def save(self, student: Student):
        with open(self.filepath, 'wb') as f:
            pickle.dump(student, f)

    def restore(self) -> Student:
        with open(self.filepath, 'rb') as f:
            return pickle.load(f)
