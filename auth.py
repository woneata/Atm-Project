#register
#-first name, last name, password, email
#-generate user id

#login
# - account number, email and password

#bank operations

#Initializing the system

import random
database ={} #dictionary

def init():
    
    print("Welcome to Bank PHP")

   
    haveAccount = int(input("Do you have an account with us: 1 (yes) 2 (no)? \n"))

    if(haveAccount == 1):
        
        login()
    elif(haveAccount == 2):
        
        print(register())
    else: 
        print("You have selected an invalid option")
        init()

def login():
    print("******* Login *******")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password? \n")

    for accountNumber, userDetails in database.items():
        if(userDetails[3] == password):
            operations(userDetails)
    print('Invalid account or password')
    login()

    

def register():
    print('****** Register ******')

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input ("What is your last name? \n")
    password = input('Create a password? \n')

    accountNumber = generateAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password ]

    print("Your account has been created")
    print(" == ==== ===== ===== ===")
    print('Your account number is: %d' % accountNumber)
    print('Make sure you keep it safe')
    print(" == ==== ===== ===== ===")

    login()

  

def operations(user):
    print('Welcome %s %s' %( user[0], user[1] ) )
   
    selectedOption = int(input("What would you like to do? (1) deposit (2) deposit (3) Logout (4) Exit \n"))

    if(selectedOption == 1):
                
        deposit()
    elif(selectedOption == 2):
               
        withdrawal()
    elif(selectedOption == 3):
        logout()
                
    elif(selectedOption == 4):
               
        exit()
    else:
        print("Invalid option selected")
        operations(user)


def withdrawal():
    print('Withdrawal')

def deposit():
    print('Deposit')

def generateAccountNumber():

    return random.randrange(111111,999999)

def logout():
    login()






#### ACTUAL BANKING SYSTEM

init()