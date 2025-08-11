if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
       a.append(str(i + 1))
    print(int("".join(a)))
