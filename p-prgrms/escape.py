#you are given a positive integer N.
#calculate the sum of the series N + N/2 + N/4 + N/8 + N/16 + ....
#input format : the first line contains an integer N.
#output format : the output contains a single integer denoting the sum of the series.
#sample input :25
#sample output : 
# N/2=12
# N/4 =6
# N/8 =3
# N/16 =1
#sum = N+N/2+N/4+N/8+N/16+.... = 25+12+6+3+1 = 47
from logging import root
import math
from unittest import result


def findSum(N):
    result = 0
    while N > 0:
        result += int(N)
        N = N/2
    return result
N=int(input())
print(findSum(N))