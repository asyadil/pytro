import json 
print("MATERI 12 - JSON")
print("------------------")
file_json_path = r"/Users/andynur/Dev/belajar-python/sinau-git/rukun_islam.json"
with open(file_json_path, "r") as file_json:
  data_json = json.load(file_json)
  print(f"Judul file: {data_json['judul']}")
  print(f"Jumlah rukun islam: {data_json['jumlah']}")
  print(f"Daftar Rukun islam:")
  for item_rukun in data_json['rukun']:
    print(item_rukun)
  print("-" * 45) # buat garis panjang
  print("Daftar 3 Surah di Al-Qur'an")
  print("-" * 45)
  # tampilkan surah sebagai tabel garis sederhana
  # keys: nomor, nama, jumlah_ayat, tempat_turun
  print("| No | Nama | Jumlah Ayat | Tempat Turun")
  print("-" * 45)
  for surah in data_json['surah']:
    print(f"| {surah['nomor']} | {surah['nama']} | {surah['jumlah_ayat']} | {surah['tempat_turun']} | ")