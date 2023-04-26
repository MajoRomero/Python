# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 09:45:16 2023

@author: Usuario
"""
def isYearLeap(year):
    return ((year %4==0 )and (year %100 !=0 ) or (year %400==0));

def daysinMoth(year,month):
    if month in [1,3,5,7,8,10,12]:
        return(31)
    if isYearLeap(year)==True:
        if month==2:
            return(29)
    if isYearLeap(year)==False:
        if month==2:
            return(28)
        else:
            return (30)  
testYears=[1900,2000,2016,1987]
testMonths=[2,2,1,11]
testResults=[28,29,31,30]

for i in range (len(testYears)):
    yr=testYears[i]
    mo=testMonths[i]
    result= daysinMoth(yr, mo)
    print(yr,mo,"->",end="")
    if result==testResults[i]:
        print("Ok")
    else:
        print("Failed")