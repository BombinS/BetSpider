#!bin/usr/env python

def getProhability(k):
    result = []
    if len(k) == 2:
        all = 1/k[0] + 1/k[1]
        result.append(1/k[0]/all) 
        result.append(1/k[1]/all)
    if len(k) == 3:
        all = 1/k[0] + 1/k[1] + 1/k[2]
        result.append(1/k[0]/all) 
        result.append(1/k[1]/all)
        result.append(1/k[2]/all)
    return result

print (getProhability([1.85, 1.85]))
print (getProhability([9, 5.2, 1.35]))
print (getProhability([1.85, 3.8, 4.5]))
print (getProhability([3, 3.45, 2.35]))
