#!/usr/bin/env python2
import timeit
import matplotlib.pyplot as plt

# Brute Force Algorithm begins
def solvebruteforce(arr,l,h):
    if(l==h):
        return(l,h,arr[l]) # checks for the presence of single element in the array
    else:
        (start,end,maxsum)=bf_max_subarray(arr,l,h)
    return(start,end,maxsum)

def bf_max_subarray(array,low,high):
    maxsum=-99999
    start=0
    end=0
    for i in range(low,high):
        subarraysum=0
        for j in range(i,high):
            subarraysum+=array[j]  
            if subarraysum >= maxsum:
                maxsum = subarraysum
                start=i
                end=j
    return(start,end,maxsum)
# Brute Force Algorithm ends


# Divide and Conquer Algorithm begins
# Pseudo code for divide & conquer referred from CLRS textbook, page 70-74
# Finding the sub-array of A[1...mid] and A[mid+1...n]
def solvedivideconquer(arr,l,h):
    if (l==h):
        return(l,h,arr[l]) # checks for the presence of single element in the array
    else:
        mid=int((l+h)/2)
        (left_start,left_end,left_maxsum)=solvedivideconquer(arr,l,mid)
        (right_start,right_end,right_maxsum)=solvedivideconquer(arr,mid+1,h)
        (cross_start,cross_end,cross_maxsum)=dccross_maxsubarray(arr,l,mid,h)
    
    if (left_maxsum >= right_maxsum and left_maxsum >= cross_maxsum):
        return(left_start,left_end,left_maxsum)
    elif (right_maxsum >= left_maxsum and right_maxsum >= cross_maxsum):
        return(right_start,right_end,right_maxsum)
    else:
        return(cross_start,cross_end,cross_maxsum)

#  Finding the maximum sub-array crossing the midpoint.
def dccross_maxsubarray(array,low,mid,high):
    leftmaxsum=-99999
    subarraysum=0
    leftlow=None
    righthigh=None
    for i in range(mid,low,-1):
        subarraysum+=array[i]       
        if subarraysum > leftmaxsum:
            leftmaxsum = subarraysum
            leftlow=i
    
    rightmaxsum=-99999
    subarraysum=0
    for j in range(mid+1,high,1):
        subarraysum+=array[j]
        if subarraysum > rightmaxsum:
            rightmaxsum = subarraysum
            righthigh=j
    
    return(leftlow,righthigh,leftmaxsum+rightmaxsum)
# Divide and Conquer Algorithm ends


# Reading the entire input file
file=open('input.txt','r').readlines()

# Convert the input data from strings to integer data type
array = list(map(int, file))

# Create an empty list to hold the average elapsed time and the number of inputs
input_list=[]
bf_avg_elapsed_time=[]
dc_avg_elapsed_time=[]

# Setting up the array length in the frequency of 500 and
# Filtering out the requisite input data to be sorted from the original array list.
for alen in range(500,10001,500):
    input=array[0:alen]
    print 'Array length is:', alen
    
    # Brute Force Algorithm
    print 'Finding the greatest sum and sub-array by Brute Force...'    
    for i in range(3):
        
        bf_elapsed_time=0
        start_time=timeit.default_timer()
        
        (bfstart,bfend,bfmaxsum)= solvebruteforce(input,0,alen)
        
        stop_time = timeit.default_timer()
        run_time = stop_time - start_time
        bf_elapsed_time=+ run_time
    
    avg_elapsed_time=round((bf_elapsed_time/3),6)

    # Append the time and number of inputs to a list for plotting graphs
    input_list.append(alen)
    bf_avg_elapsed_time.append(avg_elapsed_time)
        
    # Print the maximum sub-array and the greatest sum
    print 'The subarray is: A[',bfstart,'...',bfend,']'
    print 'Greatest sum of first',alen,'numbers is:',bfmaxsum,'\n'
        

    # Divide and Conquer Algorithm
    print 'Finding the greatest sum and sub-array by Divide and Conquer...'
    for i in range(3):
        
        elapsed_time=0
        start_time=timeit.default_timer()
        
        (dcstart,dcend,dcmaxsum)= solvedivideconquer(array,0,alen)
        
        stop_time = timeit.default_timer()
        run_time = stop_time - start_time
        dc_elapsed_time=+ run_time
    
    avg_elapsed_time=round((dc_elapsed_time/3),6)

    # Append the time and number of inputs to a list for plotting graphs
    dc_avg_elapsed_time.append(avg_elapsed_time) 
    
    # Print the maximum sub-array and the greatest sum
    print 'Max subarray is: A[',dcstart,'...',dcend,']'
    print 'Greatest sum of first',alen,'numbers is:',dcmaxsum,'\n\n'


# Plotting the graph. Defining the x-axis and y-axis data and labels to plot the graph
x=input_list
y1=bf_avg_elapsed_time
y2=dc_avg_elapsed_time

# Referred to the below website on how to plot two graphs in one.
# https://stackoverflow.com/questions/22276066/how-to-plot-multiple-functions-on-the-same-figure-in-matplotlib
# https://stackoverflow.com/questions/19125722/adding-a-legend-to-pyplot-in-matplotlib-in-the-most-simple-manner-possible
plt.plot(x, y1, 'r',label='Brute Force') # plotting the brute force graph separately 
plt.plot(x, y2, 'b',label='Divide and Conquer') # plotting the divide & conquer graph separately 
plt.legend(loc='upper left')
plt.xlabel('Number of Inputs')
plt.ylabel('Time taken')
plt.title('Running time versus the number of inputs')
plt.show()