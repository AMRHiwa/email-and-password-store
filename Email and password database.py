# importing the module for working with sql database and regex
from mysql.connector import connect
import re


# define the function for checking valid or invalid and email
def valid_email(email):
    # define a patter by regex for checking the email
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    # comparing the email and pattern with regex module
    if re.match(pattern, email):
        return True
    else:
        return False

# define a function for getting the Email and password from user
def get_email_password():

    # define a infinit loop to getting a currect email
    while True:

        # getting the email from user
        email = input('Enter your Email: ')

        # checking be valid or invalid email
        if valid_email(email):

            # if email is valid break the loop
            break
        
        else:

            # if email is not valid showing message
            print('Invalid Fromat.\nEmail must be like : personal_info@domain\nPlease try again.\n')

    # getting the password
    password = input('Enter your password: ')

    # the valid email and password to main program
    return email, password

# define the main function
def main():

    # connecting to my database
    cnx = connect(user='root', password='44527077'
                , host='127.0.0.1', database='python_db')

    # create a cursor for our database
    cursur = cnx.cursor()

    # create table for sign_in information
    cursur.execute('CREATE TABLE sign_in (username VARCHAR(255), password VARCHAR(128))')

    # commit the all change
    cnx.commit()

    # getting email and password from user by our function
    email, password = get_email_password()

    # adding information to our DataBase
    cursur.execute(f"INSERT INTO sign_in VALUE (\'{email}\', \'{password}\')")

    # commit the all change
    cnx.commit()

    # showing message for user
    print('Done!')

    # close the cursor and database in our program
    cnx.close()

if __name__ == "__main__":
    main()

