import random

database= {}
def init():
    valid_option_selected = False
    print ('Welcome to J-Bank')
    while valid_option_selected== False:
        Have_account = int(input ('Do you have an account with us? \n 1(Yes) 2(No)\n'))
        
        if Have_account==1:
            valid_option_selected= True
            login()
        elif (Have_account==2):
            valid_option_selected = True
            print(register())
        else:
            print('invalid input')

                                                                    
def login():
    print ("Welcome \n Login to Your Account")

    isLoginSuccessful = False
    
    while isLoginSuccessful == False:
        user_accountnumber =int (input ("Enter your account number\n"))
        user_password = input ('Enter your Password')
    
    for user_accountnumber.userdetails  in database.items():
        if account_number=user_accountnumber:
            if (userdetails)

    bank_operation()
def register():
    print ("Create an account with us")
    new_useremail =  input("Enter your Email:\n")
    first_name = input("Enter your First Name \n")
    last_name = input ("Enter your Last Name\n")
    new_userpassword = input("Enter your password \n")
    print ("Registration Successful!")

    account_number = account_generation()
    
    database[account_number]= [first_name, last_name, new_useremail, new_userpassword]

    login ()

def bank_operation ():
    if (password in allowedPassword [userID]):
            print ("Welcome on board %s", name)
            print ("Today is", current_time)
            print ('These are the available option:')
            print ("1. Withdrawal")
            print ("2. Cash Deposit")
            print ("3. Complaint")

def account_generation ():
    return random.randrange(1111111111,9999999999)

print (account_generation())
init()