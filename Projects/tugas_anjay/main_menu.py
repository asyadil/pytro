import json

class Main_menu:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_out() -> None:
        exit()

    @staticmethod
    def balance_chek(username):
        with open("tugas_anjay/accounts_database.json", "r") as file:
            data = json.load(file)

        balance = data[username]["balance"]

        print(f"Your current balance is:\n> {balance}")
        return True
    
    @staticmethod
    def deposit(username):
        amount = int(input("Input the deposit amount\n> "))

        with open("tugas_anjay/accounts_database.json", "r") as file:
            data = json.load(file)
            data[username]["balance"] += amount
            with open("tugas_anjay/accounts_database.json", "w") as file:
                json.dump(data, file, indent=4)
        
        print(f"Deposit is done successfully\nYour current balance is: Rp.{data[username]["balance"]},-")
        return True
    
    @staticmethod
    def withdraw(username):
        amount = input("Input the withdraw amount\n> ")
        if not amount.isdigit():
            print("Please type the correct input")
            return False
        amount = int(amount)

        while True:
            with open("tugas_anjay/accounts_database.json", "r") as file:
                data = json.load(file)
                
                data[username]["balance"] = int(data[username]["balance"])
                
                current_balance = (data[username]["balance"])
                if current_balance >= amount:
                    data[username]["balance"] -= amount
                    with open("tugas_anjay/accounts_database.json", "w") as file:
                        json.dump(data, file, indent=4)
                    print(f"Withdraw success\nYour current balance is: Rp.{data[username]['balance']},-")
                    return True
                else:
                    print(f'The balance isnt enough\nYour current balance is: Rp.{data[username]["balance"]},-')
                    return False