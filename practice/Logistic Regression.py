#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:58:21 2019

@author: cristinamulas
"""

#class Person:
#    def __init__(self, name, surname):
#        self.name = name
#        self.surname = surname
#        
#    def whole_name (self):
#        return ('{} {}'.format(self.name , self.surname))
#    
#    
#class Male(Person):
#    def __init__(self,gender, name, surname):
#        self.gender = gender
#        
#    def get_gender (self):
#        return self.gender
#    
#class Female(Male):
#   def __init__(self,gender):
#     self.gender = gender
#
#obj_per = Person("Cris","Mulas")
#onj_male = Male("male","Cris","Mulas")
#onj_fe = Female("female")
#print(onj_fe.get_gender())
#print(onj_male.get_gender())
#
#def l (x):
#    d = {}
#    for i in d:
#        if i not in d:
#            d[i]=1
#        else:
#            d[i]+=1
#    return sorted(d)
##            
#print (l("aabebeccc"))
##dic = {}
##s=raw_input()
##for s in s:
##    dic[s] = dic.get(s,0)+1
##print '\n'.join(['%s,%s' % (k, v) for k, v in dic.items()])
#
#a = {'a': 2, 'c': 3, 'b': 2, 'e': 2}
#print(a)
#print(a.get('c',0))
#b = a.items()
#print(b[0])
#print(a.values())
#print(a.keys())


# importing copy module 
import copy 
  
# initializing list 1  
li1 = (1, 2, [3,5], 4)
  
  
# using copy for shallow copy   
li2 = copy.copy(li1)  
  
# using deepcopy for deepcopy   
li3 = copy.deepcopy(li1)  
li3[2][0] = 6


li2[2][0] = 7
print(li1)
print(li2)
print(li3)
#Aliasing both change!!!!


x = [1,2,3]
y = x
print(y.append(4))
print(x)
print(y)

def b (t): 
    t=t[1:]
    return t
m= [1,2,3]
print(b(m))

d={'sam':'blue',
        2:'yellow',
        'john':'red',
        'peter':'purple'}
for k in d.keys():
    print(k)
    
for v in d.values():
    print(v)
    
for k in d.items(): #tuple
    print(k)
    
print(d.keys())

print(d.values())

print(d.items())











