from entities.account import account
from entities.bank import bank
from entities.user import user
from entities.errors import *

clients = []
users = []
egn = []
accounts = []
currency = [BGN, EUR, USD, JPY]
acc_type = [CURRENT, SAVING, CREDIT]
class Menu:
    def print_menu(self):
        print(" - - - - MENU - - - - - -")
        print("1. Create user.")
        print("2. Create account for users.")
        print("3. List users.")
        print("4. List account for users.")
        print("5. Deposit for user account.")
        print("6. Withdraw for user account.")
        print("7. Exit.")

    def create_user(self):
        egn = input("Enter user EGN: ")
        name = input("Enternter users names: ")
        user = user(egn, name)
        self.bank.user.append(user)     

    def create_acc_for_users(self):
        egn = input('Please enter user EGN')
        for i in self.bank.user:
            if i.egn == egn:
                balance = float(input("Please enter balance"))
                currency = float(input('Please enter currency'))
                type_account = float(input('Please enter account type'))
                acc = account(balance, currency, type_account)
                i.account.append(acc)
                return
            raise InvalidUser("User not found!")

    def list_users(self, users):
        for y in self.bank.user:
            print(y)

    def list_acc_for_users(self, accounts):
        egn = input("Enter user's EGN: ")
        for z in self.bank.user:
            if z.egn == egn:
                for h in z.accounts:
                    print(h)
                return
            raise InvalidUser("User not found!")

    def deposit_for_user_acc(self):
        egn = input("Enter user's  EGN: ")
        iban = input("Enter user account IBAN -> 'BG9812..........': ")
        amount = float(input("Enter a money you want to deposit: "))
        for m in self.bank.user:
            if m.egn == egn:
                for f in x.accounts:
                    if f.IBAN == iban:
                        f.balance += amount
                        return
                    raise Exception('This account doesnt exist')
                return
            raise InvalidUser("User not found!")

    def withdraw_for_user_acc(self):
        egn = input("Enter user's  EGN: ")
        iban = input("Enter user account IBAN -> 'BG9812..........': ")
        money = float(input("Enter a money you want to withdraw"))
        for k in self.bank.users:
            if k.egn == egn:
                for g in k.accounts:
                    if g.IBAN == iban:
                        if money > g.balance:
                            raise EmptyBank("Your account is empty.")
                        g.balance -= money

    def run(self):
        while True:
            Menu.print_menu(self)   

            choice = input("Choose an item from the menu: ")
           
            try:               
                menu_func(choice)
            except Exception as ex:
                print(f"Error: {str(ex)}")

    def main_func(self, choice: int):
        if choice == "1":
            self.create_user()
                                        
        elif choice == "2":
            self.create_acc_for_users()

        elif choice == "3":
            self.list_users()

        elif choice == "4":
            self.list_acc_for_users()

        elif choice == "5":
            self.deposit_for_user_acc() 
                    
        elif choice == "6":
            self.withdraw_for_user_acc()

        elif choice == "7":
            print("Goodbye!")
        else:
            raise InvalidCommand("Invalid choice!")

        print()

if __name__ == '__main__':
    menu = Menu()
    menu.run()
    print()

#poluchi se golqma kasha. pone se opitah.