string=input("enter a string:")
n=len(string)
i=0
print("In forward direction")
while i<n:
    print(string[i],end='')
    i=i+1
print()
print("In backward direction")
i=-1
while i>=-n:
    print(string[i],end='')
    i=i-1
print()
#Another way with for loop
i=0
print("In forward direction")
for x in string:
    print(x,end='')
print()
print('forward direction1')
for x in string[::]:
    print(x,end='')
print()
print("In backward direction")
for x in string[::-1]:
    print(x,end='')
print('\n end')
