accountDatabase = []

class Account:
    def __init__(self, accountNumber, name, idNumber, email,  phoneNumber, password, initialDeposit):
        self.accountNumber = accountNumber
        self.FirstName, self.MiddleInitial, self.Surname = name
        self.idNumber = idNumber
        self.email = email
        self.phoneNumber = phoneNumber
        self.password = password
        self.currentBalance = initialDeposit #Because at creation, your current balance is the one you started with

    def ShowAccountInformation(self):
        print("Account Info: \n")
        print(f"Account Name: {self.GetName()}")
        print(f"Account Number: {self.GetAccountNumber()}")
        print(f"National I.D: {self.GetIDNumber()}")
        print(f"Email: {self.GetEmail()}")
        print(f"Phone Number: {self.GetPhoneNumber()}")
        print(f"Password: {self.GetPassword()}")
        print(f"Account Balance: Php {self.GetCurrentBalance()}\n")

    def GetName(self):
        return " ".join(list((self.FirstName, self.MiddleInitial, self.Surname))) #returns string

    def GetIDNumber(self):
        return self.idNumber #returns string in the format 1234-1234-1234

    def GetEmail(self):
        return self.email

    def GetPhoneNumber(self):
        return self.phoneNumber

    def GetPassword(self):
        return self.password
    
    def GetAccountNumber(self):
        return self.accountNumber #Returns string

    def GetCurrentBalance(self):
        return self.currentBalance #Returns int

    def UpdateBalance(self, value):
        self.currentBalance = f"{float(self.currentBalance) +  value: .2f}" # For Subtraction, set value as negative ( -100 ) so that currentBalance += (-100)

    def UpdateName(self, name):
        self.FirstName, self.MiddleInitial, self.Surname = name

    def UpdateIDNumber(self, idNumber):
        self.idNumber = idNumber

    def UpdateEmail(self, email):
        self.email = email

    def UpdatePhoneNumber(self, PhoneNumber):
        self.phoneNumber = PhoneNumber

    def UpdatePassword(self, password):
        self.password = password

    def Withdraw(self, Amount):
        if float(Amount) <= float(self.GetCurrentBalance()):
            self.currentBalance = float(self.currentBalance) - float(Amount)

            self.currentBalance  = f"{float(self.currentBalance): .2f}"

            

            print(f"Withdrawal successful.. \nNew Balance: {self.GetCurrentBalance()} \n\n")
        else:
            print("Insufficient Funds.\n")


    def Deposit(self):
        while True:
            try:
                Amount = float(input("Enter the amount you want to deposit: "))

                if len(str(Amount).split(".")[-1]) >=3:
                    print("Invalid amount of decimal places. Please try again \n")
                elif Amount >= 0:

                    while True:
                        confirm = input(f"Are you sure you want to deposit{Amount: .2f}? Confirm Yes or No. ").lower()

                        if confirm == "yes" or confirm == "no":
                            break
                        else:
                            print("Invalid Input. Please try again. \n")
                    if confirm == "yes":
                        self.currentBalance = float(self.currentBalance) + Amount
                        self.currentBalance = f"{float(self.currentBalance): .2f}"
                        print("Deposit successful \n")
                        break
                    
                    
                    #self.transactions.append(f"Deposited: {Amount: .2f}")
                    # From Marc Daniel ung line of code above. Up to you @Lorenz on how to parse it

                else:
                    print("Invalid amount. Please enter a positive value")
            except ValueError:
                print("Invalid Input. Please enter a numerical value")


#Account Information Changes
def ChangeName(accountDatabase, accountIndex):
    print(f"Your current name is {accountDatabase[accountIndex].GetName()}\n")

    
   #Name
    while True:
        name = [input("Enter your new First Name: \n"),
                input("Enter your new Middle Initial: \n"),
                input("Enter your new Surname: \n")]

        if not all(((s.isalpha() or s == "." or s == " ") for s in names) and ((names.endswith(".") and names[:-1].isalpha()) if "." in names else all(word.isalpha() for word in names.split())) for names in name):
            print("You have entered an invalid name, Please try again.")
        else:
            while True:
                confirm = input(f"Your new name is {name[0]} {name[1]} {name[2]}. Confirm? Yes or No.\n Or enter exit to exit \n").lower()

                if confirm == "yes" or confirm == "no":
                    break
                else:
                    print("Invalid input, please try again.\n")
                    
            if confirm == "yes":
                if any((" ".join(name) == account.GetName() and not (accountIndex == accountDatabase.index(account) ) ) for account in accountDatabase):
                    print("There is already an existing account with the same name. Please try again. \n")
                else:
                    print("Confirming changes......\n")
                    accountDatabase[accountIndex].UpdateName(name)
                    break
            if confirm == "exit":
                break
        
