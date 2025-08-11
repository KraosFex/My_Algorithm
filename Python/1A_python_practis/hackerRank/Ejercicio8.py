if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    permutation_list  =[]
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if n == i + j + k:
                    continue
                permutation_list.append([i,j,k])
    print(permutation_list)
