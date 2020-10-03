# This is the solution of fibonacci series without using recusion.
print("enter the no. of terms")
a=int(input(""))
print("0\n1\n2\n")

x=1
y=2
for i in range(2,a):
	z=x+y
	print(z)
	print("\n")
	x=y
	y=z

 
