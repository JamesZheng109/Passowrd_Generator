from random import randint
character=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',1,2,3,4,5,6,7,8,9,0,
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','#','$','@','!','&',
           '*']
file=open('password.txt','a')
def password_maker():
    purpose=input('Account type? ')
    username=input('Username for account? ')
    amount=int(input('How many characters? '))
    generate=''
    for password in range(amount):
        password=character[randint(0,67)]
        value=str(password)
        generate+=value
    #file.write(purpose+' ('+username+')'+':'+str(generate)+'\n')
    file.write(f'{purpose} ({username}): {generate}\n')
    print(f'Password for {purpose} ({username}):{generate}')
    file.close()
def clear_data():
    check=input('Are you sure?(Y or N): ')
    if check=='Y':
        file.seek(0)
        file.truncate()
        print('Data Cleared')
        file.close()
    elif check=='N':
        pass
    else:
        print('N it is.')
print('Option:\nGenerate\nCLEAR ALL DATA')
option=input('What do you want to do?: ')
if option=='Generate':
    password_maker()
elif option=='Clear Data':
    clear_data()
input('Press the Enter key to close program.')

