import os
os.system('cls' if os.name == 'nt' else 'clear')
from colorama import init, Fore, Back, Style
init()

def main():
    ranking = {
        "rangking_kelas_A":{
            "Ali":"4",
            "Raihan":"1",
            "Hanif":"3",
            "Hafidz":"2"
        },
        "rangking_kelas_B":{
            "Dzikrul Hanif":"1",
            "Mikhail":"2",
            "Fardhan":"3"
        }
    }
    print(f"\nRanking kelas A: {ranking['rangking_kelas_A']}"
          f"\nRanking kelas B: {ranking['rangking_kelas_B']}"
        "\n_________________________________________________"
        )
    
    print("\nKelas A:"
          f"\n{Fore.YELLOW}Ali dapet ranking: {ranking["rangking_kelas_A"]["Ali"]}"
          f"\n{Fore.MAGENTA}Raihan pasti dapet ranking: {ranking["rangking_kelas_A"]["Raihan"]}"
          f"\n{Fore.RED}Hanif dapet ranking: {ranking["rangking_kelas_A"]["Hanif"]}"
          f"\n{Fore.GREEN}Hafidz dapet ranking: {ranking["rangking_kelas_A"]["Hafidz"]}"
        f"{Fore.RESET}\n_________________________________________________")
    
    print("\nKelas B: 'gak diajak'\n_________________________________________________")
    
    impian_ali = input("Ali pengen dapet ranking berapa, sih, sebenernya?\n")
    ranking["rangking_kelas_A"]["Ali",{impian_ali}]
    print(F"Sekarang Ali ranking {ranking["rangking_kelas_A"]["Ali",{impian_ali}]}")

main()