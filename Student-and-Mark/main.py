from pathlib import Path
from io import PickleIOStudent
from Class2 import Ivanov

BASE_DIR = Path(__file__).resolve().parent

if __name__ == '__main__':
    i = Ivanov(
        name="Ivanov Aleksandr",
        age=19,
        group="IPZ=21/9-d",
        assessment=85,
        discipline="KPZ")
    print(i)
    io = PickleIOStudent(str(BASE_DIR.joinpath('ivanov.pickle')))
    io.save(Ivanov)
    
    print("Ivanov is saved")
    d2 = io.restore()
    print(d2)
    
