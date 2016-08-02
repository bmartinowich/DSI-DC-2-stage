for i in range(1,5):

number = 23
running = 23

while running:
	guess = int(input('Enter an integer'))

	if guess == number:
		print('You have guessed it')
		running = False
	elif guess < number:
		print("No it's higher")
	else:
		print('no its lower')
else:
	print('the while loop is over')

	print ('done')
