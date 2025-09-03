import os
os.system('cls' if os.name == 'nt' else 'clear')

print("=== Welcome! Ini program menggunakan function di Python! ===")

def identity_input():
    name = input("Nama nya siapa?\n")
    age = int(input("Umur nya?\n"))
    maried = jumlah_istri = pekerjaan = sekolah_kgk = kelas = None

    if age >= 18:
        maried = input("Sudah nikah belum?\nKalau sudah jawab '1', kalau belum jawab '2'\n")
        if maried == "1":
            jumlah_istri = input("Wah, berapa istri nya?\n")
        elif maried == "2":
            print("Semoga cepat nikah, ya")
        kerja_kgk = input("Sudah kerja belum?\nKalau sudah ketik '1', kalau belum ketik '2'\n")
        if kerja_kgk == "1":
            pekerjaan = input("Kerjanya jadi apa?\n")
        elif kerja_kgk == "2":
            print("Maaf ya, semoga cepat dapat kerjaan")
    else:
        sekolah_kgk = input("Sekolah nggak?\nKalau masih sekolah jawab '1', kalau putus sekolah jawab '2'\n")
        if sekolah_kgk == "2":
            print("Waduh, maaf ya nanya nya nggak sopan")
        elif sekolah_kgk == "1":
            kelas = input("Kelas berapa?\n")
    return name, age, maried, sekolah_kgk, jumlah_istri, kelas, pekerjaan

def final_output(name, age, maried, sekolah_kgk, jumlah_istri, kelas, pekerjaan):
    print(f"\nOk, nama lu '{name}'. Umur lu '{age}', jadi kira-kira lu lahir tahun '{2025-age}'")
    if age >= 18:
        if maried == "1":
            print(f"Tadi lu bilang, lu udah nikah, istri lu sekarang ada {jumlah_istri}")
        elif maried == "2":
            print("lu belum menikah.")
        if pekerjaan:
            print(f"Lu kerja jadi {pekerjaan}")
        else:
            print("Lu kagak kerja.")
    else:
        if sekolah_kgk == "1":
            print(f"Lu masih sekolah, kelas {kelas}")
        elif sekolah_kgk == "2":
            print("LU PUTUS SEKOLAH.")

name, age, maried, sekolah_kgk, jumlah_istri, kelas, pekerjaan = identity_input()
final_output(name, age, maried, sekolah_kgk, jumlah_istri, kelas, pekerjaan)
