print("enter 5 subject marks ")
a=int(input(" "))
b=int(input(" "))
c=int(input(" "))
d=int(input(" "))
e=int(input(" "))
per=(a+b+c+d+e)/5
print("percentage is=",per)
if(per>=90):
 print("The grade is A")
elif(per>80):
 print("The grade is B")
elif(per>70):
 print("The grade is C")
else:
 print("the student fails")