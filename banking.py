# empty list that will be appended to in load accounts function
account_list = []


def load_accounts(file):
    '''
    A function that loads the user data from text file.
    Args:
    File containing account info.
    Returns:
    Account list: list of lists including username, password, full name, balance
    '''

    infile = open(file, "r")
    lines = infile.readlines()
    for line in lines:
        account_list.append(line.strip().split(','))
    infile.close()
    return account_list


def find_user(account):
    '''
    A function that displays full name and account balance.
    Args:
    Takes in user account after being validated.
    '''
    print(f"Your full name is {account[2]}")
    print(f"Your account balance is {account[3]}.")


def deposit(account, deposit_amount):
    '''
    A function that adds deposit amount to balance.
    Args:
    Takes in account and deposit amount.
    Returns:
    account with updated total balance
    '''

    account[3] = int(account[3])
    account[3] += deposit_amount
    print(f"Your account balance is {account[3]}.")
    return account


def withdraw(account, withdraw_amount):
    '''
     A function that subtracts withdraw amount from balance.
    Args:
    Takes in account and withdraw amount.
    Returns:
    account with updated total balance
    '''

    account[3] = int(account[3])
    if withdraw_amount <= account[3]:
        account[3] -= withdraw_amount
        print(f"Your account balance is {account[3]}.")
        return account
    else:
        print('Insufficient funds.')


def login():
    '''
    A function that prompts for user input for username and password and validates against list.
    Calls banking function is account is valid.
    Returns:
    User account info.
    '''
    username = input("Enter username: ")
    password = input("Enter password: ")

    for account in account_list:
        if account[0] == username and account[1] == password:
            banking(account)
            return account
    else:
        print('Username and password not found')


def banking(account):
    '''
    A function that prompts for user to select view balance, deposit, withdraw, or quit.
    Calls other functions depending on user selection.
    Continues looping through selections until users chooses to quit.
    Args:
    Account info
    '''
    login = True
    while login == True:
        select = int(input("Do you want to 1. view balance, 2. make a deposit, 3. withdraw, or 4. quit? Please enter 1, 2, 3, or 4: "))
        if select == 1:
            find_user(account)
        elif select == 2:
            deposit_amount = int(input("Deposit amount: "))
            deposit(account, deposit_amount)
        elif select == 3:
            withdraw_amount = int(input("Withdraw amount: "))
            withdraw(account, withdraw_amount)
        elif select == 4:
            print('Goodbye.')
            break
        else:
            print('You have not entered a valid selection. Please try again.')

# call functions to start program
load_accounts('data.txt')
login()
