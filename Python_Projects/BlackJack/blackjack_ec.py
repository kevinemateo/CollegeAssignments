import random
def main():
	print("Welcome to Black Jack!")
	user=getCard()
	comp=getCard()
	dealer=getCard()
	while comp<21 and user<21 and dealer<=17:
		hit_fold_exit = str(input("Would like to ‘hit’, ‘fold’, or ‘exit’? ")).lower()
		if hit_fold_exit == 'hit':
			user+=getCard()
			comp+=getCard()
			dealer+=getCard()
			print('Your hand:',user)
		elif hit_fold_exit == 'fold':
			print("You lost!")
			print("User's hand:",user,"Computer's hand:",comp)
			exit()
		elif hit_fold_exit == 'exit':
			print("Thanks for playing! Bye!")
			exit()
	compareHands(user,comp)
	print("User's hand:",user,"Computer's hand:",comp)
def getCard():
	card=random.randint(1,13)
	return card
def compareHands(u,c):
	if u==21 and c==21:
		print("It is a tie!")
	elif c==21 :
		print("*You're a loser, Computer is winner*")
	elif u==21:
		print("\t***You're a Winner***")
	elif u!=21 and c!=21:
		print("\t***Both of you lost***")
main()