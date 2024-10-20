student = {
    "name": "Akanksha",
    "Marks":{
         "phy" :95,
         "chem": 67,
         "maths": 87
    }
}

print(len(student))

print(student.keys())
print(student.values())


print(list(student.keys()))


print(student.items())

list = list(student.items())
print(list[0])

print(student.get("AKanksha"))

# print(student["marks2"]) #--errror

print(student.get("marks2")) #--no-error

student.update({"city":"Delhi"})
print(student)


