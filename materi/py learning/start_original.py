typing = input("Let me know youre name!")

name = typing
tier = "SSR"
role = "Diplomaticly"
ability = 99999
agility = 99999
weakness = 0.0000
defeatable = False

if (typing == "Asyadil Ali"):
    print(f"Nama: {name}\n"
        f"Tier: {tier}\n"
        f"Role: {role}\n"
        f"Ability: {ability}\n"
        f"Agility: {agility}\n"
        f"Weakness: {weakness}")
    if (defeatable == False):
        print("Defeatable: No")
    else:
        print("Defeatable: Yes")
    print("You have reach maximum level, congrats!")
else:
    ability2 = 20
    agility2 = 15
    weakness2 = 50
    print(f"Nama: {name}\n"
            f"Tier: No tier\n"
            f"Role: No role\n"
            f"Ability: {ability2}\n"
            f"Agility: {agility2}\n"
            f"Weakness: {weakness2}\n"
            f"Defeatabale: Yes")

    input2 =  input(f"Do you want we buff up your level?\n"
                f"just type 'yes'")
    if (input2.lower == "yes"):
        input3 = int(input("Type how much you want us increass youre level!"))
        ability2 += input3
        agility2 += input3
        weakness2 -= input3

        print(f"Nama: {name}\n"
            f"Tier: Rare\n"
            f"Role: Aerial\n"
            f"Ability: {ability2}\n"
            f"Agility: {agility2}\n"
            f"Weakness: {weakness2}\n"
            f"Defeatabale: Yes")
    elif (input2 == "no"):
        print("Ok, no problem")