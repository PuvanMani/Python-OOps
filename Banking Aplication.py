from random import randint
while True:
    print("\n***********************************************************")
    print("*                                                         *")
    print("*                  WELCOME TO PUVAN BANK                  *")
    print("*                                                         *")
    print("***********************************************************")
    print("*                                                         *")
    print("*               => 1) Create a New Account                *")
    print("*                                                         *")
    print("*               => 2) Deposite Money                      *")
    print("*                                                         *")
    print("*               => 3) Check Balance                       *")
    print("*                                                         *")
    print("*               => 4) WithDraw Money                      *")
    print("*                                                         *")
    print("*               => 5) Exit                                *")
    print("*                                                         *")
    print("***********************************************************")
    try:
        select=input("\nSelect Your Choice From the above Menu :")
    except :
        print("Enter Valid Number ")

    class Banking_App():
        def __init__(self,name,pin,account_no):
            self.name=name
            self.pin=pin
            self.account_no=account_no
            self.balance=0
        def create(self):
            print("Your Name is           :",self.name)
            print("Your Pin is            :",self.pin)
            print("\nYour Account Number is :",self.account_no)
        def deposite_money(self):
            if self.account_no==int(input("Enter Account Number  :")):
                if self.pin==int(input("Enter Pin Number  :")):
                    deposite_amount=int(input("Enter Deposite Money :"))
                    self.balance += deposite_amount
                    print("\nAmount Deposited:",deposite_amount)
                else:
                    print("Enter Valid Pin Number !!")
                    self.deposite_money()
            else:
                print("Enter Valid Account Number !!")
                self.deposite_money()
                
        def withdraw_money(self):
            if self.account_no==int(input("Enter Account Number  :")):
                if self.pin==int(input("Enter Pin Number  :")):
                    withdraw_amonut=int(input("Enter Withdraw Money :"))
                    if self.balance >= withdraw_amonut:
                        self.balance-=withdraw_amonut
                        print("\nYou Have Withdraw :",withdraw_amonut)
                    else:
                        print("Account Balance is Low !!")
                        
                else:
                    print("Enter Valid Pin Number !!")
                    self.withdraw_money()
            else:
                print("Enter Valid Account Number !!")
                self.withdraw_money()
                
        def check_balance(self):
            if self.account_no==int(input("Enter Account Number  :")):
                if self.pin==int(input("Enter Pin Number  :")):
                    print("\nYour Account Balance is   :",self.balance)
                else:
                    print("Enter Valid Pin Number !!")
                    self.check_balance()
            else:
                print("Enter Valid Account Number !!")
                self.check_balance()
            



    try:
        if select=='1':
            name=input("Enter Your Name Here      :")
            pin=int(input("Create Your Pin Here   :"))
            account_no=randint(29999,999999)
            obj = Banking_App(name,pin,account_no)
            obj.create()
        elif select=='2':
            obj.deposite_money()
        elif select=='3':
            obj.check_balance()
        elif select=='4':
            obj.withdraw_money()   
        elif select=='5':
            print("Sucessfully Exited...!!")
            break
        else:
            print("You Enter a Wrong Choice...")

    except:
        print("\nYou Didn't Have an Account. Create Account Press 1 ")
        
                
        
        
        























    
