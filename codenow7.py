import time

def user1():    
    user_input1 = raw_input("Enter a word with 8 or more letters: ")
    if len(user_input1) <= 7:
        print "Not a word with 8 or more letters" 
    else:
        print "Generating your password"
        for sym in xrange(8, 10):
            time.sleep(1.0)
            print '*'*sym
        print "Your password is: "
        password_gen = user_input1.replace('a' , '@' , 10).replace('e', '3' , 10).replace('i', '1', 10).replace('o', '0', 10).replace('u', '2', 10).replace(' ', '_', 10).replace('A', '@', 10).replace('E', '3', 10).replace('I', '1', 10).replace('O', '0', 10).replace('U', '2', 10)
        print password_gen
user1()