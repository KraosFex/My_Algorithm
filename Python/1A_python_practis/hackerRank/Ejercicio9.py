if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    A = list(arr)
    if n >= 2 and n <=10:
        scoremax = -99 
        scorerunner = -99
        for i in range(n):
            if A[i] >= (-100) and A[i] <= 100:
                if scoremax < A[i]:
                    scorerunner = scoremax
                    scoremax = A[i]
                elif scorerunner < A[i] and A[i] != scoremax:
                    scorerunner = A[i]  
            continue
    print(scorerunner)
