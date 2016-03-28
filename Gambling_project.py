import random

A = 10
K = 10
Q = 10
J = 10
cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'K', 'Q', 'J']

def comp_choice(x):
    if x < 21:
        print 'You Lose'
    elif x == 21:
        print 'You Win'
    else:
        print 'Nice'
    return comp_choice(x)

start = random.choice(cards) 
start2 = random.choice(cards)
total = start + start2
print "Welcome to BlackJack. Your cards first two cards are "+start+" and "+start2

user1 = raw_input("Do you want to hit or pass? H/S: ")

# if (start + start2) > 21:
#     start = random.choice(cards)
#     start2 = random.choice(cards)

if user1 == 'H':
    print random.choice(cards)
    # if total+random.choice(cards) < 21:
    #     print "You lose"
    # elif total+random.choice(cards) == 21:
    #     print "You win"
    # else: 
    #     print "Nice."
elif user1 == 'S':
    print "Ok"
    if total > 21:
        print "You lose"
    else:
        print "You win"
else:
    print "Not an option"

user1_newtotal = raw_input("Enter your new total: ")
if user1_newtotal <= 20:
    print " You can get dealt again."
elif user1_newtotal<=22:
    print "You lose"
elif user1_newtotal == 21:
    print "You win"
else: 
    "I dont know what to do"
    
ask_user_again = raw_input("Do you want to hit or pass? H/S: ")

if ask_user_again == 'H':
    print random.choice(cards)
    if random.choice(cards) < 21:
        print "You lose"
    elif random.choice(cards) == 21:
        print "You win"
    else: 
        print "Nice."
elif ask_user_again == 'S':
    print "Ok"
    if total < 21:
        print "You lose"
    else:
        print "You win"
else:
    print "Not an option"
    
ask_user_again2 = raw_input("Do you want to hit or pass? H/S: ")
if ask_user_again2 == 'H':
    print random.choice(cards)
    if random.choice(cards) < 21:
        print "You lose"
    elif random.choice(cards) == 21:
        print "You win"
    else: 
        print "Nice."
elif ask_user_again2 == 'S':
    print "Ok"
    if total < 21:
        print "You lose"
    else:
        print "You win"
        
