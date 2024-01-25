# In comparision of strings it will take in alpabetical oreder ex b and a then b>a
s1=input("enter 1st string:")
s2=input('enter 2nd string:')
if s1==s2:
    print("both strings are equal")
elif s1>s2:
    print('1st string is greater than second')
elif s2>s1:
    print('second string is gretater than first string')
elif s1>=s2:
    print("1st>=2nd")
else:
    print("1st<=2nd")