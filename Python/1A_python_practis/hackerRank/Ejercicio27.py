import textwrap

def merge_the_tools(string, k):
    # your code goes here
    for t in textwrap.wrap(string, k):
        u = ""
        for i in t:
            if i not in u:
                u += i
        print(u)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
