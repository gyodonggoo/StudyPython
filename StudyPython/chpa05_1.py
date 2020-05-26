# def print_3_times():
#     print("안녕하세요")
#     print("안녕하세요")
#     print("안녕하세요")


# def print_n_times(value, n):
#     for i in range(n):
#         print(value)


# def print_n_times(value):
#     for i in range(10):
#         print(value, end=" ")


# print_3_times()

# print_n_times("안녕하세여", 5)

# print_n_times("안녕하세여")

# def return_test():
#     print("A 위치입니다.")
#     return
#     print("B 위치입니다.")


# value = return_test()
# print("value 는 {}".format(value))

# if(value == None):
#     print("value 값이 없습니다.")
# else:
#     print("value 값이 있습니다.")

def multi_all(start, end):
    output = 1
    for i in range(start, end + 1):
        output *= i
    return output


print("0 to 100:", multi_all(1, 100))
