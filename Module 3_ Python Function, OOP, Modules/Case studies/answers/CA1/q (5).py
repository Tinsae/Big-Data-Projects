# 5
# username: [password, balance]
users = {"tinsae": ["1234", 5000], "sardeep": ["ad33%#1bbD", 3000]}

def withdraw(name, amount):
    if amount <= users[name][1]:
        users[name][1] -= amount
    else:
        print("insufficient balance")
            
def deposit(name, amount):
        users[name][1] += amount
        
def validate_user(name, password):
    if name in users and users[name][0] == password:
        return True
    else:
        return False
def change_pass(name, new_pass):
    users[name][0] = new_pass
    print("password changed\n")

def display_balance(name):
    print("Current balance: ", users[name][1])
def display_all_balances():
    print("{:8s} {:6s}".format("Name", "Balance"))
    for name, others in users.items():
        print("{:8s} {:6.2f}".format(name, others[1]))
 
while(True):
    print("\n\nWelcome To Bank\n")
    name = input("Enter user name: ")
    password = input("Enter password: ")

    if(validate_user(name, password)):
        print("Login successeful")
        print("Enter 1 to withdraw")
        print("Enter 2 to deposit")
        print("Enter 3 to check balance")
        print("Enter 4 to change password")
        print("Enter 5 to exit")


        choice = input()
        if(int(choice) == 1):
            withdraw(name, float(input("Enter amount: ")))
        elif(int(choice) == 2):
            deposit(name, float(input("Enter amount: ")))
        elif(int(choice) == 3):
            display_balance(name)
        elif(int(choice) == 4):
            change_pass(name, input("Enter new password: "))
        elif(int(choice) == 5):
            break
        else:
            print("wrong choice")
# see all account balances
print("\nShowing all account balances\n")
display_all_balances()