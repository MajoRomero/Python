# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 14:03:40 2023

@author: Usuario
"""
def isYearLeap(year):
    if(year %4)==0:
        if(year %100)==0:
            if(year %400)==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
testData=[1900,2000,2016,1987]
testResults=[False,True,True,False]
for i in range (len(testData)):
    yr=testData[i]
    result=isYearLeap(yr)
    print(yr,"->",end="")
    if result==testResults[i]:
        print("Ok")
    else:
        print("Failed")
        