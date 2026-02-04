import pickle
from account import Account

class Bank:

    def __init__(self, account):
        self.account = account

    def create_account(self):
        name = self.account.get_name()
        address = self.account.validate_address()
        ph_number = self.account.validate_ph()
        account_type = self.account.account_type()
        pin = self.account.create_pin()

        account_info = {
            "name": name,
            "address": address,
            "ph_number": ph_number,
            "account_type": account_type,
            "pin": pin,
            "balance": 0
        }

        with open("account.pkl", "wb") as f:
            pickle.dump(account_info, f)

        print(" Account created and saved")

    def load_account(self):
        try:
            with open("account.pkl", "rb") as f:
                data = pickle.load(f)

            self.account = Account(
                data["name"],
                data["balance"],
                data["pin"]
            )
            print("Account loaded")
            return True

        except FileNotFoundError:
            print("No account found")
            return False

    def menu(self):
        while True:
            print("""
1. Create Account
2. Login
3. Deposit
4. Withdraw
5. Check Balance
6. Change Pin
7. Exit
""")

            choice = input("Choose: ")

            if choice == "1":
                self.create_account()

            elif choice == "2":
                if self.load_account():
                    pin = int(input("Enter pin: "))
                    if pin == self.account.get_pin():
                        print("Login successful")
                    else:
                        print(" Wrong pin")

            
            elif choice == "3":
                 if self.load_account():
                    print("Balance:", self.account.deposit_money())
                 else:
                        print("Please login first")


            elif choice == "4":
               if self.load_account():
                 print("Balance:", self.account.withdraw_money())
               else:
                   print("Please login first")


            elif choice == "5":
               if self.load_account():
                 print("Balance:", self.account.get_balance())
               else:
                   print(" Please login first")


            elif choice == "6":
                new_pin = int(input("New pin: "))
                print(self.account.set_pin(new_pin))

                with open("account.pkl", "wb") as f:
                    pickle.dump({
                        "name": self.account.name,
                        "balance": self.account.get_balance(),
                        "pin": new_pin
                    }, f)

            elif choice == "7":
                break

  

   



 
 



    
    