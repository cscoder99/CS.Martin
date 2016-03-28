import math

print "This is a calculator to find the roots of any quadratic function your math teacher throws at you."
print "Just type the 'a', 'b', 'c' term of the equation in the console"

a = float(raw_input("Enter the first coefficient: "))
b = float(raw_input("Enter the second coefficient: "))
c = float(raw_input("Enter the third coefficient: "))

discrimnent = b**2-4*a*c

if discrimnent < 0:
    print "This equation has no real solution but the imaginary roots are"
    discrimnent = discrimnent*-1
    aterm = (math.sqrt(discrimnent))/(2*a)
    bterm = (-b)/(2*a)
    print str(aterm)+"+"+str(bterm)+"i"
    print str(aterm)+"-"+str(bterm)+"i"
elif discrimnent == 0:
    print "Your solution is zero"
else:
    one = (-b+math.sqrt(discrimnent))/(2*a)
    two = (-b-math.sqrt(discrimnent))/(2*a)
    print "Your roots are "+str(round(one, 1))+" and "+str(round(two, 1))