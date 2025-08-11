# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

arr_str = input().split()

list_p = ["".join(i) for i in list(permutations(arr_str[0], int(arr_str[1])))]

[print(i) for i in sorted(list_p)]

