print("""
1)Addition
2)Substraction
3)multiply
4)divison""")
value=int(input("Enter a value:"))
a=int(input("Enter a first number:"))
b=int(input("Enter second number:"))
if value == 1:
    print("The ans is",a+b)
elif value == 2:
    print("The answer is",a-b)
elif value == 3:
    print("The answer is",a*b)
elif value == 4:
    print("The answer is",a/b)
else:
    print("Enter between 1 to 5")
