from curses.ascii import isalnum
from email.message import Message
from FileManag import FileManager, MessageHaveNumbers, PhoneHaveNonNumeric

fm = FileManager
def checkIfNumeric(message:str):
    if message.isalnum():
        pass
    else:
        raise PhoneHaveNonNumeric

def checkIfAlphabetic(message:str):
    if message.isalpha():
        pass
    else:
        raise MessageHaveNumbers

while True:    
    mode = input("Choose a mode: ")

    if mode == "w" or mode == "r":
        name = input("Choose a file: ")
        name += ".txt"
        if mode == 'r':
            print(FileManager.read(fm,name))
        elif mode == 'w':
            try:
                F = input("Insert a surname: ")
                checkIfAlphabetic(F)
                I = input("Insert a name: ")
                checkIfAlphabetic(I)
                O = input("Insert a second name: ")
                checkIfAlphabetic(O)
                FIO = F + " " + I + " " + O
                
                phone = input("Insert phone number: ")
                FIO += "..............%s" % phone
                checkIfNumeric(phone)
                print(FileManager.write(fm,name,FIO))

            except MessageHaveNumbers as e:
                print(e)
            except PhoneHaveNonNumeric as e:
                print(e)
    else:
        if mode == "c":
            name = input("Choose a file's name: ")
            fm = FileManager
            print(FileManager.create(fm,name + ".txt"))
    
    