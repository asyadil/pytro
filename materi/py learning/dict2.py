import os
os.system('cls' if os.name == 'nt' else 'clear')

def input_identitas():
    nama = input("Masukan nama:\n")
    kelas = input("Masukan kelas:\n")
    jenis_kelamin = input("Masukan jenis kelamin:\n")
    umur = input("Masukan umur:\n")
    return nama, kelas, jenis_kelamin, umur
nama, kelas, jenis_kelamin, umur = input_identitas()

def inputnilai():
    ipa = int(input("Masukan nilai akhir IPA:\n"))
    mtk = int(input("Masukan nilai akhir MTK:\n"))
    b_indo = int(input("Masukan nilai akhir B. Indonesia:\n"))
    b_ing = int(input("Masukan nilai akhir B. Inggris:\n"))
    return ipa, mtk, b_indo, b_ing
ipa, mtk, b_indo, b_ing = inputnilai()

dict = {

    "identitas":{
        "nama":nama,
        "kelas":kelas,
        "jenis kelamin":jenis_kelamin,
        "umur":umur
        },

    "nilai akhir":{
        "ipa":ipa,
        "mtk":mtk,
        "b_ing":b_ing,
        "b_indo":b_indo
    }
}

def hasil():
    print(
        f"\nIdentitas siswa:\n"
        f"  Nama             : {dict['identitas']['nama']}\n"
        f"  Kelas            : {dict['identitas']['kelas']}\n"
        f"  Jenis kelamin    : {dict['identitas']['jenis kelamin']}\n"
        f"  Umur             : {dict['identitas']['umur']}\n"
        f"\nNilai akhir    :\n"
        f"  IPA              : {dict['nilai akhir']['ipa']}\n"
        f"  MTK              : {dict['nilai akhir']['mtk']}\n"
        f"  B. Indonesia     : {dict['nilai akhir']['b_indo']}\n"
        f"  B. Inggris       : {dict['nilai akhir']['b_ing']}\n"
        f"  Rata-rata        : {(dict['nilai akhir']['ipa'] + dict['nilai akhir']['mtk'] + dict['nilai akhir']['b_indo'] + dict['nilai akhir']['b_ing']) / 4:.2f}\n"
        f"\t{'=== Lulus ===' if dict['nilai akhir']['ipa'] >= 75 and dict['nilai akhir']['mtk'] >= 75 and dict['nilai akhir']['b_indo'] >= 75 and dict['nilai akhir']['b_ing'] >= 75 else ' (Tidak lulus)'}"
    )
hasil()