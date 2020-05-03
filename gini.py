# -*- coding: utf-8 -*-
"""
Created on Sun May  3 00:45:58 2020

@author: kaios
"""

import numpy as np
import math

#input Data

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

#sort Data for annual income
t_sorted = sorted(t, key = lambda annualIncome:annualIncome[2])

#number of data entries
t_rows = len(t)
t_split = []

#annual income in separate array
for i in range(0, t_rows):
    t_split.append(t_sorted[i][2])
    
t_buckets = []    
t_buckets.append(t_split[0] - 5)

#calculate different splits
for i in range(1, t_rows): 
    # print(i)    
    t_buckets.append(math.floor((t_split[i - 1] + t_split[i]) / 2))
    # print(t_buckets)
    
t_buckets.append(t_split[t_rows - 1] + 5) 
# print(t_buckets)
t_gini = []

#count matrix and gini index
for i in range(0, len(t_buckets)):
    count_c1_yes = 0
    count_c1_no = 0
    count_c2_yes = 0
    count_c2_no = 0
    for j in range(0, len(t)):
        if t[j][2] <= t_buckets[i] and t[j][3] == True:
            count_c1_yes += 1
        elif t[j][2] <= t_buckets[i] and t[j][3] == False:
            count_c1_no += 1
        elif t[j][2] >= t_buckets[i] and t[j][3] == True:
            count_c2_yes += 1
        elif t[j][2] >= t_buckets[i] and t[j][3] == False:
            count_c2_no += 1
    ges = count_c1_yes + count_c1_no + count_c2_yes + count_c2_no
    if (count_c1_yes + count_c1_no) == 0:
        n1_gini = 0
    if (count_c2_yes + count_c2_no) == 0:
        n2_gini = 0
    if (count_c1_yes + count_c1_no) != 0:
        n1_gini = 1 - (count_c1_yes/(count_c1_yes + count_c1_no))**2 - (count_c1_no / (count_c1_yes + count_c1_no))**2
    if (count_c2_yes + count_c2_no) != 0:
        n2_gini = 1 - (count_c2_yes/(count_c2_yes + count_c2_no))**2 - (count_c2_no / (count_c2_yes + count_c2_no))**2
    gini = ((count_c1_yes + count_c1_no) / ges) * n1_gini + ((count_c2_yes + count_c2_no) / ges) * n2_gini
    t_gini.append(gini)

t_gini_buckets = np.zeros((len(t_buckets), 2))

#put together splits and gini index
t_gini_buckets[:,0] = t_buckets
t_gini_buckets[:,1] = t_gini

#choose split with lowest gini index
t_gini_buckets = t_gini_buckets[t_gini_buckets[:,1].argsort()]

print("best split: " + str(t_gini_buckets[0][0]))