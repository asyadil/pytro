import time
def bersihkan_layar():
    print("\n" * 100)
    time.sleep(0.3)

def nanyain_nama():    
    print(
        "Halo bre, ape kabar?"
        )
    input()
    bersihkan_layar()    
    print(
        "Ok kalo boleh tau, nih ye, nama ente siape, nama panggilannye?"
        )
    nama = input()
    bersihkan_layar()
    print(
        "owwh... ok-ok, kalo nama panjangnye?"
        )
    nama_panjang = input()
    bersihkan_layar()
    return nama, nama_panjang
nama, nama_panjang = nanyain_nama()

def nanyain_jenis_kelamin():
    print(
        f"{nama}, ente laki apa cewek?"
        )
    jenis_kelamin = input()
    return jenis_kelamin
jenis_kelamin = nanyain_jenis_kelamin()
bersihkan_layar()

def nanyain_umur():
    print(
        f"Ok, {nama}, kalo boleh tau, ente nih\n"
        f"sekarang udah umur berape?"
        )
    umur = input()
    return umur
umur = nanyain_umur()
bersihkan_layar()

def nanyain_hobi():
    print(
        f"{nama}, kalo hobi ente apa?"
        )
    hobi = input()
    return hobi
hobi = nanyain_hobi()
bersihkan_layar()

def nanyain_siswa_apa_karyawan():
    print(
        f"Nah, sekarang ane minta tolong ke ente dong,\n"
        f"kalo misalkan ente masih pelajar ketik '1' kalo bukan pelajar/udah kerja ketik '2'"
        )
    siswaAPAkaryawan = input()
    return siswaAPAkaryawan
siswaAPAkaryawan = nanyain_siswa_apa_karyawan()
bersihkan_layar()

if siswaAPAkaryawan == '1':
    print(
        f"owh... masih pelajar, ya\n"
        f"udah kelas berapa emang nye, ente sekarang?"
        )
    kelas = input()
    bersihkan_layar()

elif siswaAPAkaryawan == '2':
    print(
        f"wah, ternyata ente bukan pelajar, ya, {nama}\n"
        f"emm.. maaf ya, kalo kesinggung. ente kerja, apa nganggur, nih?"
        )
    print(
        f"kalo ente kerja ketik '1' kalo kagak kerja ketik '2'\n"
        f"kalo gak mau jawab juga, gak papa, silahkan..."
        )
    kerjaAPAenggak = input()
    bersihkan_layar()

    if kerjaAPAenggak == '1':
        print(
            f"widiiih... dah kerja...\n"
            f"Kerja ape emang nye?"
            )
        kerja = input()
        bersihkan_layar()
    
    if kerjaAPAenggak == '2':
        print(
            f"owh... yaudah... kagak papa,\n"
            f"moga - moga cepet dapet kerjaan, ye"
            )
        bersihkan_layar()

def nanyain_nice():
    print(
        f"oke... lanjut...\n"
        f"{nama}, ente nih, kalo pengen digambarin tuh, sukanya apaan,\n"
        f"maksudnya tuh, ente tuh orangnya suka apaan..."
        )
    
    print(
        f"______________________________________________________\n"
        f"1.[ Nonton anime, wibu, otaku]\n"
        f"2.[ Gamer, sukanya main game aje]\n"
        f"3.[ Bola!!!, fans fanatik tim bola tertentu]\n"
        f"4.[ Anak alim, sukanya ngaji, tadarusan, dll]\n"
        f"5.[ Sukanya nonton Drakor / K-pop]\n"
        f"6.[ Hobi nonton film - film box office]\n"
        f"7.[ Suka literasi/literatur, sukanya baca-baca/nulis-nulis]\n"
        f"8.[ yang, lain...]\n"
        f"______________________________________________________"
        )
    opsiTipe = input()
    return opsiTipe
opsiTipe = nanyain_nice()
bersihkan_layar()

if opsiTipe == '1':
    print(
        f"widih... satu suku bangsa kita, hehe\n"
        f"kalo waifu ente siape, bre?"
     )
    waifu = input()
    print(f"si {waifu}, tuh, dari anime mana emangnye?")
    dari_anime = input()
bersihkan_layar()

