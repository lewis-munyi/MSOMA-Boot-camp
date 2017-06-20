#Assignment 1
numbers = ['\t1', '\t1', '\n----------------------------']
counter = 0
while counter < 3:
	counter += 1 
	print (numbers[0] + "	" + numbers[1] + numbers[2])
	pass
print("Done printing the Tic-Tac-Toe\n\n\n")

#Assignment 2
first_name = input("Enter First Name ")
last_name = input("Enter Last name ")
print ("Enter your Date of Birth:\n")
month = input("Month: ")
day = input("Day: ")
year = input("Year: ")
print (first_name + " " + last_name + " was born on " + month + " " + day + " " + year)
