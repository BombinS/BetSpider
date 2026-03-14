#!bin/usr/env python

def getProhability(k):
    result = []
    if len(k) == 2:
        all = 1/k[0] + 1/k[1]
        result.append(round(1/k[0]/all*100,1)) 
        result.append(round(1/k[1]/all*100,1))
        result.append(round(1/all*100,1))
    if len(k) == 3:
        all = 1/k[0] + 1/k[1] + 1/k[2]
        result.append(round(1/k[0]/all*100,1)) 
        result.append(round(1/k[1]/all*100,1))
        result.append(round(1/k[2]/all*100,1))
        result.append(round(1/all*100,1))
    return result

print (getProhability([3.30, 1.33]))
print (getProhability([9.00, 5.40, 1.33]))
print()
print (getProhability([1.85, 2.00]))
print (getProhability([1.85, 3.80, 4.5]))
print()
print (getProhability([1.62, 2.35]))
print (getProhability([3.00, 3.45, 2.35]))
print()
print (getProhability([1.42, 2.95]))
print (getProhability([2.50, 3.20, 2.95]))
print()
