def factorial(n):
    if n == 0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("enter the number is :"))
print(f"factorial is the number is:{factorial(n)} ")
#example
def sum_natural(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural(n - 1)

# Example
print(sum_natural(10))  
