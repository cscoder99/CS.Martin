import random

dict = {'A':'10', 'K':'10', 'Q':'10', 'J':'10'}

cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'K', 'Q', 'J']
first_card = random.choice(cards)
second_card = random.choice(cards)
third_card = random.choice(cards)
fourth_card = random.choice(cards)
fifth_card = random.choice(cards)

print "Welcome to blackjack. Keep in mind, that all letter cards count as 10"
print "Your cards are "+first_card+" and "+second_card

user1 = raw_input("Do you want to hit or stay? H/S ")

while (user1 == 'H'):
    print "OK! Your new card is "+third_card
    break
    
# user2 = raw_input("Enter you new total: ")

total = raw_input("Enter you new total: ")
print "Your total is "+total

if (user1 == 'S') or (user1 == 's'):
    print total
    if total <= '21':
        print 'You WIN!!!'
    else: 
        print "You Lose!"

if total <= '20':
    user1 = raw_input("You can still play. Do you want to hit or stay? H/S ")
    if (user1 == 'S') or (user1 == 's'):
        print total
    if total <= '21':
        print 'You WIN!!!'
    else: 
        print "You Lose!"
    if (user1 == 'H') or (user1 == 'h'):
        print "Your new card is "+fourth_card
elif total == '21':
    print "YOU WIN!!!"
else:
    print "You lose!"

if total <= '20':
    user1 = raw_input("You can still play. Do you want to hit or stay? H/S ")
    print "Your new card is "+fifth_card
print "You lose!"
