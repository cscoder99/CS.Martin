x = raw_input("Enter a decimal: ")
print x

n = 0

for i in x:
    if i == '.':
        print "Found a decimal"
        break
    # n = 1 as of right now
    n = n + 1
    hundreths = int(x[n+2])
    
    