import os
import csv
import json

os.system('cls' if os.name == 'nt' else 'clear')

# Baca file CSV
file_path = r"random/filehandling/data.csv"
with open(file_path, mode='r') as data_istri:
    ngopen = csv.reader(data_istri)
    list_data = list(ngopen)

#nampilin list data
def nih():
    # Menampilkan data yang ada di file CSV
    for i in list_data:
        print(i)

# input dan modifikasi data
def modifikasi_data():
    while True:
        try:
            nomor = int(input("Masukkan nomor istri: "))
            if nomor < 1 or nomor > len(list_data) - 1:
                print("Nomor tidak valid. Silakan coba lagi.")
                continue
            nama_istri = list_data[nomor][1]
            print(f"Nama istri ke-{nomor} adalah {nama_istri}.")
            
            # mengubah nama istri:
            ubah_nama = input(f"Ingin mengubah nama istri ke-{nomor}? (y/n): ")
            if ubah_nama.lower() == 'y':
                nama_baru = input("Masukkan nama baru: ")
                list_data[nomor][1] = nama_baru  # Memperbarui nama istri

                # Menyimpan data yang sudah diperbarui ke file CSV
                with open(file_path, mode='w', newline='') as file_istri:
                    writer = csv.writer(file_istri)
                    writer.writerows(list_data)  # Menulis ulang seluruh data yang sudah dimodifikasi

                print("Nama berhasil diubah dan disimpan ke file CSV!")
                break  # Keluar dari loop setelah berhasil mengubah data
            
            if ubah_nama.lower() == 'n':
                print("Tidak ada perubahan yang dilakukan.")
                break  # Keluar dari loop jika tidak ada perubahan

        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

# nambah data istri baru
def tambah_data():
    while True:
        try:
            nama_baru = input("Masukkan nama istri baru: ")
            if not nama_baru.strip():
                print("Nama tidak boleh kosong. Silakan coba lagi.")
                continue
            
            #klo nama dah ad bilang, dah ad
            if any(nama_baru == row[1] for row in list_data):
                print("Nama sudah ada. Silakan masukkan nama lain.")
                continue

            # Menambahkan data baru ke list_data
            list_data.append([len(list_data), nama_baru])

            # Menyimpan data yang sudah diperbarui ke file CSV
            with open(file_path, mode='w', newline='') as file_istri:
                writer = csv.writer(file_istri)
                writer.writerows(list_data)  # Menulis ulang seluruh data yang sudah dimodifikasi

            print("Data baru ditambahkan dan disimpan ke file CSV")
            break  # Keluar dari loop
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

def hapus_data():
    while True:
        try:
            nomor = int(input("Masukkan nomor istri yang ingin dihapus: "))
            if nomor < 1 or nomor > len(list_data) - 1:
                print("Nomor tidak valid. Silakan coba lagi.")
                continue
            konfirmasi = input(f"Yakin ingin menghapus istri ke-{nomor} ({list_data[nomor][1]})? (y/n): ")
            if konfirmasi.lower() == 'y':
                list_data.pop(nomor)
                # Update nomor urut setelah penghapusan
                for idx in range(1, len(list_data)):
                    list_data[idx][0] = idx
                with open(file_path, mode='w', newline='') as file_istri:
                    writer = csv.writer(file_istri)
                    writer.writerows(list_data)
                print("Data berhasil dihapus dan disimpan ke file CSV")
                break
            else:
                print("Penghapusan dibatalkan.")
                break
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

def mainmenu():
    while True:
        print("Data Istri, dlm csv:")
        nih()
        print("\nMenu:")
        print("1. Modifikasi Data")
        print("2. Tambah Data")
        print("3. Hapus Data")
        print("4. Keluar")
        opsi = input("Pilih menu (1/2/3/4): ")
        if opsi == '1':
            modifikasi_data()
        elif opsi == '2':
            tambah_data()
        elif opsi == '3':
            hapus_data()
        elif opsi == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

mainmenu()
