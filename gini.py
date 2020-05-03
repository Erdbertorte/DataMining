# -*- coding: utf-8 -*-
"""
Created on Sun May  3 00:45:58 2020

@author: kaios
"""

import numpy as np
import math

t = [[True, "Single", 125, False],
     [False, "Married", 100, False],
     [False, "Single", 70, False],
     [True, "Married", 120, False],
     [False, "Divorced", 95, True],
     [False, "Married", 60, False],
     [True, "Divorced", 220, False],
     [False, "Single", 85, True],
     [False, "Married", 75, False],
     [False, "Single", 90, True]]

t_sorted = sorted(t, key = lambda annualIncome:annualIncome[2])



t_rows = len(t)
t_split = []


for i in range(0, t_rows):
    t_split.append(t_sorted[i][2])
    
t_buckets = []
    
t_buckets.append(t_split[0] - 5)

for i in range(1, t_rows): 
    print(i)
    print(t_buckets)
    t_buckets.append(math.floor((t_split[i - 1] + t_split[i]) / 2))
    
t_buckets.append(t_split[t_rows - 1] + 5) 

for i in range(0, t_rows):
    