from unicodedata import name


a=("abcdefghijklmnopqrstuvwxyz")
print(type(a))
i=1
j=1
#n=len(s)
name=input("enter a name:")
#n1=name.split(',')
for x in a:
    if i>26:
        i=1
    #print(x,i)
    for y in name:#here instead of for loop write while loop
            #print(y,j)
        if x==y:
            print("s")
            j=j+1
            break
   
        
        
    i=i+1