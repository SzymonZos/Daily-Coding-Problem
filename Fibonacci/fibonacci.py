import time
from matplotlib import pyplot as plt


def time_execution(function, arg):
    start = time.time()
    result = function(arg)
    end = time.time()
    print("{}({}) = {}, Computing time is {:.4f}"
          .format(function.__name__, arg, result, end - start))
    return end - start


def plot_execution_time(function, max_arg):
    results = [float()] * max_arg
    for i in range(max_arg):
        results[i] = time_execution(function, i)
    plt.figure()
    plt.title("{}({})".format(function.__name__, max_arg))
    plt.plot(range(max_arg), results)
    plt.show()


def fibonacci_recursive(n):
    if n < 0:
        raise None
    if n == 0 or n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    if n < 0:
        raise None
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a


def triplonacci_recursive(n):
    if n < 0:
        raise None
    if n == 0 or n == 1 or n == 2:
        return 1
    return triplonacci_recursive(n - 1) + \
           triplonacci_recursive(n - 2) + \
           triplonacci_recursive(n - 3)


def triplonacci_iterative(n):
    a, b, c = 1, 1, 1
    for i in range(n):
        a, b, c = b, c, a + b + c
    return a


def main():
    time_execution(fibonacci_recursive, 40)
    time_execution(fibonacci_iterative, 40)
    plot_execution_time(triplonacci_recursive, 30)
    plot_execution_time(triplonacci_iterative, 30)


if __name__ == "__main__":
    main()
