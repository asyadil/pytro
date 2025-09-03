import os
os.system('cls' if os.name == 'nt' else 'clear')

#===set===
daftarGame1 = {"PB", "CSGO, Honkai, Genshin"}
daftarGame2 = {"Naruto PS3", "Genshin", "PB"}
print(f"Daftar game: {daftarGame1}, {daftarGame2}")

def main():
    jumlah_game1 = len(daftarGame1)
    jumlah_game2 = len(daftarGame2)
    total_game = daftarGame1.union(daftarGame2)
    yang_beda = daftarGame2.intersection(daftarGame1)
    kembar = daftarGame2.difference(daftarGame1)
    print(f"Daftar game baru: {daftarGame1}, {daftarGame2}"
        f"\nJumlah daftar game_1 sebanyak '{jumlah_game1}' game"
        f"\nJumlah daftar game_2 sebanyak '{jumlah_game2}' game"
        f"\nSemua game: {total_game}"
        f"\nGame yang di daftar_1 yang tidak ada di daftar_2 dan sebaliknya: {yang_beda}"
        f"\nGame yang ada di daftar_1 yang sekaligus ada di daftar_2 dan sebaliknya:")
main()

def tambahgame():
    print("Tambahkan gamenya!")
    newJumlah1 = input("Masukan jumlah game yang ingin ditambahkan\nke daftar_1: ")
    for i in range(0, int(newJumlah1)):
        newgame1 = input(f"Game ke-{i+1}: ")
        daftarGame1.add(newgame)

    newJumlah2 = input("Masukan jumlah game yang ingin ditambahkan\nke daftar_2: ")
    for i in range(0, int(newJumlah1)):
        newgame2 = input(f"Game ke-{i+1}: ")
        daftarGame1.add(newgame2)
tambahgame()

main()




#gak bisa duplikat katanya value ny