def ChangeIDNumber(accountDatabase, accountIndex):
    print(f"Your current National I.D Number is {accountDatabase[accountIndex].GetIDNumber()}\n")

    while True:
        idNumber = input("Enter your new 12-digit National I.D No.: ")


        #Handles error for cases such as "123--123--1234", "123", "1234-1234-123-"
        if (not all((len(idNumber)== 14 or len(idNumber) == 12) and (s.isdigit() or s == " " or s == "-") for s in idNumber)) or ((len(idNumber) == 14) and  not all( (( (chunk[-1] == "-" or chunk[-1] == " ") and (all(digits.isdigit() for digits in chunk[:-1]) ) ) for chunk in [idNumber[i:i+5] for i in range(0, len(idNumber) + 1, 5)][:-1] ) ) or not all ((digits.isdigit() for digits in idNumber[10:14]) )
):
            print("Invalid Input, Please try again.\n")
        else:

            # Formats the variable into " 1234-1234-1234 " 
            if (len(idNumber) == 12 and (s.isdigit() for s in idNumber)):
                idNumber = "-".join(idNumber[i: i+4] for i in range(0, len(idNumber),4))   

            if (len(idNumber) == 14) and (idNumber[4] == " " or idNumber[4] == "-") or (idNumber[9] == " " or idNumber[9] == "-"):
                idNumber = idNumber[:4] + "-" + idNumber[5:]
                idNumber= idNumber[:9] + "-" + idNumber[10:]

            while True:
                confirm = input(f"Your new National I.D Number is {idNumber}. Confirm? Yes or No. Or enter exit to exit \n").lower()

                if confirm == "yes"  or confirm == "no" or confirm == "exit":
                    break
                else:
                    print("Invalid input, Please try again\n")

            if confirm == "yes":
                if any((idNumber == account.GetIDNumber() and not(accountIndex == accountDatabase.index(account))) for account in accountDatabase):
                    print("There is already an existing account with the same ID Number. Please try again \n")
                else:
                    print("Confirming changes.....\n\n")
                    accountDatabase[accountIndex].UpdateIDNumber(idNumber)
                    break
            if confirm == "exit":
                break

def ChangeEmail(accountDatabase, accountIndex):
    print(f"Your current email is {accountDatabase[accountIndex].GetEmail()}\n")

    while True:
        email = input("Enter your new email: ")

        if not email.endswith(".com")  or email == ".com":
            print("Invalid Input. Please try again. \n")
        else:
            while True:
                confirm = input(f"Your new email is {email}. Confirm? Yes or No. or enter exit to exit\n").lower()

                if confirm == "yes" or confirm == "no" or confirm == "exit":
                    break
                else:
                    print("Invalid input, please try again.\n")
                    
            if confirm == "yes":
                
                if any((email == account.GetEmail() and not (accountIndex == accountDatabase.index(account))) for account in accountDatabase):
                    print("There is already an existing account with the same email. Please try again. \n")
                else:
                    print("Confirming changes.....\n\n")
                    accountDatabase[accountIndex].UpdateEmail(email)
                    break
            if confirm == "exit":
                break

def ChangePhoneNumber(accountDatabase, accountIndex):
    print(f"Your current Phone Number is {accountDatabase[accountIndex].GetPhoneNumber()}\n")

    while True:
        phoneNumber = input("Input your Phone Number: ")

        if not (len(phoneNumber) == 11) or not phoneNumber.startswith("09") or not all(digits.isdigit() for digits in phoneNumber):
            print("Invalid Input. Please Try again. \n")
        else:
            while True:
                confirm = input(f"Your phone number is {phoneNumber}. Confirm? Yes or No\n").lower()

                if confirm == "yes" or confirm == "no" or confirm == "exit":
                    break
                else:
                    print("Invalid input, please try again.\n")
                    
            if confirm == "yes":
                
                if any((phoneNumber == account.GetPhoneNumber() and not (accountIndex == accountDatabase.index(account))) for account in accountDatabase):
                    print("There is already an existing account with the same phone number. Please try again \n")
                else:
                    print("Confirming changes.....\n\n")
                    accountDatabase[accountIndex].UpdatePhoneNumber(phoneNumber)
                    break
            if confirm == "exit":
                break

