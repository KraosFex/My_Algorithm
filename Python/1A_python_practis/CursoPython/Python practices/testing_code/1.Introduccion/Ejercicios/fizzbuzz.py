# for num in range(1,101):
#     string = ""
#     if num % 3 == 0:
#         string = string + "Fizz"
#     if num % 4 == 0:
#         string = string + "Buzz"
#     if num % 4 != 0 and num % 3 != 0:
#         string = string + str(num)
#     print(string)

# import itertools as its

# def fizz_buzz(n):
#     fizzes = its.cycle([""] * 2 + ["Fizz"])
#     buzzes = its.cycle([""] * 4 + ["Buzz"])
#     fizzes_buzzes = (fizz + buzz for fizz, buzz in zip(fizzes, buzzes))
#     result = (word or n for word, n in zip(fizzes_buzzes, its.count(1)))
#     for i in its.islice(result, 100):
#         print(i)

# fizz_buzz(100)
