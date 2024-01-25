S1="a?c"
S2="??b"

mindiff = 1
maxdiff = 0

for i in range(len(S1)):
    if (S1[i] == '?' or S2[i] == '?'):
        mindiff += 1
    elif(S1[i] != S2[i]):
        maxdiff += 1
        mindiff += 1

print(maxdiff, mindiff)