def ChangePassword(accountDatabase, accountIndex):
    print(f"Your current password is {accountDatabase[accountIndex].GetPassword()}\n")

    
    while True:
        password = input("Input New Password: ")
        while True:
            confirm = input(f"Your password is {password}. Confirm? Yes or No. or enter exit to exit \n").lower()

            if confirm == "yes" or confirm == "no" or confirm == "exit":
                break
            else:
                print("Invalid Input. Please Try again\n")

        if confirm == "yes":
            print("Confirming changes.....\n\n")
            accountDatabase[accountIndex].UpdatePassword(password)
            break
        if confirm == "exit":
            break




#Creates Account
def AccountCreation(accountDatabase):
    print("------------Welcome to Account Creation!------------\n")

    accountNumber = str(len(accountDatabase) + 100000)

    #Name
    while True:
        name = [input("Enter your First Name: \n"),
                input("Enter your Middle Initial: \n"),
                input("Enter your Surname: \n")]

        if not all(((s.isalpha() or s == "." or s == " ") for s in names) and ((names.endswith(".") and names[:-1].isalpha()) if "." in names else all(word.isalpha() for word in names.split())) for names in name):
            print("You have entered an invalid name, Please try again.")
        else:
            while True:
                confirm = input(f"Your name is {name[0]} {name[1]} {name[2]}. Confirm? Yes or No\n").lower()

                if confirm == "yes" or confirm == "no":
                    break
                else:
                    print("Invalid input, please try again.\n")
                    
            if confirm == "yes":
                if any(" ".join(name) == account.GetName() for account in accountDatabase):
                    print("There is already an existing account with the same name. Please try again. \n")
                else:    
                    break

    #ID Number
    while True:
        idNumber = input("Enter your 12-digit National I.D No. : ")


        #Handles error for cases such as "123--123--1234", "123", "1234-1234-123-"
        if (not all((len(idNumber)== 14 or len(idNumber) == 12) and (s.isdigit() or s == " " or s == "-") for s in idNumber)) or ((len(idNumber) == 14) and  not all( (( (chunk[-1] == "-" or chunk[-1] == " ") and (all(digits.isdigit() for digits in chunk[:-1]) ) ) for chunk in [idNumber[i:i+5] for i in range(0, len(idNumber) + 1, 5)][:-1] ) ) or not all ((digits.isdigit() for digits in idNumber[10:14]) )
):
            print("Invalid Input, Please try again.\n")
        else:

            # Formats the variable into " 1234-1234-1234 " 
            if (len(idNumber) == 12 and (s.isdigit() for s in idNumber)):
                idNumber = "-".join(idNumber[i: i+4] for i in range(0, len(idNumber),4))   

            if (len(idNumber) == 14) and (idNumber[4] == " " or idNumber[4] == "-") or (idNumber[9] == " " or idNumber[9] == "-"):
                idNumber = idNumber[:4] + "-" + idNumber[5:]
                idNumber= idNumber[:9] + "-" + idNumber[10:]

            while True:
                confirm = input(f"Your National I.D Number is {idNumber}. Confirm? Yes or No \n").lower()

                if confirm == "yes"  or confirm == "no":
                    break
                else:
                    print("Invalid input, Please try again\n")

            if confirm == "yes":
                if any(idNumber == account.GetIDNumber() for account in accountDatabase):
                    print("There is already an existing account with the same ID Number. Please try again \n")
                else:
                    break

    #Email
    while True:
        email = input("Enter your email: ")

        if not email.endswith(".com")  or email == ".com":
            print("Invalid Input. Please try again. \n")
        else:
            while True:
                confirm = input(f"Your email is {email}. Confirm? Yes or No\n").lower()

                if confirm == "yes" or confirm == "no":
                    break
                else:
                    print("Invalid input, please try again.\n")
                    
            if confirm == "yes":
                if any(email == account.GetEmail() for account in accountDatabase):
                    print("There is already an existing account with the same email. Please try again. \n")
                else:
                    break
            
    #Phone Number
    while True:
        phoneNumber = input("Input your Phone Number: ")

        if not (len(phoneNumber) == 11) or not phoneNumber.startswith("09") or not all(digits.isdigit() for digits in phoneNumber):
            print("Invalid Input. Please Try again. \n")
        else:
            while True:
                confirm = input(f"Your phone number is {phoneNumber}. Confirm? Yes or No\n").lower()

                if confirm == "yes" or confirm == "no":
                    break
                else:
                    print("Invalid input, please try again.\n")
                    
            if confirm == "yes":
                if any(phoneNumber == account.GetPhoneNumber() for account in accountDatabase):
                    print("There is already an existing account with teh same phone number. Please try again \n")
                else:
                    break

    #Password No error handling here, because.... passwords..
    while True:
        password = input("Input Password: ")
        while True:
            confirm = input(f"Your password is {password}. Confirm? Yes or No \n").lower()

            if confirm == "yes" or confirm == "no":
                break
            else:
                print("Invalid Input. Please Try again\n")

        if confirm == "yes":
            break

        
    
    #Initial Deposit
    while True:
        try:
            #input
            while True:
                initialDeposit = input("Enter initial deposit: \n")

                isdeposit = float(initialDeposit)
                if "." not in initialDeposit:
                    initialDeposit = f"{float(initialDeposit): .2f}"
                    break
                elif "." in initialDeposit:
                    if not (len(initialDeposit.split(".")[-1]) == 2) and not(len(initialDeposit.split(".")[-1]) == 1):
                        print("Invalid amount of decimal places. Please try again. \n")
                    else:
                        break

            #Confirmation
            while True:
                confirm = input(f"Your initial deposit is {float(initialDeposit): .2f}. Confirm?. Yes or No: ").lower()

                if confirm == "yes" or confirm == "no":
                    break
                else:
                    print("Invalid Input. Please try again")
            if confirm == "yes":
                break
                
        except ValueError:
            print("Enter a proper value. Please try again.\n")

        

    #Creating new account object
    newAccount = Account(accountNumber, name, idNumber, email, phoneNumber, password, initialDeposit)

    #Appending new account to the database
    accountDatabase.append(newAccount)

    print("Congratulations, you have created your account, Logging in.... \n\n")

    #Actual Logging in
    AccountStatusInterface(accountDatabase, len(accountDatabase)-1)

        
