# def factorial(n):
#     output = 1
#     for i in range(1, n+1):
#         output *= i
#     return output
# def factorial(n):
#     if(n == 0):
#         return 1
#     else:
#         return n * factorial(n-1)
# print("1!:", factorial(1))
# print("2!:", factorial(2))
# print("3!:", factorial(3))
# print("4!:", factorial(4))
# print("5!:", factorial(5))

counter = 0


def fibonaci(n):
    counter += 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonaci(n-1) + fibonaci(n-2)


print(fibonaci(1))
print(fibonaci(2))
print(fibonaci(3))
print(fibonaci(4))
print(fibonaci(5))
print(fibonaci(35))
