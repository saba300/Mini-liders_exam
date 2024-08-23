'''Bank System:

1.create account
2.Deposit
3.Withdraw
4.Exit

თქვენი დავალება იქნება გააკეთოთ ბანკის სისტემა მოცემული სექციებით პითონში,რაც აქამდე ისწავლეთ 
გააკეთეთ იმ მასალით გამოიყენეთ თქვენი მაქსიმალური ცოდნა,მერე კი ჩვენ შევამოწმეთ თუ რა დონის ცოდნა 
გამოიყენეთ და იმის მიხედვით შეიგიმოწმებთ!!!'''



def create_acc():
    name=input("Enter your name: ")
    surname=input("Enter your surname: ")
    email=input("Enter your email: ")
    private_number=input("Enter your private number: ")
    card=input("Enter your card number: ")
    return name, surname, email, private_number, card

def your_balance(bal):
    print(f"your balance is {bal:.2f}")

def deposit():
    amount1=float(input("Enter amount to deposit: "))
    if amount1<0:
        print("Error")
        return 0
    else:
        return amount1
    
def withdrow(balance):
    amount=float(input("Enter amount to withdrow: "))
    if amount<0:
        print("Error")
    elif amount>balance:
        print("Error")
        return 0
    else:
        return amount

balance=0
in_progress=True
all_acc=[]

while in_progress:
    print("Bank system")
    print("1.Create account")
    print("2.Balance")
    print("3.Deposit")
    print("4.Withdrow")
    print("5.Exit")

    num=input("Enter number from 1 to 4: ")
    if num=='1':
        all_acc.append(create_acc())
        print(all_acc)
        
    elif num=='2':
        your_balance(balance)
    elif num=='3':
        balance+=deposit()
    elif num=='4':
        balance-=withdrow(balance)
    elif num=='5':
        in_progress=False
    else:
        print("Your number must be between 1 to 4.")