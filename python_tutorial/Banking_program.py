#python banking program

def show_balance(balance):
    print(f"Your balance is {balance:.2f}")

def deposit():
    amount=float(input("Enter the amount to deposit : "))

    if amount<0:
        print("! Please enter a valid amount !")
        return 0
    else:
        return amount


def withdrawal(balance):
    amount = float(input("Enter the amount to withdrawal : "))
    if balance<amount:
        print("! INSUFFICIENT BALANCE !")
        return 0
    elif amount<0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount
def main():
    balance=0
    is_running=True

    while is_running:
        print("-------BANKING APPLICATION-------")
        print(" 1.) SHOW BALANCE")
        print(" 2.) DEPOSIT")
        print(" 3.) WITHDRAWAL")
        print(" 4.) EXIT")
        print("---------XXXXXXXXX----------")

        choice=input("Enter your choice (1/2/3/4) : ")

        if choice == "1":
            show_balance(balance)

        elif choice == "2":
            balance +=deposit()

        elif choice == "3":
            balance -= withdrawal(balance)

        elif choice == "4":
            is_running=False

        else:
            print("!Not Valid!")

    print("Thank you and have a nice day ")

if __name__=='__main__':
    main()