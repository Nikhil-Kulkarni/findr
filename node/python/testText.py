import sys, string, re

# command line arguments
file = "C:\HackNash\Tomo.txt"
target = "egg"
#window = int(sys.argv[3])

a = open(file)
text = a.read() 
a.close()

tokens = text.split() # split on whitespace
keyword = re.compile(target, re.IGNORECASE)

for index in range( len(tokens) ):
    if keyword.match( tokens[index] ):
        start = max(0, index)
        finish = min(len(tokens), index+1)
        lhs = string.join( tokens[start:index] )
        rhs = string.join( tokens[index+1:finish] )
        print (lhs, tokens[index], rhs, index)