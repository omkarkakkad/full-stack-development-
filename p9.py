i = 0
while i <= 5:
    print(i)
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1
    
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
 
for val in nums:
    print(val)

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

for val in tup:
    print(val)  

str = "Hello World"

for char in str:
    if(char == "o"):
        print("found o")
        break
    print(char)
else:
    print("end")

nums = (    1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36

idx = 0
for el in nums:
    if el == x:
        print("Found", idx)
        idx += 1


print(range(10))

for i in range(10):
    print(i)
    
for i in range(2, 100, 2)  :
    print(i)

for i in range(5):
    pass
print("loop ended")
 