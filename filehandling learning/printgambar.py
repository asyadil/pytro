from rich.console import Console
from bs4 import BeautifulSoup

console = Console()

# pastikan path ditulis raw string biar aman di Windows
with open(r"C:\Users\ASUS\Desktop\py\filehandling\hutao.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# cari blok utama (biasanya ada <pre> kalau ASCII art warna)
block = soup.find("pre")
if not block:
    block = soup  # fallback kalau ga ada <pre>

# loop semua elemen span dan br
for element in block.find_all(["span", "br"]):
    if element.name == "br":
        console.print()  # baris baru
        continue

    style = element.get("style", "")
    text = element.text if element.text.strip() else " "
    
    if "rgb" in style:
        color = style.split("rgb(")[1].spli
