age = 21

if(age >= 18):
    print("can vote and apply for license")
    
    
light = "green"

if(light == "red"):
    print("stop")

if(light == "green"):
    print("go")

if(light == "yellow"):
    print("look")
    
    
num = 5

if(num > 2):
    print("greater than 2")

elif(num > 3):
    print("greater than 3")
    
    
marks = int(input("enter marks: "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"

else:
    grade = "D"
    
print("grade of the student ->", grade)

age = 34

if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")
    
num = int(input("enter number: "))


if(num % 2 == 0):
    print("EVEN")
else:
    print("ODD")
    
x = int(input("enter number: "))

if(x % 5 == 0):
    print("multiple of 5")
else:
    print("not a multiple of 7")

print("end of code")