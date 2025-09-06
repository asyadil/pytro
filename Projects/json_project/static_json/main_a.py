import os
import json

def clr():
    import os; os.system('cls' if os.name == 'nt' else 'clear')

def main_a():
    print("\t ______________________________\n"
          "\t|Tugas ke-1                    |\n"
          "\t|Ngambil dan nampilin data     |\n"
          "\t|dari file json local/static   |\n"
          "\t|______________________________|\n\n\n")
    
    input("enter ny di pencet dlu ...")

    clr()

    with open(r"static_json\data.json") as path:
        data = json.load(path)

    total = belum = 0
    print("Belum kembali:")
    for anggota in data["anggota"]:
        for buku in anggota["pinjam"]:
            total += 1
            if not buku["kembali"]:
                belum += 1
                print(f"- {anggota['nama'].lower()} : {buku['judul']} ({buku['tanggal']})")

    print(f"\n| Total dipinjam: {total}"
          f"\n| Belum kembali: {belum}")
    
    input("enternya di pencet dlu ...")
    clr()
