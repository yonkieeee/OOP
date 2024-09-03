def fib(first_num, second_num, n):
    if n == 0:
        return first_num

    return fib(second_num, first_num + second_num, n - 1)


def fib_arr(first_num, second_num, n):
    result = []

    for i in range(1, n + 1):
        result.append(fib(first_num, second_num, i))

    return result


with open("fibo_num", "r") as file:
    nums = file.readlines()

with open("steps", "r") as file:
    stepes = file.readlines()


for i_num, i_step in zip(nums, stepes):
    numbers = [float(num) for num in i_num.strip().split(',')]
    step = int(i_step.strip())

    first_num, second_num = numbers
    n = step

    print(fib_arr(first_num, second_num, n))