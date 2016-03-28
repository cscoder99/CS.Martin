import time
print "Pyg Latin Translator"

def to_pyg_latin(x):
    x = x[1:]+x[0]+'ay'
    return x

user_input1 = raw_input("Enter the word or phrase you want to translate: ")
print to_pyg_latin(user_input1)