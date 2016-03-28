user = raw_input("Enter your name: ")

gender = raw_input("Enter your gender: ")

if (gender == "male") or (gender == "Male"):
    pronoun = "his"
    pronoun_2 = "he"
    pronoun_3 = "him"
elif (gender == "female") or (gender == "Female"):
    pronoun = "her's"
    pronoun_2 = "she"
    pronoun_3 = "her"
else:
    print "That is not a gender"
    
scenario 1 = user+" walked into a bar and 