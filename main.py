from math import *
a=int(input("Unga number: "))
b=int(input("Bubga numeral: "))
c=int(input("Dunga counting symbol: "))
d=b**2-4*a*c
if d<0:
 print("Rootless")
elif d==0:
  x=-b/2*a
  print("one root =",x)
else:
 x1=(-b+sqrt(d))/2*a
 x2=(-b-sqrt(d))/2*a
 print("Two roots 1x =",x1,"2x =",x2)