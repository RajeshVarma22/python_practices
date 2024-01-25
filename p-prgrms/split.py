k,d,x=map(int(input().split()))
x*=2
if d<k:
    d=(k+d-1)/d*d
e=d+k
t=x/e*d
x%=e
if x>k*2:
    t+=k 
    t+=x-k*2
else:
    t+=x/2.0
print(t)
