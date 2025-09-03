import os
os.system('cls' if os.name == 'nt' else 'clear')

print("=== Welcome to waifu_inputer ===")
list = []
jumlah = int(input("Masukan jumlah waifu yang ada didalam harem anda : "))

for i in range(0, jumlah):
    name = input("Masukan nama: ")
    list.append(name)

print("Ini dia mereka: ", list)
