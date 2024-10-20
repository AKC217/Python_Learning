#print no 1-100

i=1

while i<=100:
    print(i)
    i+=1

print("loop ended")

print("------------------------------------------------------------------")

#print no 100-1

i=100

while i>=1:
    print(i)
    i-=1

print("loop ended")


print("------------------------------------------------------------------")
#print the multiplication table of a no 

n= int(input("Enter no: "))
i = 1

while i<=10:
    print(i*n)
    i+=1

print("loop ended")

print("------------------------------------------------------------------")
####print the elements of the following list using loop
list = [1,4,9,16,25,36,49,64,81,100]

i = 0

while i<len(list):
    print(list[i])
    i+=1

print("loop ended")

print("------------------------------------------------------------------")
##Search for a maximum no X in the tuple of the folowing list using loop
list = [1,4,9,16,25,5606,49,64,81,100]


i = 0
x = list[0]

while i<len(list):
      if(list[i] > x):
          x =list[i]

      i+=1
     

print(x)

print("------------------------------------------------------------------")
##Search for a no x in tuple
list = [1,4,9,16,25,5606,49,64,81,100]


i = 0
x = 49
idx = 0

while i<len(list):
      if(list[i] == x):
          idx = i
          break
      else:
           i+=1

print(idx)

print("------------------------------------------------------------------")

##print the no of lkist using for loop
list =[1,4,9,16,25,36,49,64,81,100]

for el in list:
     print(el)

print("------------------------------------------------------------------")

##Search for a no in list with loop
list =[1,4,9,16,25,36,49,64,81,100]

i = 0
x = 25
for el in list:
     if(el == x):
           print(i)
           break
     else:
          i+=1
     

