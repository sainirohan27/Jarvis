print("enter the no. of terms")
a=int(input(""))
print("2\n")

x=1
y=2
print_count=0
#for i in range(2,a):
while(print_count<a-1):
	z=x+y
	primecount=0	
	i=1
		
	for i in range (3 , a):
		if(a%i==0):
			primecount=primecount+1

	if(primecount is 0):	     
		print(z)
		print("\n")
		print_count+=1   

	x=y
	y=z

 
