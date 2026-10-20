import random
import time
def tie():
    print(f"YOU -> {user_pick} : AI -> {ai}")
    print("It's a tie .")

def result(res):
    print(f"you {user_pick} : ai {ai}")
    print(f"...YOU {res}...")

def count_down():
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print("<<----RESULTS ARE ---->>")
    time.sleep(1)
print("Welcome to the rock paper scissor game\n"+ "Please enjoy it...")
print("Type 'no' anytime you want to go back")
choise=['ROCK','PAPER','SCISSOR']
while True :
    ask=input("Do you want to start the game ? :")
    if ask.strip().lower()=="yes":
        while True :
            user=input("Choose ROCK/PAPER/SCISSOR ")
            user_pick=user.strip().upper()
            ai=random.choice(choise)
            if user_pick=='ROCK' and ai=='ROCK':
                count_down()
                tie()
            elif user_pick=='ROCK' and ai=='PAPER':
                count_down()
                result('won') 
            elif user_pick=='ROCK' and ai=='SCISSOR':
                count_down()
                result('lost')
            elif user_pick=='PAPER' and ai=='ROCK':
                count_down()
                result('won')  
            elif user_pick=='PAPER' and ai=='PAPER':
                count_down()
                tie()
            elif user_pick=='PAPER' and ai=='SCISSOR':
                count_down()
                result('lost')   
            elif user_pick=='SCISSOR' and ai=='ROCK':
                count_down()
                result('lost') 
            elif user_pick=='SCISSOR' and ai=='PAPER':
                count_down()
                result('won')
            elif user_pick=='SCISSOR' and ai=='SCISSOR':
                count_down()
                tie()          
            elif user.strip().lower()=='no':
                break
            else:
                print("Please type 'no' if you want to stop or choose rock/papper/scissor >>>>:")
    elif ask.strip().lower()=="no":
        print("((*-*)..Thankyou for playing..(*-*)__")
        break        
    else :
        print("Please Write 'yes' or 'no' : ")