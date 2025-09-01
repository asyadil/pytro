#jangan dihiraukan
import os
os.system('cls' if os.name == 'nt' else 'clear')

#Tugas Aloy, asikk
#____________________________

#material pelengkap:
def garis():
    print(f"\t________________________________________________________\n")
def pause():
    input("\nTekan Enter ntuk lanjut, masse...")

#fungsi2 utama
def main_menu():
    #menu utama

    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    # biar kalo selesai satu halaman balik ke halaman utama
    while True:
        print("\t=> youkoso! ni tugas Aloy <=\n")
        garis()
        print("1. Tugas Satu: Importing sederhana")
        print("2. Tugas Dua: Hitung Uang dengan Lambda, Map, dan Filter")
        print("3. Tugas Tiga: Ranking Nilai dengan Sorted, Max, dan Min")
        print("4. Tugas Empat: convert list ke Emoji")
        print("5. Tugas Lima: Mutabaah Digital")
        print("6. Keluar")
        garis()
        menu = input("Pilih nomor tugas (1-6): ")

        if menu == '1':
            tugas_satu()
        elif menu == '2':
            tugas_dua()
        elif menu == '3':
            tugas_tiga()
        elif menu == '4':
            tugas_empat()
        elif menu == '5':
            tugas_lima()
        elif menu == '6':
            print("Terima kasih.\nIya sama-sama")
            exit()
        else:
            print("Pilihan tidak valid. Silakan pilih 1-6.")
            main_menu()
    
def tugas_satu():
    #Tugas satu, materi import
    import hadits2
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\t=> Kumpulan Ayat Alquran dan Hadits <=\n")
    garis()
    hadits2.hadits_semangat()
    garis()
    hadits2.hadits_ikhlas()
    garis()
    hadits2.ayat_takdir()
    garis()
    hadits2.ayat_ikhlas()
    garis()
    hadits2.ayat_hakikat_penciptaan()
    pause()

def tugas_dua():
    # Tugas dua, materi lambda, map(), and filter()

    # import modul hitung uang, nih
    import hitungator
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    #naro list wang:
    wang = [1000, 2000, 5000, 10000, 20000, 50000, 100000]

    print("\t=> Hitung uang <=\n")
    garis()
    print("List data mentah uang anda:", wang)

    # impor fungsi dari hitungator
    garis()
    hitungator.dikirim_wang(wang)
    print("\nWang sudah dikirim, oleh ortu anda\nini saldo akhir anda:", hitungator.dikirim_wang(wang))
    garis()
    hitungator.filter_mubazir(wang)
    print("\nJangan mubazir, sodara setan, tauk\nnih, pemubaziran anda:", hitungator.filter_mubazir(wang))
    pause()

def tugas_tiga():
    # Tugas tiga: sorted(), max(), dan min()

    # impor modul ranking ny dlu
    import ranking
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    #list nya, nih
    nilai = [100, 89.5, 79, 97.5, 98, 87, 92, 79.5]

    print("\t=> Ranking nilai <=\n")
    garis()
    print("List nilai mentah:", nilai)

    # importing fungsi dari modul ranking
    ranking.urutkan_nilai(nilai)
    print("\nNilai klo diurutkan:", ranking.urutkan_nilai(nilai))

    ranking.nilai_tertinggi(nilai)
    print("Nilai tertinggi:", ranking.nilai_tertinggi(nilai))

    ranking.nilai_terendah(nilai)
    print("Nilai terendah:", ranking.nilai_terendah(nilai))
    pause()

def tugas_empat():
    # Tugas empat
    
    #ngimpor modul ny
    import feelin
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    # list mood
    mood_list = ["senang", "biasa", "sedih", "semangat", "biasa"]
    garis()
    
    print("\t=> Mood orang2 hari ni <=\n")
    print("List mood:", mood_list)

    # panggil fungsi convertor dari modul feelin'
    mood_emoji = feelin.convert_mood(mood_list)
    print("\nMood orang2 hari ni dlm icon:", mood_emoji)
    pause()

def tugas_lima():
    # Tugas lima
    garis()

    # import modul mutabaah
    import mutabaah
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    # list halaman yang dibaca
    data_hlmn_mnth = [5, 10, 8, 7, 6, 9, 4]
    garis()
    # fungsi total_ngaji dari modul mutabaah
    total_halaman = mutabaah.total_ngaji(data_hlmn_mnth)
    print(f"\n\t--> Mutabaah digital <---")
    garis()
    print(f"\n\thalaman yg dibaca setiap hari dlm seminggu:"
        f"\n\t{data_hlmn_mnth}"
        f"\n\tTotal halaman yang dibaca dalam seminggu:"
        f"{total_halaman}"
        f"\n\tTarget halaman per minggu: 35 halaman")
    garis()
    # fungsi cek_target dari modul mutabaah
    tercapai_kgk = mutabaah.cek_target(total_halaman)
    print("\tStatus target:", tercapai_kgk)
    garis()
    pause()

#jalanin main menu, dari situ manggil fungsi2 lain
main_menu()