#Reading the entire input file
orig_file=open('input.txt','r').readlines()

#Convert the input data from strings to integer data type
orig_file = list(map(int, orig_file))

#Create an empty list to hold the average elapsed time and the number of inputs
avg_elap_time_list=[]
num_of_inputs_to_sort=[]

#Setting up the array length in the frequency of 500
for alen in range(500,10001,500):
        
    #Filtering out the requisite input data to be sorted from the original array list.
    file=orig_file[0:alen]
    
    #Running the algorithm to run for the same input data 3 times.
    for runs in range(3):
        elapsed_time=0
        
        #Calculation of the running time. 
        """Below 2 lines of code to calculate the running time was referred to in the website 
        https://stackoverflow.com/questions/15707056/get-time-of-execution-of-a-block-of-code-in-python-2-7"""
        import timeit
        start_time = timeit.default_timer()
        
        #Bubble sort begins
        
        #Reading through the entire array of numbers
        for i in range(0,alen):
            
            #Reading through the array list from the end
            for j in range(alen-1,i,-1):
                if file[j] < file[j-1]:
                    file[j], file[j-1] = file[j-1], file[j]
        
        #Bubble sort ends
        
        #Calculating the elapsed time
        stop_time = timeit.default_timer()
        run_time = stop_time - start_time
        elapsed_time=+ run_time
        
    #Calculate the average elapsed time for each iterations
    avg_elapsed_time=round((elapsed_time/3),6)
    
    #Append the time and number of inputs to a list for plotting graphs
    avg_elap_time_list.append(avg_elapsed_time)
    num_of_inputs_to_sort.append(alen)

#importing pyplot package from matplotlib library. 
"""Below code to plot the graph was referred to in the website 
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot"""

import matplotlib.pyplot as plt

#Defining the x-axis and y-axis data and labels to plot the graph
x=num_of_inputs_to_sort
y=avg_elap_time_list
plt.plot(x, y,'r')
plt.xlabel('Number of Inputs')
plt.ylabel('Time')
plt.title("Bubble sort running time versus the number of inputs")
plt.show()