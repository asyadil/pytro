import subprocess

input_path = r"C:\fastfetch-windows-amd64\hoshino_logo.png"
output_path = r"C:\fastfetch-windows-amd64\hoshino_logo.ansi"

# jalankan px2ansi tapi outputnya ditangkap di Python
result = subprocess.run(
    ["px2ansi", input_path],
    capture_output=True,
    text=True,
    encoding="utf-8"
)

# tulis hasil ke file dengan encoding utf-8
with open(output_path, "w", encoding="utf-8", errors="ignore") as f:
    f.write(result.stdout)

print("✅ ANSI file berhasil dibuat:", output_path)
