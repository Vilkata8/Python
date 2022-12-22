from entities import account, bank, user
from errors import *
import random
l_1 = []
clients = []
users = []
egn = []
accounts = []
currency = [BGN, EUR, USD, JPY]
acc_type = [CURRENT, SAVING, CREDIT]
class Menu:
    def print_menu(self):
        print("1. Create user.")
        print("2. Create account for users.")
        print("3. List users.")
        print("4. List account for users.")
        print("5. Deposit for user account.")
        print("6. Withdrawal for user account.")
        print("7. Exit.")

    def create_user(self, name, l_name):
        return name, l_name

    def create_acc_for_users(self, username):
        return username

    def list_users(self, users):
        return users

    def list_acc_for_users(self, accounts):
        return accounts

    def deposit_for_user_acc(self):
        pass

    def withdrawal_for_user_acc(self):
        pass

    def run(self):
        while True:
            Menu.print_menu(self)   

            choice = input("Choose an item from the menu: ")

            try:

                if choice == "1":
                    
                    for i in range(10):
                        n = random.randint(1, 10)
                        l_1.append(n)
                    print("IBAN is: BG9812{l_1}")   
                    
                    
                    username = input("Enter username: (alpha-numeric): ")
                    if username in users:
                        raise UserAlreadyExists("This username isn't available!")

                    EGN = input("Enter your EGN: ")
                    if len(EGN) > 10:
                        raise InvalidDataFormat("Enter 10 number symbols.")
                    elif EGN != "str":
                        raise InvalidDataFormat("Invalid EGN!")
                    elif EGN in egn :
                        raise UserAlreadyExists("This EGN isn't available!")
                    else:
                        EGN.append(egn)
                        
                    accounts = input("Enter account type: (CURRENT, SAVINGS, CREDIT): ")
                    if accounts != "CURRENT" or != "SAVINGS" or != "CREDIT":
                        raise InvalidDataFormat("Try to input again account type!")

                    users.append(username)
                    char = self.(name)
                    .append(char)
                    print(char)
                    continue

                elif choice == "2":
                    acc = input("Enter account for users: (alpha-numeric): ")
                    if acc in accounts:
                        raise UserAlreadyExists("Account is already exist!")                       
                        continue

                elif choice == "3":
                    print("The list of users is:", users[])
                    continue

                elif choice == "4":
                    print(f"Account for users:", accounts[])
                    continue

                elif choice == "5":
                    
                    print(f"Deposit for user account!")
                    continue

                elif choice == "6":

                    print('Withdrawal for user account!')
                    break

                elif choice == "7":
                    print("Goodbye!")
                else:
                    raise InvalidCommand("Invalid choice!")

            except Exception as ex:
                print(f"Error: {str(ex)}")
            print()

if __name__ == '__main__':
    menu = Menu()
    menu.run()
    print()