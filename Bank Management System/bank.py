
class Bank:
    def __init__(self):
        self.client_details_list = []
        self.loggedin = False
        self.cash = 100
        self.TranferCash = False



    def register(self, name , ph , password):
        cash = self.cash
        contitions = True
        if len(str(ph)) > 10 or len(str(ph)) < 10:
            print("\nInvalid Phone number !!!!! \nPlease enter 10 digit number.\n")
            contitions = False

        if len(password) < 5 or len(password) > 18:
            print("\nEnter password greater than 5 and less than 18 character !!!\n")
            contitions = False  
        
        if contitions == True:
            print("\n*******      Account created successfully        *******\n")
            self.client_details_list = [name , ph , password , cash]
            with open(f"{name}.txt","w") as f:
                for details in self.client_details_list:
                    f.write(str(details)+"\n")



    def login(self, name , ph , password):
        with open(f"{name}.txt","r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(ph) in str(self.client_details_list):
                if str(password) in str(self.client_details_list):
                    self.loggedin = True

            if self.loggedin == True:
                print(f"\n*******       {name} logged in successfully       *******\n")
                self.cash = int(self.client_details_list[3])
                self.name = name
            
            else:
                print("\nWrong details !!!!!\n")
    


    def add_cash(self, amount):
        if amount > 0:
            self.cash += amount
            with open(f"{name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")
            
            with open(f"{name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[3]),str(self.cash)))

            print("\n*******        Amount added successfully       *******\n")

        else:
            print("\nEnter correct value of amount !!!!!\n")



    def withdraw_cash(self, amount):
        if amount > 0 and amount <= self.cash:
            self.cash -= amount
            with open(f"{name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")
            
            with open(f"{name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[3]),str(self.cash)))

            print("\n*******        Amount withdrew successfully       *******\n")

        else:
            print("\nYou don't have that much amount of money !!!!!\n")



    def Tranfer_cash(self, amount , name ,ph):
        with open(f"{name}.txt","r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(ph) in self.client_details_list:
                self.TranferCash = True


        if self.TranferCash == True:
            total_cash = int(self.client_details_list[3]) + amount
            left_cash = self.cash - amount
            with open(f"{name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[3]),str(total_cash)))

            with open(f"{self.name}.txt","r") as f:
                details_2 = f.read()
                self.client_details_list = details_2.split("\n")
            
            with open(f"{self.name}.txt","w") as f:
                f.write(details_2.replace(str(self.client_details_list[3]),str(left_cash)))

            print("\n*******        Amount Transfered Successfully to \"",name,"-",ph,"\"        *******\n")
            print("\nBalacne left =",left_cash, "\n")
            self.cash = left_cash
    


    def password_change(self, password):
        if len(password) < 5 or len(password) > 18:
            print("\nEnter password greater than 5 and less than 18 character !!!\n")
        else:
            with open(f"{self.name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{self.name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[2]),str(password)))
            print("\n*******        new Password set up successfully        *******\n")



    def ph_change(self , ph):
        if len(str(ph)) > 10 or len(str(ph)) < 10:
            print("\nInvalid Phone number !!!!! \nplease enter 10 digit number.\n")
        else:
            with open(f"{self.name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{self.name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[1]),str(ph)))
            print("\n*******        new Phone number set up successfully        *******\n")





if __name__ == "__main__":
    Bank_object = Bank()
    print("\n\n<<<<<<<<<<<<<<<<<      Welcome To my Bank Management System        >>>>>>>>>>>>>>>>>>>>\n")
    print("\n1. Login\n")
    print("2. Creata a new Account\n")
    user = int(input("Make decision: "))

    if user == 1:
        print("\nLogging in\n")
        name = input("Enter Name: ")
        ph = int(input("Enter Phone Number: "))
        password = input("Enter password: ")
        Bank_object.login(name, ph, password)
        while True:
            if Bank_object.loggedin:
                print("1. Add Amount")
                print("2. Check Balcane")
                print("3. Withdraw Cash")
                print("4. Tranfer Amount")
                print("5. Edit Profile")
                print("6. Logout\n")
                login_user = int(input())
                if login_user == 1:
                    print("Balance =",Bank_object.cash, "\n")
                    amount = int(input("Enter amount: "))
                    Bank_object.add_cash(amount)
                    print("\n1. Back to Menu")
                    print("2. Logout\n")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break
                

                elif login_user == 2:
                    print("Balacne =",Bank_object.cash, "\n")
                    print("\n1. Back to Menu")
                    print("2. Logout\n")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break


                elif login_user == 3:
                    print("Balance =",Bank_object.cash, "\n")
                    amount = int(input("Enter amount: "))
                    Bank_object.withdraw_cash(amount)
                    print("\n1. Back to Menu")
                    print("2. Logout\n")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break    


                elif login_user == 4:
                    print("Balance =",Bank_object.cash,"\n")
                    amount = int(input("Enter amount: "))
                    if amount >= 0 and amount <= Bank_object.cash:
                        name = input("Enter person name: ")
                        ph = input("Enter person phone number: ")
                        Bank_object.Tranfer_cash(amount,name,ph)
                        print("\n1. Back to Menu")
                        print("2. Logout\n")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif amount < 0 :
                        print("\nEnter please correct value of amount !!!!!\n")

                    elif amount > Bank_object.cash:
                        print("\nNot enough balance !!!!!\n")


                elif login_user == 5:
                    print("\n1. Password change")
                    print("2. Phone Number change\n")
                    edit_profile = int(input())
                    if edit_profile == 1:
                        new_passwrod = input("Enter new Password: ")
                        Bank_object.password_change(new_passwrod)
                        print("\n1. Back to Menu")
                        print("2. Logout\n")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif edit_profile == 2:
                        new_ph = int(input("Enter new Phone Number: "))
                        Bank_object.ph_change(new_ph)
                        print("\n1. Back to Menu")
                        print("2. Logout\n")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break


                elif login_user == 6:
                    break
                        

    elif user == 2:
        print("\nCreating a new  Account")
        name = input("Enter Name: ")
        ph = int(input("Enter Phone Number: "))
        password = input("Enter password: ")
        Bank_object.register(name, ph, password)
    

    else:
        print("\n\n>> >> You must select 1 or 2\n")
