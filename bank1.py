import bank

account_holder_name = input("Enter your name: ")
account = bank.BankAccount(account_holder_name)

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Quit")
    choice = int(input("Enter your choice (1/2/3/4): "))

    if choice == 1:
        amount = float(input("Enter the deposit amount: "))
        account.deposit(amount)
    elif choice == 2:
        amount = float(input("Enter the withdrawal amount: "))
        account.withdraw(amount)
    elif choice == 3:
        account.check_balance()
    elif choice == 4:
        print("Thank you for using the banking application!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")