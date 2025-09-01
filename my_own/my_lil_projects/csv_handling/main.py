import os
import csv

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear()
    print("\t ___________________________________\n"
          "\t| Selamat pergi, ini tugas Ali,     |\n"
          "\t| sok, dijalanin...                 |\n"
          "\t|___________________________________|")
    input("\n\n\nEnter nya, dipencet dlu, boleh..")
    clear()

    #manggilin pungsi
    t_1()
    t_2()
    t_3()


def t_1():
    print("\t ____________________________________\n"
          "\t| Tugas pertama, nampilin semua data |\n"
          "\t| dengan format yang ditetapkan...   |\n"
          "\t|____________________________________|")
    input("\n\n\nEnter nya dipencet dlu, boleh..")
    clear()

    with open('data.csv', mode='r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    print("Data Keuangan:")
    for row in data:
        print(f"{row['Tanggal']} | {row['Keterangan']} | {row['Kategori']} | Rp{row['Jumlah']}")
    input("\n\n\nEnternya dipencet dlu, boleh...")
    clear()

def t_2():
    print("\t ____________________________________\n"
          "\t| Tugas kedua, nampilin total jumlah |\n"
          "\t| pengeluaran...                     |\n"
          "\t|____________________________________|")
    input("\n\n\nEnternya dipencet dlu, boleh...")
    clear()

    with open('data.csv', mode='r') as file:

        reader1 = csv.reader(file)
        data = list(reader1)
        print("\t ___________________________________\n"
            "\t| Data mentah pengeluaran:          |\n"
           f"\t| {data[1][3]} + {data[2][3]} + {data[3][3]}             |\n"
           f"\t| + {data[3][3]} + {data[5][3]} + {data[6][3]} + {data[7][3]}   |")

        file.seek(0)  # pas sercing di gologolo, katanya harus dibalikin dulu cursosrnya ke awal

        reader2 = csv.DictReader(file)
        data = list(reader2)
        total_pengeluaran = sum(int(row['Jumlah']) for row in data)
        print(  f"\t| Total Pengeluaran:                |"
              f"\n\t|    Rp{total_pengeluaran}                       |"
               "\n\t|___________________________________|")

    input("\n\n\nEnternya dipencet dlu, boleh...")
    clear()
    
def t_3():

    print("\t ___________________________________\n"
          "\t| Tugas ketiga, nampilin total      |\n"
          "\t| pengeluaran per kategori...       |\n" \
          "\t|___________________________________|")
    input("\n\n\nEnternya dipencet dlu, boleh...")

    with open('data.csv', mode='r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    total_perkategori = {}
    for row in data:
        kategori = row['Kategori']
        jumlah = int(row['Jumlah'])

        if kategori not in total_perkategori:  
            total_perkategori[kategori] = 0  
        total_perkategori[kategori] += jumlah

    print("\t______________________________"
          f"\n\tPengeluaran per Kategori:\n")
    for kategori, total in total_perkategori.items():
        print(f"\t- {kategori}: Rp{total}")
    print("\t______________________________\n")
    
    input("\n\n\nEnternya dipencet dlu, boleh...")
    clear()


main()