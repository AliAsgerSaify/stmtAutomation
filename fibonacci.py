#  Copyright (c) 2023.
#  All Rights of this code is reserved with Administrator of this Project;
#  The administrator of this Project : Ali Asger
#  In case of any changes and/or discrepancies, please contact the administrator. Do not make any alteration without the permission of the administrator
def fibonacci(n):
    # Base cases: 0 and 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: use the formula F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Ask the user for a positive integer
n = int(input("Enter a positive integer: "))
n += 1

# Print the Fibonacci sequence up to the nth term
print("The Fibonacci sequence up to the", n, "th term is:")
for i in range(n):
  print(fibonacci(i), end=" ")

