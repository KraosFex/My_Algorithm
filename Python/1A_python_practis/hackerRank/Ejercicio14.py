# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

N_shoes = int(input())
shoes_size_list = list(map(int, input().split()))
N_c = int(input())
buys = [input().split() for i in range(N_c)]

total = 0

for buy in buys:
    if int(buy[0]) in Counter(shoes_size_list).keys():
       shoes_size_list.remove(int(buy[0]))
       total += int(buy[1])

print(total)
