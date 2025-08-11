array = [1,2,3,4,5,6,7,8,9,3,4,2]

def create_phone_number(n):
    #your code here
    s = "".join([str(i) for i in n])
    return f"({s[:3]}) {s[3:6]}-{s[6:11]}"

print(create_phone_number(array))