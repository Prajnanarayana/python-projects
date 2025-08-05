import json
import os


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <=0:
            print(f'Hi {self.owner} , Deposit amount should be greater than 0')
        else:
            self.balance += amount
            print(f"Hi {self.owner} ,Amount Deposited Successfully")
            print(f"Deposited Amount: {amount}")
            print(f"Updated Balance:{self.balance}")
            save_json()
    
    def withdraw(self, amount):
        if amount > self.balance or amount <0:
            print(f"Hi {self.owner}, Amount withdraw is failed")
            print(f'You are trying to withdraw {amount}Rs, but your current balance is {self.balance}')
        else:
            self.balance -= amount
            print("Amount Withdrawn Successfull")
            print(f"Withdrawn Amount: {amount}")
            print(f"Updated Balance:{self.balance}")
            save_json()
            
    def display_balance(self):
        return f"Total Balance in your account {self.balance}"

class SavingsAccount(Account):
    def add_interest(self, rate=(1/100)):
        if self.balance >50000:
            rate=(3/100)
            self.balance*= rate
            print(f'Hi {self.owner}, Interest Given by bank is {rate}')
            save_json()
            return self.balance
        else:
            self.balance *= rate
            print(f'Hi {self.owner}, Interest Given by bank is {rate}')
            save_json()
            return self.balance
    
    
class CurrentAccount(Account):
    def add_interest(self, rate=(3/100)):
        if self.balance >250000:
            rate= (7/100)
            self.balance  *= rate
            print(f'Hi {self.owner}, Interest Given by bank is {rate}')
            save_json()
            return self.balance
        else:
            self.balance  *= rate
            save_json()
            return self.balance


# Load from json file at program start
def load_json():
    if os.path.exists('accounts_data.json'):
        with open('accounts_data.json', 'r') as f:
            return json.load(f)
    return {}

# Save to json file
def save_json():
    data = {}
    for AccNo, acc_obj in account.items():
        # Detect account type
        if isinstance(acc_obj, SavingsAccount):
            acc_type = "Savings"
        elif isinstance(acc_obj, CurrentAccount):
            acc_type = "Current"
        else:
            acc_type = "Unknown"
            
        data[AccNo] = {
            "Username": acc_obj.owner,
            "AccType": acc_type,
            "Balance": acc_obj.balance
        }
    with open('accounts_data.json', 'w') as f:
        json.dump(data, f, indent=2)
        
        


def load_accounts_to_memory():
    data = load_json()
    for AccNo, acc_info in data.items():
        if acc_info.get("AccType") == "Savings":
            account[AccNo] = SavingsAccount(acc_info["Username"], acc_info["Balance"])
        elif acc_info.get("AccType") == "Current":
            account[AccNo] = CurrentAccount(acc_info["Username"], acc_info["Balance"])


def Account_Creation(UserName, AccountType):

    if Account_Type == 1:
        AccountType= 'Savings'
        AccNo= 100
        while 'S'+str(AccNo) in account:
            AccNo+=1
            continue
        else:
            Updated_AccNo= 'S'+str(AccNo)
            balance= int(input("Enter Your Balance for intial Deposit: "))
            if balance <=0:
                balance=0
                print("""You have entered the balance which is not met our bank Policy,
                So We created ZeroBalance Account So that You can deposit the amount later also""")

            account[Updated_AccNo]= SavingsAccount(UserName,balance)
            print(f"Hi {UserName}, Your {AccountType} Account is Created")
            save_json()

    elif Account_Type == 2:
        AccountType= 'Current'
        AccNo= 100
        while 'C'+str(AccNo) in account:
            AccNo+=1
            continue
        else:
            Updated_AccNo= 'C'+str(AccNo)
            balance= int(input("Enter Your Balance for intial Deposit: "))
            if balance <10000:
                print(f"Hi {UserName} you are opening a current Account, You mininum deposit should 10000")
                print('Sorry Your Account is not created')
            else:
                account[Updated_AccNo]= CurrentAccount(UserName,balance)
                print(f"Hi {UserName}, Your {AccountType} Account is Created")
                save_json()
                
    else:
        print("No Other Options is Left. Kindly Contact the Bank")


def operations():
    
    operations= int(input("Enter the Service You want to avali\n 1. Deposit\n 2. WithDrawn\n 3. Display_Balance"))
    AccNo= input("Enter your Account Number: ")
    
    if AccNo in account:
        if operations==1:
            Deposit_Amt= int(input("Enter the Amount to deposit: "))
            print(account[AccNo].deposit(Deposit_Amt))

        elif operations ==2:
            withdraw_Amt = int(input("Enter the Amount to Withdraw: "))
            print(account[AccNo].withdraw(withdraw_Amt))

        elif operations==3:
            print(account[AccNo].display_balance())
        else:
            print("Enter the Correct Input")

    else:
        print("Sorry The given Account Number is Not valid. Enter the Correct Account Number")


if __name__ =='__main__':
    account = {}
    load_accounts_to_memory()
    while True:
        Question = int(input("""Choose the Option\n 1. Account Creation\n 2. Operation(Deposit, Withdrawn, Check Balance) \n 3. Exit """))
        if Question ==1:     
            try:
                UserName= input("Enter the Name: ")
                Account_Type= int(input("""Enter the Account Type \n 1 - Savings Account \n 2 - Current Account\n"""))
            except ValueError:
                print("Kindly Enter the Numeric Values for Account_Type")
            else:
                try:
                    Account_Creation(UserName,Account_Type)  
                    confirmation= input("Wheather You need to Continue to Deposit, Withdrawn or Check balance")
                    
                    if confirmation.lower()=='yes':
                        operations()
                        continue
                    elif confirmation.lower()=='no':
                        print("ThankYou for Banking with us...")
                        break   
                        
                except ValueError:
                    print("Kindly enter the Correct Values")
                    continue

        elif Question ==2:    
            operations()
            continue
            
        elif Question ==3:
            print("ThankYou for Banking with us...")
            break
