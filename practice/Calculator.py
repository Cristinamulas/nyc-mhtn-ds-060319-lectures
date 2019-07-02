##!/usr/bin/env python2
## -*- coding: utf-8 -*-
#"""
#Created on Thu Mar 14 15:17:35 2019
#
#@author: cristinamulas
#"""
## array
#import numpy as np
#my_list = [1,2,3,4]
#my_arry = np.array(my_list)
#print(my_arry)
#print(type(my_arry))
##create another list
#my_list1 = [7,6,8,9]
#my_list= [my_list , my_list1]
#print(my_list)
##create a nultidimensional array
#my_array2 = np.array(my_list)
#print(my_array2)
#print(my_array2.shape)
#print(my_array2.dtype)
#
#
##how to make an array of zeros
#print(np.zeros(5))
#my_zeros = np.zeros(5)
#print(type(my_zeros))
#print(my_zeros.dtype)
#
##array on ones
#
#my_ones = np.ones([3,4])
#print(my_ones)
#print(my_ones.dtype)
#
##empty array == that zeros
#print(np.empty(5))
#
##IDENTITI MATRIXXXX
#
#print(np.eye(5))
#
### 
#print(np.arange(5)) # pirnt an array of a range of 0 to 4
#
##LETURE 8 use array and scalars
#
#print(5/2)



#def selectionSort(alist):
#   for fillslot in range(len(alist)-1,0,-1):
#       print(fillslot)
#       positionOfMax=0
#       for location in range(1,fillslot+1):
#           print(alist[location])
#           if alist[location]>alist[positionOfMax]:
#               positionOfMax = location
#
#       temp = alist[fillslot]
#       alist[fillslot] = alist[positionOfMax]
#       alist[positionOfMax] = temp
#
#alist = [54,26,93]
#selectionSort(alist)
#print(alist)
#
#
#for i in range(0 , len(alist)-1):
##    print(i)
#    for u in range(1 , len(alist)):
#        print(u)
##            if alist[i] > alist[u]:
##                i+= 1
##print(alist)
##            


#
#arr = [5,4,3,1,6,8,10,9] # array not sorted
#
#for i in range(len(arr))':
#    for j in range(i, len(arr)):
#        print(arr)
#        if(arr[i] > arr[j]):
#            arr[i], arr[j] = arr[j], arr[i]
#
#print arr
#o = range (0,100,4)
#print(o)
#p = o [:: 5]
#print(p)
# 
#
#
#for i in p:



#def sp(a):
#    j = 0
#    while j < len(a)  and a[j] != 'X':
#        j+=1
##        v = a[j] 
##    return v
#a = ['ekejfogo','r' ,'t','X']
#
#print(sp(a))
#import numpy as np
#book = '/Users/cristinamulas/Desktop/readme.txt.rtf'
#
#with open(book, 'r') as fd:
#    words = fd.read().split()
#    words = np.array()
#
#def count_words(word):
#    d = dict()
#    for line in words:
#        if line in d:
#            d[line] = 0
#            d[line] += 1
#    d[line] = d.get(line, 0) + 1
##     d[line] = d[line].items
#            
##
##    print (sorted(d[line]))
#
#
#print(count_words(words))
#def unique (x):
#    c =[]
#    for i in x:
#        if i  not in c:
#            c.append(i)
#    c.sort()
#    return c
#a = [1,2,3,2,3,4,5,6]
#print(unique(a))       
#
#
###OR 
#
#def unique2(l):
#    result = list(set(l))
#    result.sort()
#    return result
#
#a = [1,2,3,2,3,4,5,6]
#print(unique(a)) 
#
#
#def flatt(l):
#    re = []
#    for i in l:
#        if type(i) == list:
#            for y in i:   ## you can use extend intead of this one # re.extende(i)
#                re.append(y)
#        else:
#            re.append(i)
#    return re
#a = [[1,2,3],[4],[5,6],7,8] 
#print(flatt(a))
#    
#    
#    
#def flatt2(l):
#    re = []
#    for i in l:
#        if type (i) == list:
#            re = re + flatt(i)  ## recursion
#        else:
#             re.append(i)
#    return re
            
