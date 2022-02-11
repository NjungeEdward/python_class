#program to calc the largest number
A = float(input("Enter your first number" ))
B = float(input("Enter your second number" ))
C = float(input("Enter your third number" ))

if A>B and A>C:
  print("The largest number is",A)
elif B>A and B>C:
  print("The largest number is",B)
else:
  print("The largest number is",C)