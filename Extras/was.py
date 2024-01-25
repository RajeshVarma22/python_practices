n = 3
for i in range (n):
     m = n 
     a = 1
     for j in range(a,m+1):
          print(j , end = "")
          if(j != 1 and j % n == 0):
               m += n
               a += n