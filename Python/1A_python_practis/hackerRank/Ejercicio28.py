import numpy

arr_control = list(map(int, input().split()))

arr_a = []
for i in range(arr_control[0]):
    arr_a.append(list(map(int, input().split())))

arr_b = []
for i in range(arr_control[0]):
    arr_b.append(list(map(int, input().split())))

add_t, sub_t, mul_t, div_t, mod_t, pow_t = "", "", "", "", "", ""
for i in range(arr_control[0]):
    a = numpy.array(arr_a[i], int)
    b = numpy.array(arr_b[i], int)
    add_t += f" {numpy.add(a, b)}\n"
    sub_t += f" {numpy.subtract(a, b)}\n"
    mul_t += f" {numpy.multiply(a, b)}\n"
    div_t += f" {numpy.floor_divide(a, b)}\n"
    mod_t += f" {numpy.mod(a, b)}\n"
    pow_t += f" {numpy.power(a, b)}\n"

print(f"[{add_t[1:-1]}]")
print(f"[{sub_t[1:-1]}]")
print(f"[{mul_t[1:-1]}]")
print(f"[{div_t[1:-1]}]")
print(f"[{mod_t[1:-1]}]")
print(f"[{pow_t[1:-1]}]")

