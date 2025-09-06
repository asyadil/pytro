import requests
import json
import os

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')


def rawr():
    
    print("\t ______________________________\n"
          "\t|Tugas ke-2                    |\n"
          "\t|Ngambil dan nampilin data     |\n"
          "\t|dari file json online/static  |\n"
          "\t|via url                       |\n"
          "\t|______________________________|\n\n\n")
    
    input("enter ny di pencet dlu ...")

def arob():
    # nampilin arab ny
    
    clr()
    
    url = "https://api.alquran.cloud/v1/ayah/2:255/quran-simple"
    response = requests.get(url)
    data = response.json()
    print("Nampilin ayat kursiy:")
    ayat = data['data']['text']
    print(f"\nAyat Kursi:\n{ayat}"
          "\n________________________________________")
    
    input("enter ny pencet dlu ...")
    clr()

def injliz():
    # nampilin english translation ny
    
    url1 = "https://api.alquran.cloud/v1/ayah/2:255/en.asad"
    response_en = requests.get(url1)  
    data_json_en = response_en.json()
    ayat_en = data_json_en['data']['text']
    print(f"\nEnglish translation:\n{ayat_en}"
           "\n________________________________________")

    input("enternya di pencet dlu ...")

def main_b():
    rawr()
    arob()
    injliz()