if opsiTipe == '2':
    print(
        f"beuuhh... ngegame...\n"
        f"main game ape emangnya ente, {nama}?"
        )
    gamer = input()
bersihkan_layar()

if opsiTipe == '3':
    print(
        f"Asikk... si {nama}... gile bola ternyata dia,\n"
        f"ente ngefans sama klub bola mana emanye?"
        )
    bola = input()
    bersihkan_layar()
    print("Dari liga mana ntuh, klub nye?")
    liga = input()
    bersihkan_layar()

if opsiTipe == '4':
    print(f"Masyaalloohhh... ustadz {nama}... hehe\n"
          f"btw ente udah berapa juz, nih, hafalannya... ustadz {nama}?"
          )
    hafalan = input()
bersihkan_layar()

if opsiTipe == '5':
    print(
        f"Oohh... sukanya nonton drakor, ye\n"
        f"judul drakor kesukaan ente apa, emangnya, tuh?"
        )
    drakor = input()
bersihkan_layar()

if opsiTipe == '6':
    print(
        f"Nonton film, tuh emang asik, beneran dah, apalagi kalo filmnya seru, hehe\n"
        )
    nontonfilm = input()
bersihkan_layar()

if opsiTipe == '7':
    print(
        f"Waahh... ternyata ada orang cerdas disini...\n"
        f"{nama}, ente suka baca buku apa, emangnya? novel ato apa?\n"
        )
    sukabaca = input()
bersihkan_layar()

if opsiTipe == '8':
    print(
        f"emangnye, ente sukanya paan {nama}?"
        )
    tipelain = input()
bersihkan_layar()

def nanyain_mimpi():
    print(
        f"Emm... mungkin ini bakalan jadi agak deep, sih...\n"
        f"kalo boleh tau, impian ente yang paliiiing... banget ente pengen gapai itu, ape?"
        )
    mimpi = input()
    return mimpi
mimpi = nanyain_mimpi()
bersihkan_layar()

print(
    f"okeeh... alhamdulillah, udah selesai, wawancara ane, hehe\n"
    f"sekarang bakal ane rekapin semua yang tadi tadi ntuh, ye"
    )

print(
    f"Nama Panjang: {nama_panjang}\n"
    f"Nama Panggilan: {nama}\n"
    f"Jenis Kelamin: {jenis_kelamin}\n"
    f"Umur: {umur}\n"
    f"Kira-kira lahir di tahun: {2025 - int(umur)}\n"
    f"Hobi: {hobi}"
    )
    
if siswaAPAkaryawan == '1':
    print(f"Kelas: {kelas}\n")
elif kerjaAPAenggak == '1':
    print(f"Kerjaan: {kerja}\n")
if opsiTipe == '1':
    print(
        f"Orangnye: Suka nonton anime, waifunya: {waifu}\n"
        f"          dari anime {dari_anime}"
        )
elif opsiTipe == '2':
    print(
        f"Orangnye: Gamer\n"
        f"Game favoritnya: {gamer}\n"
        )        
elif opsiTipe == '3':
    print(
        f"Orangnye: 'Maniak Bola'\n"
        f"Klub  favorit: {bola}"
        )        
elif opsiTipe == '4':
    print(
        f"Orangnye: 'Alim'\n"
        f"Hafalannye udah sampe: {hafalan} juz\n"
        )        
elif opsiTipe == '5':
    print(
        f"Orangnye: 'Suka Drakor-an'\n"
        f"Drakor favorit: {drakor}"
        )
elif opsiTipe == '6':
    print(
        f"Orangnye: 'Suka Nonton Film'\n"
        f"Film favorit nye: {nontonfilm}\n"
        )
elif opsiTipe == '7':
    print(
        f"Orangnye: 'Cerdas'\n"
        f"Suka baca buku: {sukabaca}\n"
        )
elif opsiTipe == '8':
    print(
        f"Orangnye: keren, soalnye dia '{tipelain}'"
    )
print(f"Mimpinya: {mimpi}")
print(
    f"_______________________________________________\n"
    f"makasih, udah mau diwawancarain ama ane, ya, {nama} hehe\n"
    f"moga sukses selalu, ye\n"
    f"________________________________________________"
    f"\n * 6"
    )