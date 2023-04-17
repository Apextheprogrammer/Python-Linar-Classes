print('Let the lottery games begin!')
name=input('What is your name: ')
amount=float(input('How much are you betting with: $'))
a=len(name)*16.8*amount
if 2000>=a>=840:
    print('Congratulations! You are the winner.')
else:
    print('Unfortunately, you didnt win. Better luck next time mate!')