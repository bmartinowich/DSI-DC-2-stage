import numpy
import string

def parse_string(x):
    print x
    result = {}
    #Keeps track of how many keys with lowercase vowels and consanants
    length = 0
    for i in x:
        if type(i) != str:
            x[i] = 'delete'
        elif i[0] in 'aeiou':
            x[i] = 'vowel'
            length +=1
        elif i[0] in 'bcdfghjklmnpqrstvwxyz':
            x[i] = 'consonant'
            length +=1
        else:
            x[i] = 'delete'

    for key, value in x.items():
        if value != 'delete':
            result[key]= value

    print result
    return result

x ={ 'red':'blue', 'dog':"cat", 'espn':'asdf', 1:2}
parse_string(x)
