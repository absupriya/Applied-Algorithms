import heapq
from operator import itemgetter

# Defining the node class
class Node:
    def __init__(self):
        self.freq=None
        self.char=None
        self.left=None
        self.right=None
        
# Huffman Algorithm
def huffman(C):
    n=len(C)
    for i in range(0,n-1):
        z=Node()
        x=Node()
        y=Node()
        a=heapq.heappop(Q)
        b=heapq.heappop(Q)
        x.freq=a[0]
        x.char=a[1].char
        y.freq=b[0]
        y.char=b[1].char
        z.freq=x.freq+y.freq
        z.char=x.char+y.char
        x.left=a[1].left
        x.right=a[1].right
        y.left=b[1].left
        y.right=b[1].right
        z.left=x
        z.right=y
        heapq.heappush(Q,(z.freq, z))                                                                                                   
     
# Print Huffman Tree
def traverseTree(node,bit):
    if node.left is None and node.right is None:
        print node.char, bit
        traversetree.append((node.char,bit))
    else:
        traverseTree(node.left, bit + '0')
        traverseTree(node.right, bit + '1')	

# Intializing an array with the 32 characters.
C = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ",".",",","?","!","\'"]

# reading the text file 
f=open("WestLondonStreet.txt","r")
l=f.readlines()

# Initializing the dictionary with the characters frequency = 0
chardict={}
for char in C:
    chardict[char]=0

# Calculating frequency of each character in the file.
for line in l:
    for c in line:
        char=c.lower()
        if char in C:
            if char in chardict:
              chardict[char]+=1
            else:
              chardict[char]=1

# print the frequencies
print '\nFrequencies:\n',chardict,'\n'
       
Q = []
for c in C:
    my_node = Node()
    my_node.char = c
    heapq.heappush(Q, (chardict[c], my_node))

# Changing the key attribute to frequency and sorting
sortonchar=sorted([(value,key) for (key,value) in chardict.items()], key=itemgetter(1))

# Invoking Huffman algorithm
huffman(C)

# Print Huffman code with intial call.
traversetree=[]
initialnode = heapq.heappop(Q)
root_node = initialnode[1]
traverseTree(root_node, '')

# Calculations of the number of bits saved. Discussion part
# Count of each character
charcount=(zip(*sortonchar)[0])

# frequency of bits
charcode_tuple=sorted(traversetree)
charcode_freq=(zip(*charcode_tuple)[1])

# Length of the character frequency
charcode_freq_len=[len(y) for y in charcode_freq]

# Length of the variable bit frequency
varbitfreq=[i*j for i,j in zip(charcode_freq_len,charcount)]
total_varbitfreq=sum(varbitfreq)

# Print bits saved - Discussion questions
fixedbitencoding= sum(i*5 for i in charcount)
print '\nThe text was encoded using', total_varbitfreq,'bits.'
print 'The text had', sum(charcount), 'valid characters.'
print 'Using a 5-bit fixed length encoding, this would have been', fixedbitencoding,'bits long.'
print 'So, we saved', fixedbitencoding-total_varbitfreq, 'bits!'