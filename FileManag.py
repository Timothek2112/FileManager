from genericpath import isfile


class FileManager:
    def create(self, name:str):
        if isfile(name):
            return "File already exists"
        else:
            file = open(name, "w+")
            file.close()
            return "file" + name + "was succefully created"
    def write(self,name:str,message:str):
        if isfile(name):
            file = open(name,"a+")
            file.write("\n" + message)
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