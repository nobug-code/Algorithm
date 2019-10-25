def solution(A):
    #A is matrix
    saddle = 0

    for i in range(len(A)):
        for j in range(len(A[0])):
            max_flag = find_max_saddle(i, j, A)
            min_flag = find_min_saddle(i, j, A)
            if (max_flag or min_flag):
                saddle += 1

    return saddle


def find_min_saddle(i, j, A):
    if (i > 0 and i < len(A) - 1 and j > 0 and j < len(A) - 1):
        if(A[i][j-1] > A[i][j] and A[i][j] < A[i][j+1]
                and A[i-1][j] < A[i][j] and A[i][j] > A[i+1][j]):
            return True
        else:
            return False

    else:
        return False


def find_max_saddle(i, j, A):

    if(i > 0 and i < len(A) -1 and j > 0 and j < len(A) - 1):
        if (A[i][j - 1] < A[i][j] and A[i][j] > A[i][j + 1]
                    and A[i - 1][j] > A[i][j] and A[i][j] < A[i + 1][j]):
            return True
        else:
            return False
    else:
        return False


A = [[0,1,3], [5,2,5], [4,1,1]]

print(solution(A))