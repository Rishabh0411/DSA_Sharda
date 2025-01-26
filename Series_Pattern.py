#import time

# class Series:
#     def arithmetic_progression(self, a, d, n):
#         return [a + i * d for i in range(n)]

#     def geometric_progression(self, a, r, n):
#         return [a * (r ** i) for i in range(n)]

#     def fibonacci_series(self, n):
#         fib_series = [0, 1]
#         while len(fib_series) < n:
#             fib_series.append(fib_series[-1] + fib_series[-2])
#         return fib_series[:n]

# series = Series()
# print(series.arithmetic_progression(1, 2, 10))
# print(series.geometric_progression(1, 2, 10))
# print(series.fibonacci_series(10))

#Pattern
# def pattern(n):
#     for i in range(1, n + 1):
#         print('* ' * i)

# n = int(input('Enter the number of rows: '))
# while n > 0:
#     pattern(n)
#     time.sleep(3)
#     n -= 1

#spiral pattern

def spiral_pattern(n):
    spiral = [[0] * n for _ in range(n)]
    left, right, top, bottom = 0, n - 1, 0, n - 1
    num = 1

    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            spiral[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):
            spiral[i][right] = num
            num += 1
        right -= 1

        for i in range(right, left - 1, -1):
            spiral[bottom][i] = num
            num += 1
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            spiral[i][left] = num
            num += 1
        left += 1

    for row in spiral:
        print(' '.join(map(str, row)))

n = int(input('Enter the size of the spiral: '))
spiral_pattern(n)