import random

print("-------ROCK-PAPER-SCISSORS GAME-------")
print("INSTRUCTIONS-")
print("* Rock beats scissors\n* Scissors beat paper\n* Paper beats rock")
user_score=0
com_score=0
round_nu=1
continue_flag = True
while continue_flag:
    print("\nROUND-",round_nu)
    user_choice=input("enter her/his choice:")
    cm_list=['rock','paper','scissor']
    print("Computer choice :")
    com_choice=random.choice(cm_list)
    print(com_choice)
    if user_choice=='rock'and com_choice=='scissor'or user_choice=='paper'and com_choice=='rock'or user_choice=='scissor'and com_choice=='paper':
        user_score+=1
        print("congrets! You win this round")
    if user_choice=='paper'and com_choice=='scissor'or user_choice=='scissor'and com_choice=='rock'or user_choice=='rock'and com_choice=='paper':
        com_score+=1
        print("computer win")
    if user_choice == 'paper' and com_choice == 'paper' or user_choice == 'scissor' and com_choice == 'scissor' or user_choice == 'rock' and com_choice == 'rock':
        print("It's a tie")
    should_continue=input("enter 'y' if you want to play another round\n x for quit:")
    if should_continue=='y':
        continue_flag=True
        round_nu+=1
    else:
        continue_flag=False
if user_score>com_score:
    print("congrats! you win the game")
elif user_score<com_score:
    print("sorry! you loss")
else:
    print("game are tie")
print("your total score are",user_score)
print("computer total score are",com_score)

