from email.mime import message
from auth import Signup, Login as auth
from main_menu import Main_menu as menu
from datetime import datetime

def main_menu():
        print("<== [ Main menu ] ==>\n"
            "1.Balance cheking\n"
            "2.Deposit\n"
            "3.Withdraw\n"
            "4.Exit")
        menu_choice = input("Input the number\n> ")
        return menu_choice

def log(message: str) -> None:
    with open("tugas_anjay/log.txt", "a") as file:
        file.write(message)

def main():
    print("Wellcome to our mini simplefied bank")
    input("Press enter to continue...")
    while True:
        have_an_account = input("Do you have an account\ntype Y/n\n").strip().lower()
        if have_an_account == "n":
            username = Signup.signup()
            if type(username) == str:
                log(f"[{datetime.now()}] A new account is created with username {username}\n")
            else:
                log(f"[{datetime.now()}] User trying for create an account but the operation is failed")
        elif have_an_account == "y":
            username = auth.login()
            if username:
                log(f"[{datetime.now()}] User {username} logged in\n")
                while True:
                    menu_choice = main_menu()
                    if not menu_choice.isdigit():
                        print("Please type the correct input")
                        continue
                    else:
                        menu_choice = int(menu_choice)
                        if menu_choice > 4 or menu_choice < 1:
                            print("Please input the correct number")
                            continue
                        else:
                            if menu_choice == 1:
                                menu.balance_chek(username=username)
                                log(f"[{datetime.now()}] User {username} checked their balance\n")
                            elif menu_choice == 2:
                                menu.deposit(username=username)
                                log(f"[{datetime.now()}] User {username} deposited money\n")
                            elif menu_choice == 3:
                                menu.withdraw(username=username)
                                log(f"[{datetime.now()}] User {username} withdrew money\n")
                            elif menu_choice == 4:
                                menu.get_out()
                                log(f"[{datetime.now()}] User {username} logged out\n")
                            else:
                                print("Please type the correct input")
                                continue
        else:
            print("Please type the correct input")
            continue
    
if __name__ == "__main__":
        main()