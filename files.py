import os
import shutil
import csv
from pathlib import Path
ROOT_PATH = Path(__file__).parent #Dir of this Python file

file = open(ROOT_PATH / "file.txt", "w") #Write or create file
file.write("Using WRITE. Also, adding new lines...\nLike this new line here!\n")
file.writelines(["--------------------\n", "WRITELINES ", "writes ", "as ", "a ", "compilation ", "of ", "items ", "in ", "a ", "list"])
file.close()

file = open(ROOT_PATH / "file.txt", "r")
print(file.readline()) #Read first line
print(file.readline()) #Read second line
file.close()

file = open(ROOT_PATH / "file.txt") #Param 'r' is default
print(file.readlines()) #Read every line as a list
file.close()

file = open(ROOT_PATH / "file.txt", "a") #Append text to file
file.write("\nUsing 'a' to append.")
file.close()

with open(ROOT_PATH / "file.txt") as file: #Using with file closes automatically
    print(file.read()) #Read every line

os.remove(ROOT_PATH / "file.txt")
os.mkdir(ROOT_PATH / "NDIR")
file = open(ROOT_PATH / "file2.txt", "w")
file.write("\nThis is file2\n")
file.close()
shutil.move(ROOT_PATH / "file2.txt", ROOT_PATH / "NDIR" / "file2.txt")
os.rename(ROOT_PATH / "NDIR" / "file2.txt", ROOT_PATH / "NDIR" / "file_new.txt")
file = open(ROOT_PATH / "NDIR" / "file_new.txt")
print(file.read())
file.close()
os.remove(ROOT_PATH / "NDIR" / "file_new.txt")
os.rmdir(ROOT_PATH / "NDIR")

try:
    file = open("filethatdoesntexist.txt")
except FileNotFoundError as exc:
    print("File not found!")
    print(exc)
except Exception as exc:
    print("Error/exception!")
    print(exc)

try:
    with open(ROOT_PATH / "data.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["id", "name", "grade"])
        escritor.writerow(["1", "Marcie", "8.5"])
        escritor.writerow(["2", "Cloud", "9.0"])
        escritor.writerow(["3", "Dany", "7.0"])
except IOError as exc:
    print("Erro on creating file.")
    print(exc)

COL_ID = 0
COL_NAME = 1
COL_GRADE = 2
try:
    with open(ROOT_PATH / "data.csv", newline="", encoding="utf-8") as arquivo:
        reader = csv.reader(arquivo)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            print(f"ID: {row[COL_ID]}\t| Name: {row[COL_NAME]}\t| Grade: {row[COL_GRADE]}")
except IOError as exc:
    print("Erro on reading file.")
    print(exc)

try:
    with open(ROOT_PATH / "data.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"ID: {row['id']}\t| Name: {row['name']}\t| Grade: {row['grade']}")
except IOError as exc:
    print("Erro on reading file.")
    print(exc)

os.remove(ROOT_PATH / "data.csv")