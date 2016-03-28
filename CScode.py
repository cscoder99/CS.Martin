num = raw_input("Enter a Number: ")
print num
numlength = len(num)
print numlength 

all_numerical = True

for x in xrange(numlength):
   print "loop", x
   if num[x] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
      print num[x], "is a number"
   else:
      all_numerical = False
      print num[x], "is not a number"
      
      
if all_numerical:
   print num, "is a number"
   my_int = int(num)
   if my_int % 2 == 0:
      print "This is even"
   else: 
      print "This is odd"
else:
   print num, "is not a number"