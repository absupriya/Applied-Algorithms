#!/usr/bin/env python2
import timeit
import matplotlib.pyplot as plt

# Merge Sort Algorithm begins
# Pseudo code for merge sort referred from CLRS textbook, page 30-34
# Finding the sub-array of A[1...mid] and A[mid+1...n]
def solvemergesort(A,l,h):
    if l < h:
        mid=int((l+h)/2)
        solvemergesort(A,l,mid)
        solvemergesort(A,mid+1,h)
        solvemerge(A,l,mid,h)
    

#  Merge the sub-array and place them in the final sorted array.
def solvemerge(array,low,mid,high):
# finding the length of the two sub-arrays
    n1=mid-low+1
    n2=high-mid
    
# Initializing the left and right arrays
    left_array=[0]*(n1+1)
    right_array=[0]*(n2+1)
    
# Copy the data into the left and right sub-arrays
    for i in range(n1):
        left_array[i]=array[low+i]
    for j in range(n2):
        right_array[j]=array[mid+j+1]
        
# Merge the sub-arrays into the array
    i=0
    j=0
    left_array[n1]=float("inf")
    right_array[n2]=float("inf")

    for k in range(low, high+1):
        if left_array[i] < right_array[j]:
            array[k] = left_array[i]
            i+=1
        else:
            array[k] = right_array[j]
            j+=1

# Reading the entire input file
file=open('input.txt','r').readlines()

# Convert the input data from strings to integer data type
array = list(map(int, file))
alen=len(array)

# Create an empty list to hold the average elapsed time and the number of inputs
input_list=[]
ms_avg_elapsed_time=[]

# Setting up the array length in the frequency of 500 and
# Filtering out the requisite input data to be sorted from the original array list.
for alen in range(5000,100001,5000):
    input=array[0:alen]
    #print 'Array length is:', alen   

    # Merge Sort Algorithm
    for i in range(3):
        ms_elapsed_time=0
        start_time=timeit.default_timer()
        
        solvemergesort(input,0,alen-1)
        
        stop_time = timeit.default_timer()
        run_time = stop_time - start_time
        ms_elapsed_time=+ run_time
        #print ms_elapsed_time
    
    avg_elapsed_time=round((ms_elapsed_time/3),6)
    
# Append the time and number of inputs to a list for plotting graphs
    input_list.append(alen)
    ms_avg_elapsed_time.append(avg_elapsed_time)

# Plotting the graph. Defining the x-axis and y-axis data and labels to plot the graph
x=input_list
y=ms_avg_elapsed_time
plt.plot(x, y, 'r',label='Merge Sort')
plt.legend(loc='upper left')
plt.xlabel('Number of Inputs')
plt.ylabel('Time taken')
plt.title('Running time versus the number of inputs')
plt.show()