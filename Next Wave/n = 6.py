n = 5

for i in range(1, n+1):
    if(i == n):
        print((" "*(n)) + str(i))
    else:
        print(((" " * (i-1)) + (str(i)+ " ")) + ((n-i) * "  ")+ str(i))
for i in reversed(range(1, n+1)):
    if(i != n):
        print(((" " * (i-1)) + (str(i)+ " ")) + ((n-i) * "  ")+ str(i))

print()
print()

p = 5
for i in range(1, p+1):
    for j in range(1,i):
        print(" ", end= " ")
    print(i, end=" ")
    for j in range(1, ((2*(p-i))-1-1)):
        print(" ", end=" ")
    if(i != p):
        print(i, end=" ")
    print()
for i in range(p-1, 0,-1):
    for j in range(1,i):
        print(" ", end= " ")
    print(i,end=" ")
    for j in range(1, ((2*(p-i))-1*1)):
        print(" ", end=" ")
    print(i, end=" ")
    print()