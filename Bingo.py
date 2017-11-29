from time import sleep
import random


mynumber=random.randint(0,50)

Daniel = []

Daniel.append(mynumber)
	


game = 0

while(game < 6):
  
	number=random.randint(0,50)
	number=(int(number))
	numberstr = (str(number))


	print(Daniel)
	print(numberstr)
	sleep(1)
  
	if number in Daniel:
		print("Bingo!")
		game = game + 1
