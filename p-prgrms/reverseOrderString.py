s=input("enter a string:")
l=s.split()
l1=[]
i=len(l)-1
while i>=0:
    l1.append(l[i])
    i=i-1
o=' '.join(l1)
print(o)

