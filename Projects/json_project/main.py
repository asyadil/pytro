import os
from static_json import main_a
from dynamic_json import main_b

def clr():
    import os; os.system('cls' if os.name == 'nt' else 'clear')


def main():
    main_a.main_a()
    main_b.main_b()

main()
clr()
input("yeaaay ...")