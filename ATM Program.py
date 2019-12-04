class BankAccount:
    def __init__(self,ID,PIN,checking,savings):
        self.ID = ID
        self.PIN = PIN
        self.checking = checking
        self.savings = savings

    def getID(self):
        return self.ID

    def getPIN(self):
        return self.PIN

    def getSavings(self):
        return self.savings

    def withdraw(self,amount):

        if(self.savings<amount):
            return False
        else:
            self.savings -= amount
            return True

        def deposit(self,amount):
            self.savings += amount

def main():
    account = []
    n=0
    with open("accounts.txt") as file:
        for line in file:
            li = line.split(' ')
            account.append(BankAccount(li[0],li[1],float(li[2]),float(li[3].replace('\n',''))))
            n += 1
userid = input("Enter ID: ")
userpin = input("Enter PIN: ")
i=0


while i<n:
    if(account[i].getID()==userid):
        if(account[i].getPIN()==userpin):
            option = int(input('Enter 1 for withdraw\n 2 for deposit\n 3 for balance: '))
            if(option==1):
                amount = float(input("Enter amount: "))
                if(account[i].withdraw(amount)):
                    print(amount,'withdrawn. Closing balance: ',account[i].getSavings())
                else:
                    print('enter amount within your balance')
            elif(option==2):
                amount = float(input("enter amount: "))
                account[i].deposit(amount)
                print('Balance after deposit:',account[i].getSavings())
            else:
                print('Your savings balance:',account[i].getSavings())
            print('Thank you')
            break

i += 1

if(i==n):
    print('invalid login')
