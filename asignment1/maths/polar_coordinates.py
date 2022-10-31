complexnumber = complex(input())
import cmath as cm 
phi = cm.phase(complexnumber)
absnum = abs(complexnumber)
print(absnum, '\n', phi)