collection = {1, 2 , 2, 3, 3 ,4 ,5}

print(collection)

print(type(collection))

print(len(collection))


collection = set()
print(type(collection))

collection = {1, 2, 3, 4, 5}
print(collection.pop())
print(collection.pop())

values = {9, 9.0, 9.25, 8.25, 8.0, 8.0}
print(values)

values = {
    ("float", 9.0,
     ("int", 9))
}

print(values)

marks = {}

x = int(input("enter phy: "))
marks.update({" phy" : x})

x = int(input("enter chem: "))
marks.update({" chem" : x})

x = int(input("enter maths: "))
marks.update({" maths" : x})

print(marks)

