import random

def guess(x):
	random_number = random.randint(1,x)
	guess = 0
	while guess != random_number:
		guess = int(input(f'Prova ad indovinare un numero da 1 a {x} '))
		#print(guess)
		if guess < random_number:
			print("Troppo basso")
		elif guess > random_number:
			print("Troppo alto")
	print(f'Esatto, hai indovinato, il numero è {random_number} ')

guess(10)
