import requests
from rapidfuzz import process
import os

BASE_URL = "https://api.jikan.moe/v4"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def header(teks):
    print("\t ___________________________________")
    for line in teks.split("\n"):
        print(f"\t| {line:<33}|")
    print("\t|___________________________________|")

def search_anime():
    clear()
    header("Pencarian Anime\nMasukkan nama anime")
    query = input("\n>> ")
    url = f"{BASE_URL}/anime?q={query}&limit=10"
    response = requests.get(url).json()

    if not response["data"]:
        print("\n❌ Tidak ditemukan, coba ejaan lain.")
        input("\nEnter dulu...")
        return

    titles = [anime["title"] for anime in response["data"]]
    best_match = process.extractOne(query, titles)
    print(f"\n🔍 Sugesti terdekat: {best_match[0]} (score: {best_match[1]:.1f})\n")

    print("\t ___________________________________")
    print("\t| Hasil Pencarian Anime             |")
    print("\t|___________________________________|")
    for idx, anime in enumerate(response["data"], start=1):
        print(f"\t{idx}. {anime['title']} ({anime.get('year', 'Unknown')})")

    choice = input("\nPilih nomor untuk detail (enter skip): ")
    if choice.isdigit() and 1 <= int(choice) <= len(response["data"]):
        anime = response["data"][int(choice)-1]
        clear()
        header("Detail Anime")
        print("Judul   :", anime["title"])
        print("Score   :", anime.get("score", "N/A"))
        print("Episode :", anime.get("episodes", "N/A"))
        print("Status  :", anime.get("status", "N/A"))
        print("Sinopsis:", anime.get("synopsis", "Tidak ada sinopsis"))

    input("\nEnter dulu...")

def search_character():
    clear()
    header("Pencarian Karakter\nMasukkan nama karakter")
    query = input("\n>> ")
    url = f"{BASE_URL}/characters?q={query}&limit=10"
    response = requests.get(url).json()

    if not response["data"]:
        print("\n❌ Tidak ditemukan, coba ejaan lain.")
        input("\nEnter dulu...")
        return

    names = [chara["name"] for chara in response["data"]]
    best_match = process.extractOne(query, names)
    print(f"\n🔍 Sugesti terdekat: {best_match[0]} (score: {best_match[1]:.1f})\n")

    print("\t ___________________________________")
    print("\t| Hasil Pencarian Karakter          |")
    print("\t|___________________________________|")
    for idx, chara in enumerate(response["data"], start=1):
        print(f"\t{idx}. {chara['name']}")

    choice = input("\nPilih nomor untuk detail (enter skip): ")
    if choice.isdigit() and 1 <= int(choice) <= len(response["data"]):
        chara = response["data"][int(choice)-1]
        clear()
        header("Detail Karakter")
        print("Nama    :", chara["name"])
        print("Kanji   :", chara.get("name_kanji", "N/A"))
        print("Favorit :", chara.get("favorites", 0))
        print("Tentang :", chara.get("about", "Tidak ada info"))

    input("\nEnter dulu...")

def main():
    while True:
        clear()
        header("=== Myanimelist on the cli ===")
        print("\t1. Cari Anime")
        print("\t2. Cari Karakter")
        print("\t3. Keluar")
        choice = input("\nPilih menu (1/2/3): ")

        if choice == "1":
            search_anime()
        elif choice == "2":
            search_character()
        elif choice == "3":
            clear()
            header("Keluar... bye 👋")
            break
        else:
            print("Pilihan tidak valid!")
            input("\nEnter dulu...")

if __name__ == "__main__":
    main()
