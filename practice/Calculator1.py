#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:12:50 2019

@author: cristinamulas
"""

class DescriptiveCalculator:
    def __init__(self, data):
        self.data = data
        self.length = len(data)
        self.total = sum(data)
        self.mean = self.find_mean()
        self.median = self.find_median()
        self.mode = self.find_mode()
        
        
    def find_mean(self):
         return self.total / self.length
         
    def find_median(self):
        sorted_data = sorted(self.data) 
        length = self.length
        num = length // 2
        if length % 2 == 0:
            middlenum = (sorted_data[num]+sorted_data[num - 1]) / 2
        else:
            middlenum = sorted_data[num]
        return middlenum
    
    def find_mode(self):
        num_count = {}
        for i in self.data:
            if i in num_count:
                num_count[i] += 1
            else:
                num_count[i] = 1
        return max(num_count.values())
            
        #from collections import Counter
        #Counter(self.data).most_common(1)
        
    def find_mode(self)
        return(max(set(self),key = self.count))
    def find_var(self):
        mean = self.mean
        return sum([x  - mean] **2 for x in self.data)]         

        










