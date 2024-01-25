# List Basics
# list_a = [] # Empty List
# print(type(list_a)) # Class List
# list_a = ['Rajesh Vrma', 'Gireesh Varma']

# A list can contain different datatype slike int str and float

# list_b = [22, 'march', '2000', 22.9, True]
# print(list_b) 
# print(len(list_b)) # 5

# # Accessing list items
# print(type(list_b[-1])) #Boolean

# # Iterating over the list
# for item in list_b:
#     print(item,type(item))

# List concatination 
# list_c = list_a + list_b
# print(list_c) # ['Rajesh Vrma', 'Gireesh Varma', 22, 'march', '2000', 22.9, True]

# Repetition in lists
# list_d = [1 , 2 , 3 , 4 , 5]
# print(list_d * 2) # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# convert to list
# name = 'Rajesh Varma'
# print(list(name)) # ['R', 'a', 'j', 'e', 's', 'h', ' ', 'V', 'a', 'r', 'm', 'a']

# List by range

# list_e = list(range(20,30))
# print(list_e) # [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

list_f = list(range(3,20,3))
print(list_f) # [3, 6, 9, 12, 15, 18]

print(type(str(list_f))) # <class 'str'>
