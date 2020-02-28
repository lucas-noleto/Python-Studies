# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 06:15:17 2020

@author: lucas
"""

altura = float(input("Digite a altura: "))
largura =  float(input ("Digite a largura: "))
preco = float(input("Preço da telha: "))

area = altura * largura
x = area*preco

print ("Custo: %1.2f" %(x))