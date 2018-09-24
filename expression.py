def power(x, y):
	return pow(x, y)
	# This gives the power

# take input from the user
print("Select Operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. power")
choice = input("Enter choice(1/2/3/4/5:")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
	print(num1, "+", num2, add(num1, num2))
	   print(value, ..., sep='', end="\n", file=sys.stdout, flush=False)