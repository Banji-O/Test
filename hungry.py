
hungry = input("are you hungry? ")

if hungry in ['yes','Yes', 'YES']:
    print(f'eat rice')  
    print('eat fries')
    print('eat pizza')  
else:
    print(f"have a nice day")
    
thirsty = str(input('are you thirsty?'))

if thirsty in ['yes', 'Yes', 'YES']:
    print('drink water')
elif thirsty == None:
    print(f'drink chilled soda')    
else: 
    print('have a nice day')
    
       
food = ['yam', 'bread', 'fufu', 'spag']

