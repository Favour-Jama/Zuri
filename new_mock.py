import random

database= {}


def init():
   
    print ('Welcome to J-Bank')
   
    Have_account = int(input ('Do you have an account with us? \n 1(Yes) 2(No)\n'))
        
    if Have_account==1:
        login()
    elif (Have_account==2):
        register()
    else:
        print('Invalid input')
        init()
                                                                    
def login():
    print ("Welcome \n Login to Your Account")
    
    user_accountnumber = int(input ("Enter your account number\n"))

    #is_valid_account_validation = validation.account_validation (user_accountnumber)
    #if is_valid_account_validation:
        
    user_password = input ('Enter your Password\n')
    
    for account_number, userdetails  in database.items():
        if (account_number==user_accountnumber):

            if (userdetails[3] == user_password):
                
                print ("Invalid Account or Passsword")
                bank_operation(userdetails)
    bank_operation(userdetails)

   
def register():
    print ("Create an account with us")
    first_name = input("Enter your First Name \n")
    last_name = input ("Enter your Last Name\n")
    new_useremail =  input("Enter your Email:\n")
    new_userpassword = input("Enter your password \n")
    print ("Registration Successful!")

    account_number = account_generation()
    
    database[account_number]= [first_name, last_name, new_useremail, new_userpassword]

    print("Your Account has been Created\n")
    print("Loading....")
    print ("Your Account Number is %s" % account_number)

    login ()

def bank_operation (user):

    print ("Welcome on board %s %s" % (user [0], user [1]))
    Select_option = int (input ('These are the available option: \n 1. Withdrawal \n 2. Cash Deposit \n 3. Complaint\n'))
    if Select_option == 1:
        withdrawal()

    elif Select_option== 2:
        deposit ()

    elif Select_option== 3:
        complaint()

    else:
        print("Incorrect Input, Try Again")
        bank_operation(user)

def withdrawal():
    amount= int(input ("How much do you want to withdraw?"))
    print ("Take your", amount,"cash")
    print ("Thank you, see you again.")


def deposit():     
       
    amount_deposit= int(input ("How much would you like to deposit? "))
    print ("You deposited ",amount_deposit)
    print("Your current balance is", amount_deposit)

def complaint ():
    complaint = input("What issues will you like to report?")
    print ("We have received your complaint, we will respond to it shortly")
    print ("Thank you for contacting us.")

            
def account_generation ():
    return random.randrange(1111111111,9999999999)

    print (account_generation())
    
init()
