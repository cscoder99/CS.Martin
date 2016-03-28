import time
import math
user_input = raw_input("Enter your name to begin: ")
print "Welcome "+user_input+". You are about to embark on a mysterical journey that is designed to help you with basic arethmatic math."
time.sleep(1.0)
print "Let's us begin!"
time.sleep(1.0)

def gamestart():    
    user_input2 = int(raw_input("What is your age: "))
    print "Determining eligibility..."
    time.sleep(1.0)
    if user_input2 < 9:
        print "You are too young"
    else:
        print "You qualify to play"
gamestart()

user_input3 = raw_input("You are in a murder house and the killer is fast on the run. You are trying to escape but you find yourself in a prediciment. There are two doors. Which one do you choose? Right or Left: ")
print "Opening the "+user_input3+" door."
time.sleep(1.5)
if (user_input3 == "Left") or (user_input3 == "left"):
    print "You chose poorly. It is nothing but a furnance that locked behind you and started burning you."
    exit()
elif (user_input3 == "Right") or (user_input3 == "right"):
    print "You chose wisely but you are still not out of the house. Now in order enter the next room, you must solve a problem"
else:
    print "That is not a direction."

user_input4 = int(raw_input("What is 25*2: "))
if user_input4 == 50:
    print "You are correct. You may proceed to the next room."
time.sleep(1.0)
print "The room you have now entered is dark."

user_input5 = raw_input("Do you wish to solve a bonus question to get a flashlight? ")
if user_input5 == ("Yes") or ("yes") or ("YES"):
    bonus_1 = raw_input("Good choice. The flashlight will be helpful considering the room you have entered is a LABRYNTH!. In order to get it, what is sqrt(2)+sqrt(4)? ")
    if bonus_1 == "2+sqrt(2)":
        print "You are correct! You have obtained a flashlight. Lucky you."
    else:
        print "That is incorrect. You get no fashlight."
elif user_input5 == ("No") or ("no") or ("NO"):
    print "Bad choice...The dark room you are in is a LABRYNTH!"
else:
    print "That is not a choice."
    exit()
    
def flashlight():
    print "Now that you have aquired a flashlight you can use it to find secret items to get out of the labrynth quickly"
    user_input6 = raw_input("To turn on the flashlight, type 'Turn on' ")
    if user_input6 == ("On") or ("on"):
        print "Your flashlight is now on."
    else: 
        print "Ok, you can use this when you need it."
            
flashlight()

print "You are officially in the labrynth!!! Unfortunately, as soon as you walked in you stepped on a detanator."
# user_input7 = raw_input("")


