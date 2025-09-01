name = input("Let me know your name! ")

tier = "SSR"
role = "Diplomaticly"
ability = 99999
agility = 99999
weakness = 0.0000
defeatable = False

if name == "Asyadil Ali":
    print(f"Nama: {name}\n"
          f"Tier: {tier}\n"
          f"Role: {role}\n"
          f"Ability: {ability}\n"
          f"Agility: {agility}\n"
          f"Weakness: {weakness}")
    if not defeatable:
        print("Defeatable: No")
    else:
        print("Defeatable: Yes")
    print("You have reached maximum level, congrats!")
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
          f"Defeatable: Yes")

    user_input = input("Do you want us to buff up your level? Just type 'yes'! ")
    if user_input.lower() == "yes":
        try:
            level_up_input = int(input("Type how much you want us to increase your level: "))
            ability += level_up_input
            agility += level_up_input
            weakness -= level_up_input
            print(f"Your level has been buffed!\n"
                  f"Nama: {name}\n"
                  f"Tier: Rare\n"
                  f"Role: Aerial\n"
                  f"Ability: {ability}\n"
                  f"Agility: {agility}\n"
                  f"Weakness: {weakness}\n"
                  f"Defeatable: Yes")
        except ValueError:
            print("Please enter a valid number to increase your level.")
    else:
        print("Ok, no problem")
