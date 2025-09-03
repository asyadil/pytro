import os
os.system('cls' if os.name == 'nt' else 'clear')

# Tugas ke-1
def jadwal_piket():
    print("_______________________________________________________________________")
    print("Jadwal Piket Hari-yadi:")
    jadwal_piket = ["Aloy", "Loloy", "Baloy", "Trondol"]
    for i in jadwal_piket:
        print("-", i)
jadwal_piket()

# Tugas ke-2
def rukun_iman():
    print("_______________________________________________________________________")
    print("Kepercayaan kita:")
    rukun_iman = ("Syahadat", "Sholat", "Zakat", "Puasa", "Haji")
    number = 1
    for i in rukun_iman:
        print(f"{number}. {i}")
        number += 1
rukun_iman()

# Tugas ke-3
def kitab_sihir():
    print("_______________________________________________________________________")
    print("Kitab Sihir yang dipelajari Frieren")
    kitab_sihir = {"Grimoire of Armadel", "The Key of Solomon", "The Book of Abramelin"}
    for i in kitab_sihir:
        print("-", i)
kitab_sihir()

# Tugas ke-4
def bio_ali():
    bio = {"Nama": "Ali", "Umur": 15, "Hobi":"Melakukan hal yang bermanfaat", "Cita-cita":"Masuk surga"}
    print("_______________________________________________________________________")
    print("Biodata Ali")
    for key, value in bio.items():
        print(f"{key}: {value}")
bio_ali()