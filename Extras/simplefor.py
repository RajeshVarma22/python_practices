s="Rajesh is a good boy"
n=len(s)
i=0
print("frwrd direction")
while i<n:
    print(s[i],end='')
    i+=1
print()
print("back direction")
i=-1
while i>=-n:
    print(s[i],end='')
    i-=1