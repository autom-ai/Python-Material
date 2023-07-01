# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 14:07:40 2023

@author: Mini Einstein
"""
def largest(num):
    max=num[0]
    for i in num:
        if max < i:
            max=i
    return max
            
        
        