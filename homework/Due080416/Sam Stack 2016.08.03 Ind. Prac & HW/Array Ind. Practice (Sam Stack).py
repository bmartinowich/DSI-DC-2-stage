# import a randomize and created an array
import random
a_list = random.sample(range(1, 101), 100)
array = np.asarray(a_list)
array = array.reshape(10,10)
array

# iterate through each row and find statistical numbers
for row[:10] in array:
    print np.mean(row)
    print np.std(row)
    print max(row)
    print 
    
#couldn't get this if function to iterate through columns so... I transposed it!
arrayt = np.transpose(array)
arrayt

for row[:10] in arrayt:
    print np.mean(row)
    print np.std(row)
    print max(row)
    print  #this is to sprint a space to makes things look nicer (if you were wondering)
    
# create another random list to make a array out of
b_list = random.sample(range(1,200),100)
array2 = np.asarray(b_list)
array2 = array2.reshape(10,10)
array2

# The screen shut off so im assuming you wanted all of these.
adder = np.add(agay,agay2)
print 'Array plus Array2' 
print adder
print

sub = np.subtract(agay,agay2)
print 'Array minus Array2' 
print sub
print 

dota = np.dot(agay,agay2)
print'Array dotting(?) Array2' 
print dota

