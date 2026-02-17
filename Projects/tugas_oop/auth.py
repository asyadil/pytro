
import json
from typing import Dict, Any, Optional

database_json: str = "tugas_oop/accounts_database.json"

class Login:
    @staticmethod
    def login() -> Optional[str]:
        while True:
            username: str = input("Please type your username\n> ")
            password: str = input("Please type your password\n> ")

            # semua file load gak pake error handling soalnya dipastikan file nya aman
            with open(database_json, 'r') as file:
                data: Dict[str, Dict[str, Any]] = json.load(file)
            if username in data:
                if data[username]["password"] == password:
                    print("Login success")
                    username = username
                    return username
                else:
                    print("Password is incorrect")
                    return None
            else:
                print("The account isnt found")
                return None

class Signup:
    @staticmethod
    def signup():
        username: str = input("Please type the username\n> ")
        password: str = input("Please type the password\n> ")
        rewrited_password: str = input("Please retype the password\n> ")

        if rewrited_password != password:
            print("Please type same as you typed")
            return False
        else:
            with open(database_json, 'r') as file:
                data: Dict[str, Dict[str, Any]] = json.load(file)

            if username in data:
                print("this username is taken, use another username")
                return False
            else:
                data[username] = {
                    "password": password,
                    "balance": 0
                }

                with open(database_json, 'w') as file:
                    json.dump(data, file, indent=4)

                print(f"Your account is successfully created")
        return username
