import os
from datetime import datetime

# Elementarus budas

#os.mkdir("./projects")
#os.mkdir("./projects/data")
#os.mkdir("./projects/scripts")
#os.mkdir("./projects/logs")

#with open("./projects/README.md", "w") as file:
    #file.write("Duomenu irasymui : ")




folders_to_create = ["./automatizavimas/projects", "./automatizavimas/projects/data", "./automatizavimas/projects/scripts", "./automatizavimas/projects/logs"]
files_to_create = ["./automatizavimas/projects/README.md"]
log_file = "./automatizavimas/projects/logs/activity.log"

def info_to_log_file(log_file):
    with open(log_file, "a+") as file_opened:
        time_now = datetime.now()
        file_opened.write(f'buvo sukurtas: {time_now}\n')

directory = os.path.dirname(log_file) # ./automatizavimas/projects/logs sukuriama pirma direktorija projects/logs
os.makedirs(directory, exist_ok=True)
info_to_log_file(log_file=log_file)

for folder in folders_to_create:
    #folder = ./automatizavimas/projects
    if not os.path.exists(folder): # True kai folderis neegzistuoja       
        os.makedirs(folder)
        info_to_log_file(log_file=log_file)
    if os.path.exists(folder): # True  kai folderis egzistuoja
        print(f'folder: {folder} exists')
    else:
        print((f'tokio folderio: {folder} nera'))

for file in files_to_create: 
    # file = ./automatizavimas/projects/README.md 
    with open(file, "w") as file_opened:
        file_opened.write('Mano daroma programa')
   
    if os.path.exists(file): # True kai failas egzistuoja
        print(f'file: {file} exists')
    else:
        print((f'file: {file} do not exist'))
