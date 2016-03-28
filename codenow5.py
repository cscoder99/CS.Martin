import math
print "This is a calculator to find the time of any physics problem given the vi, vf and acceleration."

vi = float(raw_input("Enter is the initial velocity: "))
vf = float(raw_input("Enter is the final velocity: "))
a = float(raw_input("Enter is the acceleration: "))

if a == 0:
    print "Does not leave the ground"
else:
    d = (vf*vf-vi*vi)/(2*a)
    t = ((vf-vi)/a)*(-1)
    t2 = (vf-vi)/a
    
    rt2 = round(t*2, 1)
    rt = round(t*2, 1)

    if t < 0:
        print str(rt2)+"s"
    elif t == 0:
        print str(0)+"s"
    else:
        print str(rt)+"s"