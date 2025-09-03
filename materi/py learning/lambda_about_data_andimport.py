import os
os.system('cls' if os.name == 'nt' else 'clear')
import your_story

your_story.hoshino_ai()
your_story.vladilenna_millize()
your_story.maria_teresa()

# peebandingan funtion biasa dan funtion lambda/ anonim function

#fungsi biasa 
def fungsi_1(nama):
    print(f"nih, fungsi biasa {nama}")

# fungsi lambda
fungsi_2 = lambda nama: print(f"nih, fungsi lambda {nama}")

# pemanggilan fungsi
print("____________________________________")
fungsi_1("Aloy")
fungsi_1("Aliy")
print("\n=== yg atas function biasa, yg bawah pake lambda ===\n")
fungsi_2("Aluy")
fungsi_2("Aley")
print("____________________________________")

#bedanya cuma di penulisan aja, kalau fungsi biasa harus pakai def, kalau lambda cukup pakai lambda aja
#tapi kalau fungsi biasa bisa lebih kompleks, sedangkan lambda hanya untuk fungsi sederhana
#biar kalo misalnnya cuma butuh satu baris kode, nulis nya gk ribet

#______________________________________________________________________________________________________

# ini cara manipulasi data
data_num = [1, 28.9, 7, 65.4, 45, 43, 54, 6, 6.8, 5, 4.76, 0.3, 231, 76]
pembulatan_data = map(lambda nilai: round(nilai), data_num)
nilai_dibulatkan = list(pembulatan_data)
print(nilai_dibulatkan)

int_to_str = 4
int_to_str = str(int_to_str)
str_to_int = "15"
str_to_int = int(str_to_int)

print(str_to_int, int_to_str)
print("______________________________________")

# sorted data ('alal hal number)

data_num = [
    {"nama": "Aloy", "nilai": 97.6},
    {"nama": "aliy", "nilai": 88.1},
    {"nama": "aluy", "nilai": 69.9},
    {"nama": "aley", "nilai": 82.3}
    ]

print("data sebelum diurutkan", data_num)

data_num.sort(key=lambda x: x["nilai"])
print("data setelah diurutkan", data_num)

print("klo pake for loop gini juga bisa:")
for data in data_num:
    print(f"nama: {data['nama']}, nilai: {data['nilai']}")
print("______________________________________")

#sorting list
daftar_nama = ["cAloy", "bAliy", "Aluy", "fAley", "dAlay"]
nama_terurut = sorted(daftar_nama)
print(f"daftar nama sebelum diurutkan:\n {daftar_nama}")
print(f"daftar nama setelah diurutkan:\n {nama_terurut}")
nama_terbalik = sorted(daftar_nama, reverse=True)
print("daftar nama setelah diurutkan terbalik:\n", nama_terbalik)

#higher order function, filtering data

print("\t____________Filtering Data___________")

transaksi = [
    50000, 150000, 200000, 304000, 105000, 250000, 5000, 2500, 5000, 10000, 3000, 6000
]

transaksi_besar = filter(lambda x: x > 100000, transaksi)
transaksi_besar = list(transaksi_besar)

transaksi_kecil = filter(lambda x: x < 100000, transaksi)
transaksi_kecil = list(transaksi_kecil)

print(
    f"transaksi: {transaksi}\n"
    f"transaksi besar: {transaksi_besar}"
      f"\ntransaksi kecil: {transaksi_kecil}")

hoshino_ai()
vladilenna_millize()
maria_teresa()