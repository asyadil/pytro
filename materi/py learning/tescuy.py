import os
os.system('cls' if os.name == 'nt' else 'clear')

def main():
    set = []
    print("Masukan jumlah game yang anda mainkan: ")
    jumlah_game = input()
    for i in range(0,int(jumlah_game)):
        print(f"Nama game ke-{i+1}: ")
        nama_game = input()
        set.append(nama_game)
    print(f"Game-game yang anda mainkan: {set}")

main()
