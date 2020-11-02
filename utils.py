import os
def crear_screen():
     os.system('cls')
def get_data_file_name(name):
   
    n=name.split('\\')[len(__file__.split('\\'))-1].split(".")[0]+".txt"
    return n