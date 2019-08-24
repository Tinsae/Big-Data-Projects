# function to validate password
def password_check(passwd): 
    val = True
    # At least 1 letter between [a-z]
    if not any(letter.islower() for letter in passwd): 
        print('At least 1 letter between [a-z]') 
        val = False
    # At least 1 number between [0-9]
    if not any(letter.isdigit() for letter in passwd): 
        print('At least 1 number between [0-9]') 
        val = False
    # At least 1 letter between [A-Z]
    if not any(letter.isupper() for letter in passwd): 
        print('At least 1 letter between [A-Z]') 
        val = False
    # At least 1 character from [$#@]
    if not any(letter in "$@#" for letter in passwd): 
        print('At least 1 character from [$#@]') 
        val = False  
    # Minimum length of transaction password: 6
    if len(passwd) < 6: 
        print('Minimum length of transaction password: 6') 
        val = False
    # Maximum length of transaction password: 12
    if len(passwd) > 12: 
        print('Maximum length of transaction password: 12') 
        val = False
    return val  

# Main method 
def main(): 
    print("Testing method...")
    passwd_one = 'aA@22$$'
    if (password_check(passwd_one)): 
        print(passwd_one , " is Valid password") 
    else: 
        print(passwd_one , "is Invalid Password !!")   
    print()
    print()
    passwd_two = '13Dba'
    if (password_check(passwd_two)): 
        print(passwd_two , " is Valid password") 
    else: 
        print(passwd_two , " is Invalid Password !!")

    print("Now accepting input")

    passwd_input = input("Enter password: ")
    if(password_check(passwd_input)):
        print(passwd_input , " is Valid password") 
    else:
        print(passwd_input , " is Invalid password") 

# Driver Code         
if __name__ == '__main__': 
    main() 