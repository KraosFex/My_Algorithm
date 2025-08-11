arr1 = [1, 1, 2]
arr2 = [17, 17, 3, 17, 17, 17, 17]

def stray(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x

#esta opcion me parece muuuy comprimida
def stray(arr):
    # esto no lo entiendo
    return [num for num in arr if arr.count(num) == 1][0]

print(stray(arr2))