#bitcoin converter
import os
os.system('cls' if os.name == 'nt' else 'clear')

print(
    "=== Asik, banyak bitcoin nya ===\n"
    "itung, yok, kalo ke rupiah/dollar, jadi berapa"
    )

bitcoin = int(input("Masukin jumlah bitcoin yang lu punya sekarang:\n"))
import_kemana = input("Mo di konversi ke rupiah apa dollar?\nKlo mau ke rupiah ketik '1', klo mau ke dollar ketik '2'\n")
if import_kemana == '1':
    print(f"Jumlah bitcoin lu sekarang {bitcoin} BTC, ye. kalo di konversi ke rupiah jadi {bitcoin * 500000000} IDR\nOrang tajir, lu ye, bagi-bagi dong")
elif import_kemana == '2':
    print(f"Jumlah bitcoin lu sekarang {bitcoin} BTC, ye.\nKlo di konversi ke dollar jadi {bitcoin * 30000} USD\nOrang tajir lu, ye, bagi-bagi dong")
else:
    print("Ngisi inpout tuh, yang bener, ngulang lagi, ye.")