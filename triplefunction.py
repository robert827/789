# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 16:06:46 2021

@author: AMD_PC
"""

from itertools import combinations as comb
from itertools import product as prod
from scipy.stats import stats
import pandas as pd
import numpy as np
df = pd.read_excel('data.xlsx', index_col=False)
g = df['green']
b = df['blue']
r = df['red']
e = df['rededge']
n = df['nir']
# 種類跟數量
substance = 'TP'
#substance = input("代測物質:")
substance = df[substance]

def triple_plus(n1, n2, n3):
    value = n1+n2+n3
    p = stats.pearsonr(value, substance)
    return abs(p[0])
def remove_punctuation(str):
    '''(str) -> str 
    Return s with all non-space or non-alphanumeric 
    characters removed. 
    >>> remove_punctuation('a, b, c, 3!!') 
    'a b c 3' 
    '''
    punctuation = " ',()"
    no_punct = ""
    for c in str:
        if c not in punctuation:
            no_punct += c
    return(no_punct)

sequence = list(prod('bgrne', repeat=3))

#可行的
test = [b, g, r]
value = triple_plus(test[0], test[1], test[2])
#%%
#不可行的
def remove_punctuation(str):
    '''(str) -> str 
    Return s with all non-space or non-alphanumeric 
    characters removed. 
    >>> remove_punctuation('a, b, c, 3!!') 
    'a b c 3' 
    '''
    punctuation = " '"
    no_punct = ""
    for c in str:
        if c not in punctuation:
            no_punct += c
    return(no_punct)
zxc = sequence[47]
zxcv = remove_punctuation(str(zxc))
print(zxcv)

zxcv_value=triple_plus(zxcv[0],zxcv[1],zxcv[2])