from venv import create
from FileManag import FileManager

while True:
    mode = input("Choose a mode: ")
    if mode == "c":
        name = input("Choose a file's name: ")
        fm = FileManager
        FileManager.create(fm,name)