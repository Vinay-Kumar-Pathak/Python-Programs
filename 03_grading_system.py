a = int(input("Enter the marks of Hindi(from 100) : "))
if a>100:
    print("Error: Enter The marks from 100")
    exit()

b= int(input("Enter the marks of Eng(from 100)  : "))
if b>100:
    print("Error: Enter The marks from 100")
    exit()

c = int(input("Enter the marks of maths(from 100)  : "))
if c>100:
    print("Error: Enter The marks from 100")
    exit()

d = int(input("Enter the marks of science(from 100)  : "))
if d>100:
    print("Error: Enter The marks from 100")
    exit()


# main Logic
avg=(a+b+c+d)/4

if avg==100:
    print("Grade : O")
elif avg > 90 :
    print("Grade : A+")
elif avg >80:
    print("Grade : A")
elif avg > 70 :
    print("Grade : B+")
elif avg >60:
    print("Grade : B")
elif avg > 50 :
    print("Grade : C")
else:
    print("Grade : F")





