x = open('CivicsTrimesterFinal.txt', 'r')
print x

words2 = 0

for i in x:
    words = i.split()
    words2 += len(words)
    
print words2