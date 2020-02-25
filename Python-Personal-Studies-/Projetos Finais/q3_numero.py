# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 11:19:35 2020

@author: lucas
"""




def fibo (var):
    n2= 1
    n1 = 0
    for i in range(var):
        aux = n2+ n1        
        n1=n2
        n2 = aux
        print (aux) 

fibo(10)
