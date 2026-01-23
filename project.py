import pickle
from account import Account
class Bank:
    # Defined simple attributes for my bank class
    def __init__(self,account):
        self.account = account




    def create_account(self):
                # name
                name = self.account.get_name()
                print("Let's move on to the next step: ",name)


                # address
                address = self.account.validate_address()
                print("Let's move on to the next step: ",address)

                # ph number
                ph_number = self.account.validate_ph()
                print("Let's move on to the next step: ",ph_number)
                

                # account type
                account_type = self.account.account_type()
                print("Let's move on to the next step: ",account_type)


                # pin creation
                pin = self.account.create_pin()
                print("Lets move on to the next step: ",pin)
                
                
                # Writing everything on a file
                account_info = {"name": name ,
                                "address": address,
                                "ph_number": ph_number,
                                "account_type" : account_type,
                                 "pin" : pin}
                
                with open("account.txt","wb") as f:
                    pickle.dump(account_info,f)
                

    def menu(self):
        print(
        """
           1).Change pin
           2).Create Account
           3).Deposit
           4).Withdraw
           5).Check Balance
           6).Return
           """ 
            )
        Task = int(input("Enter the task you want to perform: "))

        if Task == 1:
            try:
               old_pin = int(input("Enter your pin: "))
               if old_pin == self.account.get_pin():
                   new_pin = int(input("Enter a new pin: "))
                   print(self.account.set_pin(new_pin))

               else:
                   print("incorrect pin ")
               
            except ValueError as e:
                print(e)
                  
            
        elif Task == 2:
           self.create_account()
             


        # Withdraw money
        elif Task == 3:
            withdraw_money = self.account.withdraw_money()
            print("Your new balance is ",withdraw_money)

        # deposit money
        elif Task == 4:
            deposit_money = self.account.deposit_money()
            print("Your new balance is",deposit_money)
        
        # check_balance
        elif Task == 5:
            check_balance = self.account.check_balance()
            print("Your current balance is ",check_balance)


        elif Task == 6:
            exit()
        else:
            print("Invalid choice")
  

   



 

acc1 = Account("Nirab", 12345, 500, 1234)
b1 = Bank(acc1)
b1.menu()




    
    