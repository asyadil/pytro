import requests

BASE = "https://api.alquran.cloud/v1"

#fungsi utama:
def tiga_surah_pertama():
    try:
        url = f"{BASE}/surah"
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()['data']

        print("3 Surah Pertama:")
        for s in data[:3]:
            print(f"{s['number']}. {s['englishName']} ({s['numberOfAyahs']} ayat)")
    #error handling nya bre
    except requests.RequestException as e:
        print("Gagal mengambil data surah:", e)

def alfatihah_ayat_1_3():
    try:
        url = f"{BASE}/surah/1"
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        detail = r.json()['data']

        print("\nSurah Al-Fatihah (Ayat 1–3):")
        for a in detail['ayahs'][:3]:
            print(f"{a['numberInSurah']}. {a['text']}")
    except requests.RequestException as e:
        print("Gagal mengambil detail Al-Fatihah:", e)

def bagianB():
    tiga_surah_pertama()
    alfatihah_ayat_1_3()

