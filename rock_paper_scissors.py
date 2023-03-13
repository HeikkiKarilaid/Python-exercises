import random
print("A paper, rock, scissors game.")
win=False

while win==False:
    user_input=input("Input Rock, paper or scissors--->")
    user_input=user_input.lower()
    comp=random.choice(['rock','paper', 'scissors'])
    if user_input=='rock' and comp=='scissors':
        print(f'Computer has {comp}' )
        print('Rock beats scissors. You win!')
        win=True
    
    elif user_input=='paper' and comp=='rock':        
        print(f'Computer has {comp}' )
        print('Paper beats rock. You win!')
        win=True
    
    elif user_input=='scissors' and comp=='paper':
        print(f'Computer has {comp}' )
        print('Scissors beats paper! You win!')
        win=True
    elif user_input==comp:
        print(f'Computer has {comp} and you have {user_input}. It´s a tie. Try again!' )
    else:
        print(f'Computer has {comp}' )
        print(f'{comp} beats {user_input}')
        print('You lose.. Try again')  