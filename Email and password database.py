from mysql.connector import connect
import re

def valid_email(email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(pattern, email):
        return True
    else:
        return False


def get_email_password():
    while True:
        email = input('Enter your Email: ')
        if valid_email(email):
            break
        else:
            print('Invalid Fromat.\nEmail must be like : personal_info@domain\nPlease try again.\n')
    password = input('Enter your password: ')

    return email, password


# connecting to my database
cnx = connect(user='root', password='44527077'
            , host='127.0.0.1', database='python_db')
cursur = cnx.cursor()

# create table for sign_in information
cursur.execute('CREATE TABLE sign_in (username VARCHAR(255), password VARCHAR(128))')
cnx.commit()

email, password = get_email_password()

# adding information
cursur.execute(f"INSERT INTO sign_in VALUE (\'{email}\', \'{password}\')")
cnx.commit()
print('Done!')

cnx.close()



