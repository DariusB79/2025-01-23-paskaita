import os

# Elementarus budas

#os.mkdir("./projects")
#os.mkdir("./projects/data")
#os.mkdir("./projects/scripts")
#os.mkdir("./projects/logs")

#with open("./projects/README.md", "w") as file:
    #file.write("Duomenu irasymui : ")


# Gudresnis budas :-) 

create_folder = ["./projects","./projects/data", "./projects/scripts", "./projects/logs" ]
create_file = ["./projects/README.md"]

for folder in create_folder:
    if not os.path.exists(folder):
         os.mkdir(folder)
    if os.path.exists(folder):
         print(f"folderis : {folder} egzistuoja")
    else:
         print(f"tokio folderio {folder} nera")

for file in create_file:
     with open(file, "w") as open_file:
          open_file.write("Ivedami nauji duomenys: ")

     if os.path.exists(file):
          print(f"Sis failas - {file}  jau egzistuoja")
     else:
          print(f"Tikio failo - {file} - NERA")


