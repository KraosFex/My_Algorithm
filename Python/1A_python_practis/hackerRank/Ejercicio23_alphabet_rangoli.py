def print_rangoli(size):
    # your code goes here
    w = (size * 2 - 1) * 2 - 1
    al = "abcdefghijklmnopqrstuvwxyz"

    for i in range(size-1,-1,-1):
        a = f"{al[i]}"
        for x in range(i+1,size):
            a = f"{al[x]}-" + a + f"-{al[x]}"
        print(a.center(w,"-"))

    for i in range(1,size):
        a=f"{al[i]}"
        for x in range(i+1,size):
            a= f"{al[x]}-" + a + f"-{al[x]}"
        print(a.center(w,"-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
