from operator import le


n=[[10,4,20,30],[40,50,60],[70,80,90]]
for i in range(len(n)):
    print(len(n[i]))
    for j in range (len(n[i])):
        print(n[i][j],end=" ")
    print()
    