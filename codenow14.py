x = open('IOPoetryProject-OrtechoRichard (1).txt', 'r')
print x

z = x.read().split()

replacer = {'dream':'fantasy',
            'O God!':'O Heavens',
            'I ':'Jeo'}

new_word = ''
for i in z:
    new_word+=replacer[i]    
    
print new_word