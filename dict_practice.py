import time
user_input1 = raw_input("Enter a message: ")
print "Decoding message..."
time.sleep(1.0)

decoder = {'a':'1', 
           'b':'2', 
           'c':'3', 
           'd':'4',
           'e':'5',
           'f':'6',
           'g':'7',
           'h':'8',
           'i':'9',
           'j':'10',
           'k':'!',
           'l':'@',
           'm':'#',
           'n':'$',
           'o':'%',
           'p':'^',
           'q':'&',
           'r':'*',
           's':'(',
           't':')',
           'u':'<',
           'v':'>',
           'w':'?',
           'x':'/',
           'y':'{',
           'z':'}',
           ' ':'+',
           '.':'-',
           '?':'~',
           '!':','}
           
new_word = ''
yes = ['y','yes','Y','Yes']
no = ['N','n','no','No']
for i in user_input1:
    new_word+=decoder[i]    
    
print new_word
user_input2 = raw_input("Do you want to reverse this decode? Y/N ")

if user_input2 in yes:
    print "OK!"
    print "Encoding decoded message"
    time.sleep(1.0)
    print user_input1
elif user_input2 in no:
    print "OK. Glad to decode for you!"
else:
     print "Not an option"