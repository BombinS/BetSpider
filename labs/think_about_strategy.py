#!bin/usr/env python

# [10.6, 17.7, 71.7, 95.4]
#  3.30, 1.33
#  9.00, 5.40, 1.33

print("let do 100 odd by 1000 RUR again favorite")
p1 = 10.6
p2 = 17.7
nwin = round((p1 + p2))
print(f"{p1:.2f} + {p2:.2f} = {(p1 + p2):.2f} ({nwin})")
print(f"we are waiting the {nwin} wins")
print(f"all bets = 100 * 1000 = {100*1000}")
print(f"success = {nwin} * 3.3 * 1000 = {(round(nwin * 3.3 * 1000)):,}") 
print(f"we have {(round(nwin * 3.3 * 1000) - 100*1000):,} rur")