import os
os.system('cls' if os.name == 'nt' else 'clear')
from colorama import init, Fore, Back, Style
init()

print(Fore.GREEN + " === Welcome to 'Inputor_Data_Siswa' ===")
list = []
print(Fore.LIGHTCYAN_EX + "Silakan masukan jumlah siswa\nyang akan dimasukan data-datanya :")
jumlah = int(input())

for i in range(0, jumlah):
    data = input(Fore.RED  + f"Masukan nama dari siswa ke-{i+1} : ")
    list.append(data)
    data = input("Masukan kelas: ")
    list.append(data)
    data = input(Fore.YELLOW + f"Masukan jenis kelamin dari siswa ke-{i+1}: ")
    list.append(data)
    nilai = int(input(Fore.CYAN + f"Masukan nilai akhir dari siswa ke-{i+1}:"))
    list.append(nilai)
    if nilai >= 75:
        print(Fore.YELLOW + "Siswa tersebut lulus")
    if nilai < 75:
        print(Fore.RED + "Siswa tersebut tidak lulus")

print(Back.YELLOW + Fore.WHITE + "Rekap data akhir: ", list )
