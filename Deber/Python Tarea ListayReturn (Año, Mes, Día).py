# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 10:14:06 2023

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

def daysinMoth(year,month):
    if year<46 or month<1 or month>12:#46 comienzo de conteo de años 
    #1582 no existió del 5-14 de octubre por ejemplo en España
    #1929 la adopción completa de todos los paises como Inglaterra del calendario gregoriano
        return None
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    res= days[month-1]
    if month == 2 and isYearLeap(year):
        res=29
    return res

def dayofYear(year,month,day):
    days=0
    for i in range(1,month):
        slista=daysinMoth(year, i)
        if slista == None:
            return None
        days +=slista
    slista=daysinMoth(year, month)
    if day >=1 and day <=slista:
        return days + day
    else:
        return None
print(dayofYear(1580,12,31))
