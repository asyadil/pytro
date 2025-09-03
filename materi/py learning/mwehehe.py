kabar = input("Halo bre, ape kabar?")
nama = input("Ok kalo boleh tau nih ya, nama ente siape?")

print(f"Ok, {nama}, kalo boleh tau elu, nih\n"
      f"lebih suka nonton anime, apa main game?")

pilihan1 = int(input("ketik '1' kalo elu wibu, kalo elu gamer ketik '2' ..."))
if pilihan1 == (1):
   print("widih... berarti kita satu suku bangsa coy...")
   wibu = input("kalo boleh tau, waifu ente siape")
   animemana = input("beuh, dari anime mana dia, tuh")
   print(f"keren lu {nama}, ok, jadi waifu lu {wibu} dari anime {animemana}, ya")
elif pilihan1 == (2):
   print("oh, elu lebih suka main game, ya.")
   game = input("kalo boleh tau main game ape, lu?")
   rank = input("wokeh... rank nya dah nyampe mane?")
   print(f"gile... pemain {game}... dah sampe rank {rank} pulak... gilee...")
else:
   print("masukinnya angka '1' kalo nggk '2', jangan yang lain, elah gimane sih, lu")


      