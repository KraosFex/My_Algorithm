import textwrap
# Enter your code here. Read input from STDIN. Print output to STDOUT
size = list(map(int, input().split()))

H = size[0]
W = size[1]

x = "-"
y = ".|."
z = "WELCOME"

# top door
for i in range(H // 2):
    # print("\n".join(textwrap.wrap(f"{x*((W//2)*H)}", W)))
    # print(x*((W//2)-i) + y*(i+1) + x*((W//2)-i))
    print(x*((W // 2) - 1 - i * 3) + y*(i + 1) + y*i + x*((W // 2) - 1 - i * 3))

# middle door
print(z.center(W, '-'))

#botton door
for i in range(H // 2): 
     print(x*((i + 1) * 3) + y*((W // 2)-i) + y*((W // 2) - i - 1) + x*((i + 1) * 3))