#            
#range_twenty_four = list(range(0, 25))
#print(range_twenty_four)
#six = list(map(lambda x: x/4.0, range_twenty_four))
#print(six)
#def cscs (l):
#    for i in range(len(l)):
#        result = i/4.0
#    return result    
#    
#a = list(range(0, 25))
#print(cscs(a))  
#a =[ (2, 3), (4, 2)]
#print(a[0])
#    
#    
#def find_term_derivative(term):
#    x = term[0]
#    y = term[1]
#    term_1 =(y * x)
#    term_2 = y -1
#    return term_1, term_2
#def three_x_y_at_one(x):
#    return 3*x*1
#print(three_x_y_at_one(3)) # 9
#
#
#
#
#zero_to_ten = list(range(0, 11))
#zero_to_four = list(range(0, 5))
#
##def y_values_for_at_one(x_values):
##    return list(map(lambda x : three_x_y_at_one(x), x_values))
##print(y_values_for_at_one(zero_to_four))
#def coco (x_values):
#    new = []
#    for i in range(len(x_values)):
#
#
#
#
#
#        new + = three_x_y_at_one(i)
#    return new
#        
#print(coco(zero_to_four))

 #
#def term_output(term, x_value, y_value):
#    return (term[0])*(x_value**term[1])*(y_value**term[2])
#
#
#
#
##def multivariable_output_at(list_of_terms, x_value, y_value):
##    
##    outputs = list(map(lambda term: term_output(term, x_value, y_value), list_of_terms))
##    return sum(outputs)
##
##print(multivariable_output_at(four_x_squared_y_plus_three_x_plus_y, 1, 1))# 8
#
#
#
##def multivariable_output_at(list_of_terms, x_value, y_value):
#    result = []
##using for loop accessing each value in x_values and calling
##three_x_y_at_one and adding result to list result.
#    for value in list_of_terms:
#        temp = term_output(value, x_value, y_value)
#        result.append(temp)
#    return sum(result)

#
#print(multivariable_output_at(four_x_squared_y_plus_three_x_plus_y, 1, 1))

#def term_df_dx(term):
#    return (term[0]*term[1], term[1]-1, term[2])
##
##def df_dx(list_of_terms):
##    filtered_terms = list(filter(lambda x : x[1]!=0, list_of_terms))
##    return list(map(lambda term: term_df_dx(term), filtered_terms))
#
#
#
#
#def df_dx(list_of_terms):
#    result = []
##using for loop accessing each value in x_values and calling
##three_x_y_at_one and adding result to list result.
#    for value in list_of_terms:
#        if value[1] != 0:
#            temp = term_df_dx(value)
#            result.append(temp)
#    return result
#print(df_dx(four_x_squared_y_plus_three_x_plus_y)) 


# def term_output(term, x_value, y_value):
#     return (term[0])*(x_value**term[1])*(y_value**term[2])
#four_x_squared_y_plus_three_x_plus_y = [(4, 2, 1), (3, 1, 0), (1, 0, 1)]
#def multivariable_output_at(list_of_terms, x_value, y_value):
#    result = []
##using for loop accessing each value in 
#    for value in list_of_terms:
#        
#        temp = (value[0])*(x_value**value[1])*(y_value**value[2])
#        result.append(temp)
#    return sum(result)
#
##print(multivariable_output_at(four_x_squared_y_plus_three_x_plus_y, 1, 1)) # 8
#a = [1,2,3,4,5,5,6,66,6,7]
#def lili(l):
#    new = []
#    for i in l:
#        if i not in new:
#            new.append(i)
#    return new
#            
#print(lili(a))
#
#
#def unique (x):
#    c =[]
#    for i in x:
#        if i  not in c:
#            c.append(i)
#    c.sort()
#    return c
#
#print(unique(a))
#
#
#def flatt(l):
#    re = []
#    for i in l:
#        if type(i) == list:
#            for y in i:   ## you can use extend intead of this one # re.extende(i)
#                re.append(y)
#        else:
#            re.append(i)
#    return re
#
#
#
#
#a = [[1,2,3],[4],[5,6],7,8] 
#print(flatt(a))
#
##
#import numpy as np
#import random
#
#def create_array (x,y):
#
#    randon_sample = random.sample(range(x), y)
#    array = np.array(randon_sample)
#    return array
#print(create_array(101,100))


numbers = (1, 2, 3, 4) 
result = map(lambda x: x + x, numbers) 
#print(list(result)) 

def c (x):
    d ={}
    for i in x:
        if i not in d:
            d[i]=1
        else:
            d[i]+= 1
    return d
print(c("aaabcbcccc"))

def v (x):
    d={}
    for k ,v in x.items():
       if v not in d:
           d[v]= k
       else:
           d[v].append(k)
    return d




colors={'sam':'blue',
        2:'yellow',
        'john':'red',
        'peter':'purple'}
print(v(colors))
def ch(x):
    d={}
    for i in x:
        d[i]=d.get(i,0)+1
    return d
print(ch('AAAVCdC'))

