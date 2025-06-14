for i in range (1, 50,2):
    if i ==34:
        break
    print(i)
    #another example is using while loop
    i = 1
    while (i<50):
        if i == 34:
            break
        i = i+1
        print(i)
       # continue function using loop 
x = ["apple","banana","peach","lemon" "talha"]
for i in x:

    print(i)
    #another example is using loop
    #print the total sum of natural number of 10
    total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)
#Write a loop to reverse a given integer
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print("Reversed number:", rev)
#example 
n = int(input("enter the number:"))
for i in range(1,11):
  print(f"{n} x {i} = {n*i}")  
  #example of factorial of a 
  num = int(input("Enter a number: "))
  fact = 1
  for i in range(1, num + 1):
    fact = fact * i
    print (fact)
