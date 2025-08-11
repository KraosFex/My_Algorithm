# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
# print([(x,y) for x in list_a for y in list_b])
print(" ".join(["".join(str(i)) for i in list(product(list_a, list_b))]))
