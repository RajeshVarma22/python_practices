# Complete the 'maxEnergy' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY mat as parameter.
#

def maxEnergy(mat):
    # Write your code here
    max_energy = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i == 0 and j == 0:
                max_energy = mat[i][j]
            elif i == 0:
                max_energy = max(max_energy, mat[i][j])
            elif j == 0:
                max_energy = max(max_energy, mat[i][j])
            else:
                max_energy = max(max_energy, mat[i][j] + min(mat[i-1][j], mat[i][j-1]))
    return max_energy   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    mat_rows = int(input().strip())
    mat_columns = int(input().strip())

    mat = []

    for _ in range(mat_rows):
        mat.append(list(map(int, input().rstrip().split())))

    result = maxEnergy(mat)

    fptr.write(str(result) + '\n')

    fptr.close()