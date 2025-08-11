if __name__ == '__main__':
    s = input()
    cont_ad = cont_a = cont_l = cont_u = cont_d = 0
    for i in range(len(s)):
        if s[i].isalnum():
            cont_ad += 1
            if s[i].isalpha():
                cont_a += 1
                if s[i].islower():
                    cont_l += 1
                elif s[i].isupper():
                    cont_u += 1
                    continue
            elif s[i].isdigit():
                cont_d += 1

    print(True if cont_ad > 0 else False)
    print(True if cont_a > 0 else False)
    print(True if cont_d > 0 else False)
    print(True if cont_l > 0 else False)
    print(True if cont_u > 0 else False)

