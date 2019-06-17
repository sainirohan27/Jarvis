b=int(input("enter the no."))
a=b
digit_count=0
total=0
while(a!=0):
	a=a//10
	digit_count+=1
print("the no. of digits are\n")
print(digit_count)
print("\n")	
a=b
while(a>10):
	x=a%10
	a=a/10
	a=int(a)
	c=x*x*x
	total=total+c
print(total)
print("\n")	
if(total==b):
	print("armstrong number")	
else:
	print("not armstrong number")	
