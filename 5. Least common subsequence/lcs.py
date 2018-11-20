#!/usr/bin/env python2
# lcs.py : Maximum length Longest Common Subsequence (LCS)
# Supriya Ayalur Balasubramanian, 14-Oct-2018
# Find longest common subsequence (LCS) of given two sequences, X and Y using bottom up approach of dynamic programming.

# Calculating the length of the LCS
def lenoflcs(X,Y,m,n,c):
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                c[i][j]=0
            elif X[i-1]==Y[j-1]:
                c[i][j]=c[i-1][j-1]+1
            else:
                c[i][j]=max(c[i-1][j], c[i][j-1])
    return c[m][n]    
    
# Printing the LCS.
def print_lcs(i,j,lcs_arr):
    if i==0 or j==0:
        return
    if X[i-1]==Y[j-1]:
        print_lcs(i-1,j-1,lcs_arr)
        lcs_arr.append(X[i-1])
    elif c[i][j-1] >= c[i-1][j]:
        print_lcs(i,j-1,lcs_arr)
    else:
        print_lcs(i-1,j,lcs_arr)
    return lcs_arr
    
# Input arrays
X = ['A','B','C','B','D','A','B']
Y = ['B','D','C','A','B','A']   

#X = [1, 0, 0, 1, 0, 1, 0, 1]
#Y = [0, 1, 0, 1, 1, 0, 1, 1, 0]

# Calculating the length of the input sequence
m=len(X)
n=len(Y)

# Initializing a m*n array c
c=[[0 for x in range(n+1)] for x in range(m+1)]

# Initializing an empty array to store the LCS sequence
lcs_arr=[]

# Calling the function to calculate the maximum length of the LCS
lcs_len=lenoflcs(X,Y,m,n,c)

# Calling the fucntion to print the LCS
lcsarr=print_lcs(m,n,lcs_arr)

# Printing final output 
print 'X:',X
print 'Y:',Y
print 'Length of the LCS is', lcs_len
print 'Longest common subsequence of X and Y is',lcsarr
