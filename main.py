# from math import *
# a=int(input("Unga number: "))
# b=int(input("Bubga numeral: "))
# c=int(input("Dunga counting symbol: "))
# d=b**2-4*a*c
# if d<0:
#  print("Rootless")
# elif d==0:
#   x=-b/2*a
#   print("one root =",x)
# else:
#  x1=(-b+sqrt(d))/2*a
#  x2=(-b-sqrt(d))/2*a
#  print("Two roots 1x =",x1,"2x =",x2)



A=int(input("First edge's degree: "))
B=int(input("Second edge's degree: "))
C=int(input("Third edge's degree: "))
T=A+B+C
if T>180:
  print("Incorrect degree ammount")
elif T<180:
  print("Incorrect degre ammount")
elif A==B and B==C:
  print("Equal triangle")
elif A>90 or B>90 or C>90:
  print("Obtuse triangle")
elif A==90 or B==90 or C==90:
  print("Right triangle")
else:
  print("Just kinda a triangle")