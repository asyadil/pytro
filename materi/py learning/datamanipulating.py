datalist = ["Asyadil", "Ali", "Ramdani"]
datalist.remove("Ramdani")
print(datalist)
datalist.insert(0, "Sang")
indexes = [0, 2]
print(
    "Sambutlah kedatangan Raja baru!\n",
    [datalist[i] for i in indexes]
    )

print(
    "Sambutlah kedatangan Raja baru!\n",
    datalist[0], datalist[1]
    )

print(
    f"Sambutlah kedatangan Raja baru!\n"
    f"'{datalist[1:3]}' "
    )

atributes = ("Asyadil Ali The Fuhrer"), ("Atributes:"), ("Rank: SSR"), ("Role: All"), ("Element: Necro & Darkness")
print(atributes)

name, header, rank, role, elementtype = atributes

print(
    f"_______________________"
    f"\n\n{name}\n"
    f"\n{header}\n"
    f"  {rank}\n"
    f"  {role}\n"
    f"  {elementtype}\n" 
    f"_______________________"   
)

wihle = True
print("\n" * 10)
name = ("asyadil", "ali", "ramdani")
print("Masukan nama mu, Ali")
nama = input().islower
if nama in name:
    print("bagus!") 
else:
    print("!?!?!?")
print("\n" * 10)





huruf_ali = ["a","s","y","a","d","i","l"]
print(for i in huruf_ali)

huruf_ali.insert(0, "A")
huruf_ali.insert(1, "l")
huruf_ali.insert(2, "i")