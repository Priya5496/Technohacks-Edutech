def cel_to_far(celsius):
	return(celsius*9/5)+32
def far_to_cel(fahrenheit):
	return(fahrenheit-32)*5/9
print("Temperature Converter")
while True:
	print("Select an Option")
	print("1.Convert Celsius to Farenheit")
	print("2.Convert Farenheit to Celsius")
	print("3.Exit")
	choice=input("Enter your Choice(1-3):")
	if choice=='3':
		print("Exit")
		break
	if choice=='1':
		celsius=float(input("Enter the temperature in Celsius"))
		fahrenheit=cel_to_far(celsius)
		print(f"{celsius}C is equal to {fahrenheit}F")
	elif choice=='2':
		fahrenheit=float(input("Enter the temperature in fahrenheit"))
		celsius=far_to_cel(fahrenheit)
		print(f"{fahrenheit}C is equal to {celsius}F")
	else:
		print("Invalid chie.Please try again.")
		
		
		
