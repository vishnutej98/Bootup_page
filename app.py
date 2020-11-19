#!Python3
#  app.py - this is text-based application used for creating database.
#  data store in db is not original this is only for trial purpose.
#  app.py has two additional files for creating the database.

from database_2 import sign_in, log_in, pass_verify

print('-' * 30)
print('Welcome\nAboard!')
print('-' * 30)
print(('-' * 13) + 'MENU' + ('-' * 13))
print('1. Sign In')
print('2. Log In')
print('3. Forgot Email/Password')
print('Q. Quit')
print('-' * 30)


def menu():
    user_input = input(': ')
    while user_input != 'Q':
        if user_input == '1':
            print('**LOADING**')
            sign_in()
            break
        elif user_input == '2':
            print('**LOADING**')
            pass_verify(data=log_in())
            break
        elif user_input == '3':
            print('todo')
            break
        elif user_input == 'q':
            print('Thanks for using')
            print(':-)')
            break
        else:
            print('Error!!')

        user_input = input(': ')


menu()
