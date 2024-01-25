# Complete the 'largestCountValue' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#Input from stdin will be processed as follows and passed to the function.

#In the first line, there is a single integer n.
#Each of the following n lines contains
#an integer, arr[i].


def largestCountValue(a):
    # Write your code here
    max_count = 0
    count = 0
    for i in range(len(a)):
        if i == 0:
            max_count = a[i]
        elif a[i] == a[i-1]:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = largestCountValue(a)