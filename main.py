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



# A=int(input("First edge's degree: "))
# B=int(input("Second edge's degree: "))
# C=int(input("Third edge's degree: "))
# T=A+B+C
# if T>180:
#   print("Incorrect degree ammount")
# elif T<180:
#   print("Incorrect degre ammount")
# elif A==B and B==C:
#   print("Equal triangle")
# elif A>90 or B>90 or C>90:
#   print("Obtuse triangle")
# elif A==90 or B==90 or C==90:
#   print("Right triangle")
# else:
#   print("Just kinda a triangle")



# D=int(input("Give me number a you please: "))
# if D==1:
#  print("January")
# elif D==2:
#   print("February")
# elif D==3:
#   print("March")
# elif D==4:
#   print("April")
# elif D==5:
#   print("May")
# elif D==6:
#   print("June")
# elif D==7:
#   print("July")
# elif D==8:
#   print("August")
# elif D==9:
#   print("September")
# elif D==10:
#   print("October")
# elif D==11:
#   print("November")
# elif D==12:
#   print("December")
# elif D<1:
#  print("Not a month")
# elif D>12:
#   print("Not a month")



# x=int(input("I'll need a first coordinate (x): "))
# y=int(input("And a second one (y): "))
# if x==0 and y!=0:
#   print("The coordinate is on plane x. Coordinates:", x,y)
# elif x!=0 and y==0:
#   print("The coordinate is on plane y. Coordinates:", x,y)
# elif x==0 and y==0:
#   print("The coordinate is in the middle. Coordinates:", x,y)
# elif x>0 and y>0:
#   print("The coordinate is in the first quadrant. Coordinates:", x,y)
# elif x>0 and y<0:
#   print("The coordinate is in the second quadrant. Coordinates:", x,y)
# elif x<0 and y<0:
#   print("The coordinate is in the third quadrant. Coordinates:", x,y)
# elif x<0 and y>0:
#   print("The coordinate is in the forth quadrant. Coordinates:", x,y)



E=int(input("your numer: "))
if E<0:
  print("It's a negative number.")
  if E<0 and E>-10:
    print("It's single digit.")
  elif E<-9 and E>-100:
    print("It's double digit.")
  elif E<-99 and E>-1000:
    print("It's triple digit.")
  elif E<-999:
    print("Quadruple and more digit numbers")

elif E>0:
  print("It's a pozitive number.")
  if E>0 and E<10:
    print("It's single digit.")
  elif E>9 and E<100:
    print("It's double digit.")
  elif E>99 and E<1000:
    print("It's triple digit.")
  elif E>999:
    print("Quadruple and more digit numbers")
else:
  print("Null")