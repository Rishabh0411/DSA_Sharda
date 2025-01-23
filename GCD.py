import time

# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# start_time = time.time()

# result = gcd(num1, num2)

# end_time = time.time()

# time_taken = end_time - start_time

# print(f"The GCD of {num1} and {num2} is {result}")
# print(f"Time taken to compute the GCD: {time_taken:.10f} seconds")

#Iterative
def gcd(a, b):
    while b != 0:
        a = a % b  
        a, b = b, a 
    return a

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

start_time = time.time()

result = gcd(num1, num2)

end_time = time.time()

time_taken = end_time - start_time
print(f"The GCD of {num1} and {num2} is {result}")
print(f"Time taken to compute the GCD: {time_taken:.10f} seconds")
