from genericpath import isfile

class MessageHaveNumbers(Exception):
    def __init__(self, message="FIO can't include non-alphabetic simbols"):
        self.message = message
        super().__init__(self.message)
        
class PhoneHaveNonNumeric(Exception):
    def __init__(self, message = "Phone number cannot include non-numeric simbols"):
        self.message = message
        super().__init__(self.message)
        

class FileManager:
    def create(self, name:str):
        try:
            if isfile(name):
                return "File already exists"
            else:
                file = open(name, "w+")
                file.close()
                return "file " + name + " was succefully created"
        except FileNotFoundError as e:
            print(e)
            return "File is not exist"

    def write(self,name:str,message:str):
        if isfile(name):
            file = open(name,"a+")
            file.write("\n" + message)
            file.close()
            file = open(name,"r")
            r = file.read()
            file.close()
            return r
        else:
            return "This file dont exist"

    def read(self,name:str):
        if isfile(name):
            file = open(name,"r")
            r =  file.read()
            file.close()
            return r