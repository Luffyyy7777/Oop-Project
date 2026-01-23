import requests
import pickle
class Account:
# all the private and public attributes are defined in here 
    def __init__(self,acc_num,acc_bal,pin):
        self.__acc_num = acc_num
        self.__acc_bal = acc_bal
        self.__pin = pin
    
    def get_pin(self):
        return self.__pin
    
    def set_pin(self,new_pin):
        if not isinstance(new_pin,int) or len(str(new_pin)) !=4:
            raise ValueError("New pin must be 4 digit")
        
        self.__pin = new_pin
        return "Pin changed succesfully"
    
    def get_balance(self):
        return self.__acc_bal



# Validating pin 

    def validate_pin(self):
       while True:
         try:
               Your_pin = int(input("Enter your pin: "))
               if Your_pin == info["pin"]:
                    print("Move ahead with your task")
                    return True
                    
               else:
                     print("Enter a valid pin number")
                   
         except ValueError:
             print("Enter a numeric pin ")


    # ph number validation   
    def validate_phone(self):
       while True:
            ph_number = int(input("Enter a ph number: "))
            
            if not ph_number.isdigit():
                print("Please enter a valid phone number.")
                continue  

            if len(ph_number) != 10:
                print("Pleae enter a valid phone number:")
                continue


            return ph_number


 


# I am gonna define all the function in here
    def get_name(self):
     while True:
         name = input("Enter your full name: ").strip()
         if name.replace(" ","").isalpha() and len(name.split()) >= 2:
                  print("We can move on to the next step")
                  return name
         else:
             print("Enter your valid full name.")
         



# Address

    def validate_address(self):
     while True:
        house = input("Enter house number: ").strip()
        street = input("Enter street name: ").strip()

        full_address = f"{house} {street}"

        url = "https://nominatim.openstreetmap.org/search"

        params = {
            "q": full_address,
            "format": "json"
        }

        headers = {
            "User-Agent": "BankApp/1.0"
        }

        response = requests.get(url, params=params, headers=headers)

        data = response.json()

        if len(data) > 0:
            print(" Address is valid. Let's move on to the next step.")
            return data
        else:
            print(" Address not found. Please enter a valid address.")



 # ph number
    def validate_ph(self):
            ph_number = validate_phone()

            print("Let's move on the next step")
            return ph_number
        



# Account type 
    def account_type(self):
        print(""" Choose option 1 or 2 
              1 - Checking account 
              2 - Savings Account
              """)
        accounts = int(input("Enter the account type you want to create: "))
        match accounts:
            case 1:
                print("You successfully create a checkings account")
                return "Checking"

            case 2:
                print("You successfully create a savings Account.")
                return "Savings"
            case _:
                  print("Please choose between these two.")



# Create pin 
    def create_pin(self):
        while True:
            pin = int(input("Enter your 4 digit pin: "))
            if not isinstance(pin,int) or len(str(pin)) !=4:
                    raise ValueError("New pin must be 4 digit")
            
            else:
                return pin


#  Withdraw function
    def withdraw_money(self):
       
       if self.validate_pin() == True and self.validate_phone() == info["ph_number"]:
            amount = int(input("Enter the balance you want to withdraw: "))
            if (self.get_balance() > amount):
                 self.__acc_bal-= amount
                 print("Your money was successfully withdrawn",amount)
                 return self.__acc_bal

       else:
            print("Enter a valid amount you want to withdraw")



#  deposit mone
    def deposit_money(self):
       if self.validate_pin() == True and self.validate_phone() == info["ph_number"]:
            amount = int(input("Enter the balance you want to deposit: "))
            if (self.__acc_bal > amount):
                 self.__acc_bal += amount
                 print("Your money was successfully deposited",amount)
                 return self.__acc_bal

       else:
            print("Enter a valid amount you want to withdraw")



# check_balance

    def check_balance(self):
        if self.validate_pin() == True and self.validate_phone() == info["ph_number"]:
             return self.get_balance()
        




#  Reading file
def read_file():
    with open("account.pkl","rb") as g:
        return pickle.load(g)


info = read_file()

# Taking input
