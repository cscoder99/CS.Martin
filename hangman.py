inp = raw_input("What is your name: ")
print "Hello "+inp+". Welcome to hangman! Keep in mind spaces count as letters."

word = inp
guesses = ''

#number of turns
turns = 10

#turns 
while turns > 0:
  missed = 0
  for letter in word:
    if letter in guesses:
      print letter,
    else:
      print '_',
      missed += 1
  print

  if missed == 0:
    print 'You win!'
    break

  guess = raw_input('guess a letter: ')
  guesses += guess

  if guess not in word:
    turns -= 1
    print 'Try again.'
    print turns, 'more turns'
    if turns == 0:
      print 'The word is', word
      
      break