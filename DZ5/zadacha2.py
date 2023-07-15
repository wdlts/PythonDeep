# 2. Напишите функцию, которая принимает на вход строку - абсолютный
# путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

inputstr = "G:\JOB\TINKOFFQA\PYTHONTASKS\\venv\DZ\DZ5\zadacha2.py"

def returntuple(inputstr):
    splitstr = inputstr.split("\\")
    return(("\\".join(splitstr[:-1]), "".join(splitstr[-1].split(".")[:-1]), splitstr[-1].split(".")[-1]))
print(returntuple(inputstr))