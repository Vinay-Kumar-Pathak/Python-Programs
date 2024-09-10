#x=[10,20,58,57,30,40,50,70,80]
x = int(input("write any number:"))
#taking divisor
a=int(x/2)
b=int(x/3)
c=int(x/4)
d=int(x/5)
#divisor=int(a,b,c,d)
 

if x % a==0:
    print("yes it is divided by 2")
elif x % b== 0:
    print("yes it is divided by 3")
elif x % c== 0:
    print("yes it is divided by 4")
elif x % d== 0:
     print("yes it is divided by 5")
else :
     print("no it is not divisible by any no")

