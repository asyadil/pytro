# mutabaah, asikkkkkkkkkk

# fungsi ini, buat notalin jumlah halaman di dlm list ny, nanti
def total_ngaji(data_halaman):
    return sum(data_halaman)

# klo ini buat ngecek dah sesuai target apa blon
def cek_target(total, target=35):
    if total >= target:
        return "Tercapai, asikk"
    else:
        return "Belum tercapai, terlalu santai"
