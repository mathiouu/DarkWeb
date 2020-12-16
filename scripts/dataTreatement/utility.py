from os import listdir
from os.path import isfile, join

def getFile(path) :

    dataFiles = [f for f in listdir(path) if isfile(join(path, f))]
    return dataFiles

def formatTitle(path) :
    file_name = path.split('/')
    file_name_splitted = file_name[2].split('_')
    title = file_name_splitted[0] + ' ' + file_name_splitted[1] 
    return title