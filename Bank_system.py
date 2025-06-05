#users data
user1 = {"user": "ali", "password": "vli21_XO", "balance": 4300}
user2 = {"user": "ebrahim", "password": "monir-sakr", "balance": 6500}
users = [user1, user2]

#FUNCTIONS

#login
def login():
    login_state = False
    attempts = 0
    max_attempts = 3
    current_user = None

    username = input("Please enter your user : ").lower()

    for i in users:
        if i["user"] == username:
            current_user = i
            break

    if current_user:  # check user
        while login_state == False and attempts < max_attempts:
            password = input("\nPlease enter your password ")
            attempts += 1
            if password == current_user["password"]:
                print("\nWelcome", current_user['user'])
                select_operation(current_user)
                login_state = True
            else:
                remaining = max_attempts - attempts
                print("\nWrong password, Remaining attempts: ", remaining)
    else:
        print("\nUser not found")

#select operation
def select_operation(user):
    operation = input("""\nPlease enter your operation: 
  1:change password
  2:check balance
  3:deposit money
  4:withdraw money 
  5: Transfer money: """)

    match operation:
        case "1":
            Change_password(user)
        case "2":
            Check_balance(user)
        case "3":
            Deposit_money(user)
        case "4":
            Withdraw_money(user)
        case "5":
            Transfer_money(user)
        case _:
            print("\nInvalid operation")

#1_Change password
def Change_password(user):
    if user["password"] == input("\nPlease enter your current password "):
        new_password = input("\nPlease enter your new password ")
        if new_password == user["password"]:
            print("\nNew password can't be the same as the old one")
            return
        user["password"] = new_password
        print("\nPassword changed successfully")
    else:
        print("\nWrong password, operation failed")

#2_Check balance
def Check_balance(user):
    print("\nYour balance is", user["balance"])

#3_Deposit money
def Deposit_money(user):
    deposit = int(input("\nPlease enter the amount you want to deposit"))
    user["balance"] += deposit
    print("\nOperation succeed. Your new balance is", user["balance"])

#4_Withdraw money
def Withdraw_money(user):
    print("\nYour current balance is", user["balance"])
    withdraw = int(input("\nPlease enter the amount you want to withdraw"))
    if withdraw > user["balance"]:
        print("\nInsufficient balance")
    else:
        user["balance"] -= withdraw
        print("\nOperation succeed. Your new balance is", user["balance"])

#5_Transfer money
def Transfer_money(user):
    receiver_name = input("Enter the username you want to transfer money to: ").lower()

    receiver = None
    for i in users:
        if i["user"] == receiver_name and i != user:
            receiver = i
            break

    if receiver is None:
        print("Invalid receiver.")
        return

    amount = int(input("Enter the amount to transfer: "))
    if amount <= 0:
        print("Amount must be greater than 0.")
    elif amount > user["balance"]:
        print("Insufficient balance.")
    else:
        user["balance"] -= amount
        receiver["balance"] += amount
        print("Transfer successful. You sent:", amount, "to", receiver['user'])
        print("Your new balance is:", user['balance'])


login()
