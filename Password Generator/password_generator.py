from random import randint
character=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',1,2,3,4,5,6,7,8,9,0,
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','#','$','@','!','&',
           '*']
def password_maker():
    purpose,username,amount,generate=input('Account type? '),input('Username for account? '),int(input('How many characters? ')),''
    with open('password.txt','a') as file:
        for password in range(amount):password=character[randint(0,67)];value=str(password);generate+=value
        file.write(f'{purpose} ({username}): {generate}\n');print(f'Password for {purpose} ({username}):{generate}')
def clear_data():
    check=input('Are you sure?(Y or N): ')
    if check=='Y':file.seek(0);file.truncate();print('Data Cleared');file.close()
    elif check=='N':pass
    else:print('N it is.')
def read():
    with open('password.txt','r') as file:content=file.read();print(content)
def main():
    print('Option:\nGenerate\nCLEAR ALL DATA\nDisplay Info');option=input('What do you want to do?: ')
    if option=='Generate':password_maker()
    elif option=='Clear Data':clear_data()
    elif option=='Display Info':read()
    input('Press the Enter key to close program.')
if __name__=='__main__':main()
