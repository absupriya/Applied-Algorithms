#!/usr/bin/env python2
  
# Find median of the given array of 5 elements. 
# First the array is sorted using insertion sort and median is calculated.
def findMedian(arr):
    
# Insertion sort
    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]: 
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    
# Finding the mid position to return the median
    if len(arr)%2==0:
        mid=(len(arr)/2)-1
    else:
        mid=len(arr)/2
    return(arr[mid])

# Divide arr[] in groups of size 5, calculate median of every group and store it in median[] array. 
def divide(arr, l, r):
    n = r-l+1
    median=[]
    for i in range(0,n,5):
        median.append(findMedian(arr[i:(i+5)]))

# Find median of all medians using recursive call. 
# If median[] has only one element, then no need of recursive call 
    if len(median)==1:
        medofMed = median[0]
    else:
        medofMed = divide(median, 0, len(median)-1)
            
    return(medofMed)


# Generate a random array of numbers.
#import random
#arr=[]
#for x in range(1000):
#    arr.append(random.randint(1,5001))

# Read the given input file.
file=open('input.txt','r').readlines()
# Convert the input data from strings to integer data type
arr = list(map(int, file))

n = len(arr)
print '\nLength of the array:', n
median=divide(arr, 0, n-1)
print '\nMedian of medians is:',median