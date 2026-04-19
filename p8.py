count = 1

while count <= 5:
    print("Hello World")
    count += 1
    
i = 1
while i <= 5:
    print("Hello World", i)
    i += 1
    
i = 1
while i <= 5:
    print(i)
    i += 1
    
i = 100
while i <= 100:
    print(i)
    i += 1
    
i = 1
while i <= 10:
    print(4*i)
    i += 1
    
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 36, 36]

# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx += 1        

x = 36

i = 0
while i < len(nums):
    if nums[i] == x:    
        print("Found", i)
        break
    else:
        print("finding....")
    i += 1
    

print("loop ended")