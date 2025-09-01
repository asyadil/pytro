import os
os.system('cls' if os.name == 'nt' else 'clear')
import json

path = r"C:\Users\ASUS\Desktop\py\filehandling\jip.json"

# buka file json
with open(path, 'r') as file:
    data = json.load(file)

#rukun iman
def rkn_iman():
    jdl = data["Rukun iman"]["judul"]
    jmlh = data["Rukun iman"]["jumlah"]
    rkn = data["Rukun iman"]["Al-Arkanul iman"]

    print(f"\nJudul: {jdl}"
        f"\nJumlah: {jmlh}"
        )
    nmr = 1
    for  i in rkn:
        print(f"{nmr}. {i}")
        nmr += 1

#klo ini rkn islam ny
def rkn_islm():
    jdl = data["Rukun Islam"]["judul"]
    jmlh = data["Rukun Islam"]["jumlah"]
    rkn = data["Rukun Islam"]["Arkanul Islam"]

    print(f"\nJudul: {jdl}"
        f"\nJumlah: {jmlh}"
        )
    nmr = 1
    for  i in rkn:
        print(f"{nmr}. {i}")
        nmr += 1

def ply():
    rkn_iman()
    rkn_islm()
ply()