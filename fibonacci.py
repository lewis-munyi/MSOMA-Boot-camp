a = [1, 1]
#counter = 0
for counter in range(1, 30):
	x = a[counter - 1] + a[counter]
	a.append(x)
	counter += 1
print (a)