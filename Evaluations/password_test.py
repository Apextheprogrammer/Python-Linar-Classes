password=(input('Enter your password: '))
if len(password)<5:
    print('Pls input a longer password.')
    if password!=str():
        print('Pls must include letters. ')
else:
    print('The password is valid. ')