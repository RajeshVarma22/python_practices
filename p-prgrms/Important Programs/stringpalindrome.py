string = "aaacca" 
#         tdgbcba
# string2 = reversed(string)
l = ""

for x in range(len(string)):
    for i in string:
        m = string.find(i)
        print("m : ",m)
        pal = string[x:m]
        revpal = pal[::-1]
        print("pal:" , pal)
        print("revpal:" , revpal)
        if(pal == revpal):
            print("yessssss")


