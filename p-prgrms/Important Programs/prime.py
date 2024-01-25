value = 1500
a1 = []
a2 = []
for number in range (value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            a1.append(number)  

n = 1500
for i in range(2 , n+1) :
    if i == 2 :
        a2.append(i)
    elif(i % 2 != 0):
        yes = 1
        for j in range(2,i+1):
            if (i % j == 0):
                yes -= 1
                if((yes == 0) and (i == j)):
                    a2.append(i)
                    
print(a1)
print(a2)
if(a1 == a2):
    print("Yes")
else:
    print("No")