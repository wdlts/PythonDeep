matrix = [[1,2,3,7],[3,4,5,6]]

def transpose(matrix):
    res = []
    n = len(matrix)
    m = len(matrix[0])
    for j in range(m):
        tmp = []
        for i in range(n):
            tmp = tmp + [matrix[i][j]]
        res = res + [tmp]
    matrix[:] = res
    print(res)
    return res
transpose(matrix)