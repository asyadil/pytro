from PIL import Image
import subprocess
import os

# Path input/output
input_path = r"C:\fastfetch-windows-amd64\hoshino_logo.png"
resized_path = r"C:\fastfetch-windows-amd64\hoshino_logo_fixed.png"
output_path = r"C:\fastfetch-windows-amd64\hoshino_logo2.ansi"

# --- Step 1: Resize gambar biar proporsional ---
# (karena terminal karakter lebih tinggi dari lebarnya, rasio diatur)
img = Image.open(input_path)

# resize ke ukuran pas (boleh kamu atur sendiri, misalnya 25 x 50)
new_width = 50
new_height = 50
img_resized = img.resize((new_width, new_height), Image.NEAREST)
img_resized.save(resized_path)

print(f"[OK] Gambar berhasil di-resize jadi {new_width}x{new_height} -> {resized_path}")

# --- Step 2: Convert ke .ansi pakai px2ansi ---
try:
    subprocess.run(
        ["px2ansi", resized_path, "-o", output_path],
        check=True,
        shell=True,
    )
    print(f"[OK] Konversi berhasil! File disimpan di: {output_path}")
except subprocess.CalledProcessError as e:
    print("[ERROR] Gagal menjalankan px2ansi:", e)
except FileNotFoundError:
    print("[ERROR] px2ansi tidak ditemukan, pastikan sudah install: pip install px2ansi")
