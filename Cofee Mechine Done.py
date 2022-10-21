class Cofee_Mechine:
    def __init__(self):
        print("\n\n                 ♥ WELCOME TO PM COFEE SHOP ♥     \n")
        self.water=3000
        self.milk=2000
        self.cofeepowder=500
        self.teapowder=500
        self.sugar=3000
        self.profit=0
        
    def cofee(self):
        print("\n              Cofee Price 15              ")
        print("\n  Available Quantity in Mechine  ")
        print("************************************")
        print("Water is           :",self.water,"ml")
        print("Milk is            :",self.milk,"ml")
        print("Cofee Powder is    :",self.cofeepowder,"g")
        print("Cofee Powder is    :",self.teapowder,"g")
        print("Sugar is           :",self.sugar,"g")
        amount=int(input("\nPay The Amount Here :"))
        if amount>=15:
            water = int(input("Enter the Quantity of Need Water :"))
            milk = int(input("Enter the Quantity of Need Milk :"))
            cofeepowder = int(input("Enter the Quantity of Need Cofee Powder :"))
            sugar = int(input("Enter the Quantity of Need sugar :"))
            if amount>15:
                print("\nRefund Amoun is",amount-15)
            report=input("\nDo You Want Report Type Y. If No Type N :").upper()
            if report =='Y':
                print("\nWater Added",water,"ml")
                print("Milk Added",milk,"ml")
                print("Cofee Powder Added",cofeepowder,"g")
        else:
            print(f"\nCofee Price is 10 but You Pay {amount}. Pay The Correct Amount")
        self.water -= water
        self.milk -= milk
        self.cofeepowder-=cofeepowder
        self.profit += 15
        self.sugar -= sugar
    def tea(self):
        print("\n              Tea Price 10              ")
        print("\n  Available Quantity in Mechine  ")
        print("************************************")
        print("Water is           :",self.water,"ml")
        print("Milk is            :",self.milk,"ml")
        print("Tea Powder is      :",self.teapowder,"g")
        print("Sugar is           :",self.sugar,"g")
        amount=int(input("\nPay The Amount Here :"))
        if amount>=10:
            water = int(input("Enter the Quantity of Need Water :"))
            milk = int(input("Enter the Quantity of Need Milk :"))
            teapowder = int(input("Enter the Quantity of Need Tea Powder :"))
            sugar = int(input("Enter the Quantity of Need sugar :"))
            if amount>10:
                print("\nRefund Amoun is",amount-10)
            report=input("\nDo You Want Report Type Y. If No Type N :").upper()
            if report =='Y':
                print("\nWater Added",water,"ml")
                print("Milk Added",milk,"ml")
                print("Tea Powder Added",teapowder,"g")
        else:
            print(f"\nTea Price is 10 but You Pay {amount}. Pay The Correct Amount")
        self.water -= water
        self.milk -= milk
        self.teapowder-=teapowder
        self.profit += 10
        self.sugar -= sugar
    def puremilk(self):
        print("\n              Milk Price 10              ")
        print("\n  Available Quantity in Mechine  ")
        print("************************************")
        print("Water is           :",self.water,"ml")
        print("Milk is            :",self.milk,"ml")
        print("Sugar is           :",self.sugar,"g")
        amount=int(input("\nPay The Amount Here :"))
        if amount>=10:
            water = int(input("Enter the Quantity of Need Water :"))
            milk = int(input("Enter the Quantity of Need Milk :"))
            sugar = int(input("Enter the Quantity of Need sugar :"))
            self.water -= water
            self.milk -= milk
            self.profit += amount
            if amount>10:
                print("\nRefund Amoun is",amount-10)
            report=input("\nDo You Want Report Type Y. If No Type N :").upper()
            if report =='Y':
                print("\nWater Added",water,"ml")
                print("Milk Added",milk,"ml")
        else:
            print(f"\nMilk Price is 10 but You Pay {amount}. Pay The Correct Amount")
        self.water -= water
        self.milk -= milk
        self.profit += 10
        self.sugar -= sugar
    def blacktea(self):
        print("\n              Black Tea Price 5              ")
        print("\n  Available Quantity in Mechine  ")
        print("************************************")
        print("Water is           :",self.water,"ml")
        print("TeaPowder is       :",self.teapowder,"g")
        print("Sugar is           :",self.sugar,"g")
        amount=int(input("\nPay The Amount Here :"))
        if amount>=5:
            water = int(input("Enter the Quantity of Need Water :"))
            teapowder = int(input("Enter the Quantity of Need Tea Powder :"))
            sugar = int(input("Enter the Quantity of Need sugar :"))
            self.water -= water
            self.teapowder-=teapowder
            self.profit += amount
            if amount>5:
                print("\nRefund Amoun is",amount-5)
            report=input("\nDo You Want Report Type Y. If No Type N :").upper()
            if report =='Y':
                print("\nWater Added",water,"ml")
                print("Tea Powder Added",teapowder,"g")

        else:
            print(f"\nBlack Tea Price is 5 but You Pay {amount}. Pay The Correct Amount")
        self.water -= water
        self.teapowder-=teapowder
        self.profit += 5
        self.sugar -= sugar
    def all_profit(self):
        print("Total Profit is :",self.profit)
obj=Cofee_Mechine()
while True:
    print("***********************************************************")
    print("*                                                         *")
    print("*               => 1) Cofee                               *")
    print("*                                                         *")
    print("*               => 2) Tea                                 *")
    print("*                                                         *")
    print("*               => 3) Milk                                *")
    print("*                                                         *")
    print("*               => 4) Black Tea                           *")
    print("*                                                         *")
    print("*               => 5) Off                                 *")
    print("*                                                         *")
    print("***********************************************************")
    try:
        select=int(input("\nSelect Your Choice From the above Menu :"))
    except :
        print("Enter Valid Number ")

    try:
        if select==1:
            obj.cofee()
        elif select==2:
            obj.tea()
        elif select==3:
            obj.puremilk()
        elif select==4:
            obj.blacktea()   
        elif select==5:
            print("Cofee Mechine Was Off...!!")
            obj.all_profit()
            break
        else:
            print("You Enter a Wrong Choice...")
    except Exception as a:
        print(a)
