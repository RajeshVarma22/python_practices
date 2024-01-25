''' find the number of sustrings that get from the main string in clockwise and anti clockwise direction'''
from re import S


S=input("enter the string:")
for i in range(len(S)):
    for j in range(i+1,len(S)+1):
        print(S[i:j])   #print the substring
        


