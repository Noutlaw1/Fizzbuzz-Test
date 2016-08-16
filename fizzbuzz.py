count = 1
while count <= 100:
	if count%3 == 0:
		if count%5 == 0:
			print("Fizzbuzz")
			count = count + 1
			continue
		else:
			print("Fizz")
			count = count + 1
			continue
	if count%5 == 0:
		print("Buzz")
		count = count + 1
		continue
	
	print count
	count = count + 1
