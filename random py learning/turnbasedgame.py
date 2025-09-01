import os
os.system('cls' if os.name == 'nt' else 'clear')
import random

# Inisialisasi poin karakter
if milih_char == '1':  # Tank
    attack_point = 100
    defense_point = 100
elif milih_char == '2':  # Jet Tempur
    attack_point = 120
    defense_point = 80
elif milih_char == '3':  # Artileri
    attack_point = 80
    defense_point = 120

enemy_attack = 100
enemy_defense = 100
player_hp = 200
enemy_hp = 200

print("\n[GAME START]\n")
turn = 1
while player_hp > 0 and enemy_hp > 0:
    print(f"\n--- Turn {turn} ---")
    print(f"HP Anda: {player_hp} | HP Musuh: {enemy_hp}")
    print(f"Attack Point: {attack_point} | Defense Point: {defense_point}")

    action = input("Pilih aksi: [1] Serang [2] Bertahan : ")
    if action == '1':
        atk = int(input(f"Masukkan attack point yang ingin digunakan (1-{attack_point}): "))
        if atk < 1 or atk > attack_point:
            print("Input tidak valid.")
            continue
        enemy_hp -= atk
        print(f"Anda menyerang musuh dengan {atk} poin!")
    elif action == '2':
        dfn = int(input(f"Masukkan defense point yang ingin digunakan (1-{defense_point}): "))
        if dfn < 1 or dfn > defense_point:
            print("Input tidak valid.")
            continue
        print(f"Anda bertahan dengan {dfn} poin!")
    else:
        print("Input tidak valid.")
        continue

    # Giliran musuh (sederhana, random)
    enemy_action = random.choice(['attack', 'defend'])
    if enemy_action == 'attack':
        enemy_atk = random.randint(10, enemy_attack)
        player_hp -= enemy_atk
        print(f"Musuh menyerang Anda dengan {enemy_atk} poin!")
    else:
        enemy_def = random.randint(10, enemy_defense)
        print(f"Musuh bertahan dengan {enemy_def} poin!")

    turn += 1

if player_hp <= 0:
    print("\nAnda kalah! Game Over.")
elif enemy_hp <= 0:
    print("\nSelamat! Anda menang!")
