#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 20:48:26 2018

@author: pineapple
"""

T = 4
import numpy as np
for i in range(T):
    a = np.random.randn(1)
    if a >= 0:
        print 'Yes'
    else:
        print 'No'
        
import numpy as np        
np.random.randn(1)