#Login to account
def Login(accountDatabase):
    print("------------Log in Page------------\n")
    while True:

        #Account Number
        while True:
            accountNumber = input("Enter your account number or enter exit to exit: ")
            if accountNumber.lower() == "exit":
                break
            if not any(accountNumber == account.GetAccountNumber() for account in accountDatabase):
                print("That account number does not exist in our database. Please try again.\n")
            else:
                break
        
        if accountNumber.lower() == "exit":
            break

        #Email
        while True:
            email = input("Enter your email or enter exit to exit: ")
            if email.lower() == "exit":
                break
            if not any(email == account.GetEmail() for account in accountDatabase):
                print("Invalid Email. Please Try again.\n")
            else:
                break
        
        if email.lower() == "exit":
            break

        #Password
        while True:
            password = input("Enter your password: ")
            if not any( password == account.GetPassword() for account in accountDatabase):
                print("Invalid Password. Please try again. \n")
            else:
                break
        
        #Actual Logging in
        for account in accountDatabase:
            if accountNumber == account.GetAccountNumber() and email == account.GetEmail() and password == account.GetPassword():
                AccountStatusInterface(accountDatabase, accountDatabase.index(account))
                break
                
        #Checked if Logged in
        if not any((accountNumber == account.GetAccountNumber() and email == account.GetEmail() and password == account.GetPassword()) for account in accountDatabase):
            print("Invalid Account Number, Email and Password. Please try again.\n")
        else:
            break
        
def EditAccountInfo(accountDatabase, accountIndex):
    
    while True:
        print("------------Edit Account Information------------\n")

        while True:
            options = ["a","b","c","d","e","f"]

            userInput = input("What would you like to edit?: \n" +
                              "a.Name\n" +
                              "b.National I.D\n" +
                              "c.Email\n" +
                              "d.Pho