import random
lang = ['Konichiwa', 'Hola', 'Bonjour']

user1 = raw_input("Say hello in English so the computer can say it back in a foreign langauge: ")

if (user1 == 'Hello') or (user1 == 'hello'):
    print random.choice(lang)
else:
    print "That is not hello in English"