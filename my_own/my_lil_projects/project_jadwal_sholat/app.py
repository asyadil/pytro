import requests
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

while True:
    #start page
    print("\t_________________________________________")
    print("\tSelamat pergi di program ini!"
        "\n\tini buat ngecek jadwal sholat di kota ente hari ini")
    print("\t_________________________________________")
    input ("\t\n\n\nTekan enter untuk lanjut...")
    clear()
    namakota = input(
        "\t__________________________________________\n"
        "\tNah, karang biar bisa ditampilin jadwal sholatnya,\n"
        "\tKetikan nama kota ente sekarang: \n"
        "\t__________________________________________\n"
        "\t\n\n\nKota: ")
    date_and_time = time.strftime("%d-%m-%Y")  # Format tanggal ny udh sesuai buat url

    url = f"https://api.aladhan.com/v1/timingsByCity/{date_and_time}?city={namakota}&country=Indonesia&method=20"

    response = requests.get(url)
    data_json = response.json()
    clear()

    #hasil ny    
    print(f"\tngasiiiiiiiiiikkk,\n"
        f"\tnih, jadwal sholat hari ni di {namakota}:")
    print("\t+-----------------+----------+")
    print(f"\t| {'Sholat':<15} | {'Waktu':<8} |")
    print("\t+-----------------+----------+")
    print(f"\t| {'Imsak':<15} | {data_json['data']['timings']['Imsak']:<8} |")
    print(f"\t| {'Subuh':<15} | {data_json['data']['timings']['Fajr']:<8} |")
    print(f"\t| {'Dzuhur':<15} | {data_json['data']['timings']['Dhuhr']:<8} |")
    print(f"\t| {'Ashar':<15} | {data_json['data']['timings']['Asr']:<8} |")
    print(f"\t| {'Maghrib':<15} | {data_json['data']['timings']['Maghrib']:<8} |")
    print(f"\t| {'Isya':<15} | {data_json['data']['timings']['Isha']:<8} |")
    print("\t+-----------------+----------+")
    print("\tJangan lupa sholat ye bree..")
    
    exit = input("\tMau keluar, apa masih mo nanya lagi? (y/n): ")
    
    if exit.lower() == 'y':
        break
    
    if exit.lower() == 'n':
        clear()
        continue

exit