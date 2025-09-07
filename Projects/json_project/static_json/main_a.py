import os
import json

def clr():
    import os; os.system('cls' if os.name == 'nt' else 'clear')

def main_a():
    print("\t ______________________________\n"
          "\t|Tugas ke-1                    |\n"
          "\t|Ngambil dan nampilin data     |\n"
          "\t|dari file json local/static   |\n"
          "\t|______________________________|\n\n\n\n")
    
    input("enter ny di pencet dlu ...")

    clr()

    with open(r"static_json\data.json") as path:
        data = json.load(path)

    total = 0
    blm = 0
    
    print("\tPeminjam yang belum mengembalikan buku:\n")
    for nama_org in data["anggota"]:
        for buku in nama_org["pinjam"]:
            total += 1
            if not buku["kembali"]:
                blm += 1
                print(f"\t- {nama_org['nama']} : {buku['judul']} ({buku['tanggal']})")

    print("\n\n\n\tInformasi buku:"
            f"\n\t| Total buku yang dipinjam       : {total}"
            f"\n\t| Total buku yang Belum kembali  : {blm}")
    
    input("\nenternya di pencet dlu ...")
    clr()
