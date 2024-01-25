'''You are given a string S represnting the beads in clockwise order starting from an arbitary point.
Name=s
type=STRING
return=the function mustreturn a VOID denoting the number of unique final stringd you write down.
input=aba output=3 
input= abcd output=8
input=aabbbbaaaabbbbaaa output=17'''
from re import S


S = input("enter here") 
count = 0
for i in range(len(S)):
    if S[i] == S[i+1]:
        count += 1
print(count)