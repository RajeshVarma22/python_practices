s = 'acceenture'


oc = [0] * 27

for i in range(len(s)):
    oc[ord(s[i]) - ord('a')] += 1
  
bc ='a'
br = 0

for i in range(1,27):
    j = chr(i)
    if(oc[i] >= br+1):
        bc = chr(ord('a') + i)
        br = oc[i]

print(bc)