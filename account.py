import requests

class Account:

    def __init__(self, acc_num, acc_bal, pin):
        self.__acc_num = acc_num
        self.__acc_bal = acc_bal
        self.__pin = pin

    # ---------- PIN ----------
    def get_pin(self):
        return self.__pin

    def set_pin(self, new_pin):
        if not isinstance(new_pin, int) or len(str(new_pin)) != 4:
            raise ValueError("New pin must be exactly 4 digits")
        self.__pin = new_pin
        return "Pin changed successfully"

    def validate_pin(self):
        while True:
            try:
                entered_pin = int(input("Enter your pin: "))
                if entered_pin == self.__pin:
                    return True
                else:
                    print("Incorrect pin")
            except ValueError:
                print("Pin must be numeric")

    # ---------- BALANCE ----------
    def get_balance(self):
        return self.__acc_bal

    def deposit_money(self):
        while True:
            try:
                amount = int(input("Enter amount to deposit: "))
                if amount <= 0:
                    print("Amount must be positive")
                else:
                    self.__acc_bal += amount
                    return self.__acc_bal
            except ValueError:
                print("Enter a numeric amount")

    def withdraw_money(self):
        while True:
            try:
                amount = int(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Amount must be positive")
                elif amount > self.__acc_bal:
                    print("Insufficient balance")
                else:
                    self.__acc_bal -= amount
                    return self.__acc_bal
            except ValueError:
                print("Enter a numeric amount")

    # ---------- USER INFO ----------
    def get_name(self):
        while True:
            name = input("Enter your full name: ").strip()
            if name.replace(" ", "").isalpha() and len(name.split()) >= 2:
                return name
            else:
                print("Enter a valid full name")

    def validate_phone(self):
        while True:
            ph = input("Enter phone number: ").strip()
            if ph.isdigit() and len(ph) == 10:
                return ph
            else:
                print("Enter a valid 10-digit phone number")

    def validate_ph(self):
        return self.validate_phone()

    def validate_address(self):
        while True:
            house = input("Enter house number: ").strip()
            street = input("Enter street name: ").strip()
            full_address = f"{house} {street}"

            url = "https://nominatim.openstreetmap.org/search"
            params = {"q": full_address, "format": "json"}
            headers = {"User-Agent": "BankApp/1.0"}

            response = requests.get(url, params=params, headers=headers)
            data = response.json()

            if data:
                return data
            else:
                print("Address not found. Try again.")

    def account_type(self):
        while True:
            print("""
1 - Checking Account
2 - Savings Account
""")
            try:
                choice = int(input("Choose: "))
                if choice == 1:
                    return "Checking"
                elif choice == 2:
                    return "Savings"
                else:
                    print("Choose 1 or 2")
            except ValueError:
                print("Enter a number")

    def create_pin(self):
        while True:
            try:
                pin = int(input("Enter a 4-digit pin: "))
                if len(str(pin)) == 4:
                    return pin
                else:
                    print("Pin must be 4 digits")
            except ValueError:
                print("Pin must be numeric")

        




 
