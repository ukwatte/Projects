from termcolor import colored
import re
import sys
pres=0
li=[]
word=sys.argv[1]
m=sys.argv[2]
for match in re.finditer(m,word):
    li.append(word[pres:match.start()])
    li.append(colored(word[match.start():match.end()],'red'))
    pres = match.end()

li.append(word[pres:])
print ''.join(li)

## Example usage
## python regex.py "aabaaha aba" a+b
## this would print the string as is
## but 'aab' and 'ab' would appear red 

