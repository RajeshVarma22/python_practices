n = int(input())
left_spaces = n - 1
print(left_spaces * " " + "*")
hollow_spaces_count = -1
for i in range(2 , n + 1):
    left_spaces = n - i
    hollow_spaces_count = hollow_spaces_count + 2
    print(left_spaces * " " + "*" + hollow_spaces_count * " " + "*")
for j in range(1 , n-1):
    left_spaces = j
    hollow_spaces_count = hollow_spaces_count  - 2
    print(left_spaces * " " + "*" + hollow_spaces_count * " " + "*")
left_spaces = n - 1
print(left_spaces * " " + "*")