import numpy as np
import scipy
from scipy import stats
import random



a = np.arange(50,150)
for i in range(0,100):
    a[i] = random.randint(-1000,1000)
a = a.reshape(10,10)

def rows(x):
    largest_sum = 0
    largest_mean = 0
    largest_std = 0
    largest_sum_row = -1
    largest_mean_row = -1
    largest_std_row = -1
    for i in range(0,10):
        #Sum
        current_sum = x[i,0]+ x[i,1]+x[i,2]+ x[i,3]+x[i,4]+ x[i,5]+ x[i,6]+ x[i,7]+ x[i,8]+ x[i,9]

        #Mean
        current_mean = current_sum/10

        #Get the sum of the squares of the differences from the mean
        sum_of_squares = 0
        for z in range(0,10):
            sum_of_squares = (x[i,z]-current_mean)**2+sum_of_squares

        #Standard Deviation
        current_std = np.sqrt(sum_of_squares/10)
        if current_sum > largest_sum:
            largest_sum = current_sum
            largest_sum_row = int(i)
        if current_mean > largest_mean:
            largest_mean = current_mean
            largest_mean_row = i
        if current_std > largest_std:
            largest_std = current_std
            largest_std_row = i
    print ("Largest Sum is", largest_sum,"on row", largest_sum_row)
    print ("Largest Mean is", largest_mean,"on row", largest_mean_row)
    print ("Largest Standard Deviation is", largest_std,"on row", largest_std_row)

def cols(x):
    largest_sum = 0
    largest_mean = 0
    largest_std = 0
    largest_sum_col = 0
    largest_mean_col = 0
    largest_std_col = 0
    for i in range(0,10):
        #Sum
        current_sum = x[0,i]+ x[1,i]+x[2,i]+ x[3,i]+x[4,i]+ x[5,i]+ x[6,i]+ x[7,i]+ x[8,i]+ x[9,i]

        #Mean
        current_mean = current_sum/10

        #Get the sum of the squares of the differences from the mean
        sum_of_squares = 0
        for z in range(0,10):
            sum_of_squares = (x[z,i]-current_mean)**2+sum_of_squares

        #Standard Deviation
        current_std = np.sqrt(sum_of_squares/10)
        if current_sum > largest_sum:
            largest_sum = current_sum
            largest_sum_col = i
        if current_mean > largest_mean:
            largest_mean = current_mean
            largest_mean_col = i
        if current_std > largest_std:
            largest_std = current_std
            largest_std_col = i
    print ("Largest Sum is", largest_sum,"on column", largest_sum_col)
    print ("Largest Mean is", largest_mean,"on column", largest_mean_col)
    print ("Largest Standard Deviation is", largest_std,"on column", largest_std_col)

rows(a)
cols(a)
