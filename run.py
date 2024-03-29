#!/usr/bin/env python3.7
from user import User, Credentials
 

def create_user(fname, lname, username, password):
    '''
    Function to create a new contact
    '''
    new_user = User(fname, lname, username, password)
    return new_user


def save_user(User):
    '''
    Function to save contact
    '''
    User.save_user()


def create_Credentials(saccount, susername, spassword, username):
    '''
    Function to create a new contact
    '''
    new_credentials = Credentials(saccount, susername, spassword, username)
    return new_credentials


def save_credentials(Credentials):
    """
    function to save credential
    """
    Credentials.save_credentials()


def del_credentials(Credentials):
    Credentials.delete_credentials()


def find_credentials(number):

    return Credentials.find_by_name_credential(number)


def display_credentials():
    '''
    Function that returns all the saved contacts
    '''
    return Credentials.display_credentials()

def generate_password():

    return Credentials.generate_password()



def authenticate_login(username, password):
    return User.login_authentication(username, password)


def main():

    print("Hello Welcome to your user/credential_list. What is your name?")
    user_name = input()
    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short code : ca- create a new user account ")
        short_code = input().lower()

        if short_code == 'ca':
            print("new Account")
            print('-'*10)

            print("First name.....")
            f_name = input()

            print("Second name.....")
            s_name = input()

            print("Username.....")
            U_name = input()

            print("Password.....")
            paswd = input()

            # create and save new user
            save_user(create_user(f_name, s_name, U_name, paswd))
            print('\n')
            print(f"New user {f_name} {s_name} created")
            print('\n')

            print("login:username and password is requird")
            print('-'*10)
            print("your username.....")
            U_name = input()

            print("your password....")
            paswd = input()

            # log in
            loggedin = authenticate_login(U_name, paswd)

            if loggedin:
                print('-'*10)
                print(f'Welcome {loggedin.username}')
                print('-'*10)
                print('Choose the options below to navigate through the app:')
                print('-'*10)

                while True:
                    print("Use these short codes : cc- create credentials, dc - display credentials,del-delete credentials ex -exit the credentials list ")
                    short_code = input().lower()

                    if short_code == 'cc':

                        print("Creat social account...")
                        print('-'*10)

                        print("Social media name...")
                        medianame = input()

                        print("Social Username")
                        S_username = input()

                        while True:
                            print("use 'gen' to generate pasword or use 'ent'to enter your own prefferd password")
                            passopt= input().lower()
                            if passopt == 'gen':
                                S_passwd = generate_password()
                                break
                            elif passopt == 'ent':
                                print('Enter your password:')
                                S_passwd = input()
                                break
                            else:
                                print("WRONG!. please try again")
                            
                        save_credentials(create_Credentials(medianame,S_username,S_passwd,loggedin.username))
                        print("_"*10)
                        print('\n')
                        print(f'Credentials for "{medianame}" with username "{S_username}" and password "{S_passwd}" has been created.')
            
                    elif short_code == 'dc':
                        print('\n')
                        if display_credentials(): 

                            print("social media credentials available are:")
                            print("\n")
                    

                            count = 0   
                            for credential in display_credentials():
                                if credential.username == loggedin.username:
                                    count += 1
                                    print(f'They are {count}. Social Media: {credential.social_account}, Username: {credential.username}.')
                                    print('\n')
                        else:
                            print("Sorry no credentials saved here!")
            
                    elif short_code =="del":
                        print("name of the social media you want to delete!")
                        account = input()
                        if find_credentials(account):
                            del_credentials(find_credentials(account))
                            print('\n')
                            print("credential has been deleted")

if __name__ == "__main__":
    main()