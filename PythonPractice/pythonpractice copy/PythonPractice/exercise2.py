num = int(input("Enter a number: "))

mod = int(num % 2)
four = int(num%4)

if mod == 1:
	print(str(num) + " is odd.")
elif four == 0:
	print(str(num) + " is divisible by four and even.")
else:
	print(str(num) + " is even.")
	
#comment



