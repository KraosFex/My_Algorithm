def print_formatted(number):
    # your code goes here
    w_s = len(str(bin(number)).replace('0b', ''))
    decim =lambda n: str(n + 1).rjust(w_s)
    octal = lambda n: oct(n + 1).replace('0o', '').rjust(w_s)
    hexad = lambda n: hex(n + 1).replace('0x', '').upper().rjust(w_s)
    binad = lambda n: bin(n + 1).replace('0b', '').rjust(w_s)
    [print(f"{decim(n)} {octal(n)} {hexad(n)} {binad(n)}") for n in range(number)]

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
