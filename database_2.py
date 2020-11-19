USER_LIST = ['Andrew', 'Alex', 'Josh', 'Vishnu']
INITIAL_USER_LEN = len(USER_LIST)
PASS_LIST = ['an123', 'al12', 'jo1234', 'v123']
INITIAL_PASS_LEN = len(PASS_LIST)


def sign_in():
    print('Enter the Username: ')
    username = str(input(' ')).title()
    while username is not None:
        for name in USER_LIST:
            if username == name:
                print('Already username exist\n Please try again.')
                #  username = str(input(' ')).title()
            elif username != name:
                USER_LIST.append(username)
                print('Username Updated')
                FINAL_LEN = len(USER_LIST)
                #  password update need to be done
                sign_pass_update()
                return FINAL_LEN
            else:
                print('Already username exist\n Please try again.')

            username = str(input(' ')).title()
        break

    if INITIAL_USER_LEN == sign_in():
        sign_in()
    else:
        exit()


def sign_pass_update():
    print('Enter the password: ')
    password = str(input(' '))
    if password is not None:
        PASS_LIST.append(password)
        print('Password updated')
        return password


def log_in():
    print('Username: ')
    username = str(input(' ')).title()
    for user, password in zip(USER_LIST, PASS_LIST):
        if username == user:
            data = password
            return data
        else:
            pass


def pass_verify(data):
    print('Enter the password: ')
    password = str(input(' '))
    while password is not None:
        if password == data:
            print('Loading....')
            print('Login Successful')
            exit()
        else:
            print('Incorrect Password.\n Try again.')
        print('Password: ')
        password = str(input(' '))
