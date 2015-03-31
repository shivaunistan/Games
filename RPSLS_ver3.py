#!/usr/bin/env python breaks the game?

import time
from sys import exit 
from random import randint

  
def game(wins, losses, count):
	print "Choose your weapon! Please type Rock, Paper, Scissors, Lizard or Spock"
	player_choice = raw_input().lower()
	game_options = ['rock', 'paper', 'scissors', 'lizard', 'spock']
	while player_choice not in game_options:
		print "Look buddy - I don't have time for this. You gotta pick one of the options! Try again!"
		player_choice = raw_input().lower()
	
	computer_choice = randint(0,4)
	print "Great - here we go!"
	time.sleep(.75)
	print "GET READY!"
	time.sleep(.75)
	print "Rock"
	time.sleep(.5)
	print "Paper"
	time.sleep(.5)
	print "Scissors"
	time.sleep(.5)
	print "Lizard"
	time.sleep(.5)
	print "Spock"
	time.sleep(.5)

	if player_choice == "rock":
		if computer_choice == 0:
			print "You both picked Rock - it's a draw!"
			end(wins, losses, count)
		elif computer_choice == 1:
			print "Rock is covered by Paper - you lose!"
			losses += 1
			end(wins, losses, count)
		elif computer_choice == 2:
			print "Rock smashes Scissors - you win!"
			wins += 1
			end(wins, losses, count)
		elif computer_choice == 3:
			print "Rock squashes Lizard - you win!"
			wins += 1
			end(wins, losses, count)
		elif computer_choice == 4:
			print "Rock is vaporized by Spock - you lose!"
			losses += 1
			end(wins, losses, count)


	if player_choice == "paper":
		if computer_choice == 0:
			print "Paper covers Rock - you win!"
			wins += 1
			end(wins, losses, count)
		elif computer_choice == 1:
			print "You both picked Paper - it's a draw! (Get it?!?)"
			end(wins, losses, count)
		elif computer_choice == 2:
			print "Paper is cut by Scissors - you lose!"
			losses += 1
			end(wins, losses, count)
		elif computer_choice == 3:
			print "Paper is eaten by Lizard - you lose!"
			losses += 1
			end(wins, losses, count)
		elif computer_choice == 4:
			print "Paper disproves Spock - you win!"
			wins += 1
			end(wins, losses, count)        


	if player_choice == "scissors":
		if computer_choice == 0:
			print "Scissors are smashed by Rock - you lose!"
			losses += 1
			end(wins, losses, count)
		elif computer_choice == 1:
			print "Scissors cuts Paper - you win!"
			wins += 1
			end(wins, losses, count)
		elif computer_choice == 2:
			print "You both picked Scissors - it's a draw!"
			end(wins, losses, count)
		elif computer_choice == 3:
			print "Scissors decapitates Lizard - you win!"
			wins += 1
			end(wins, losses, count)
		elif computer_choice == 4:
			print "Scissors are smashed by Spock - you lose!"
			losses += 1
			end(wins, losses, count)


	if player_choice == "lizard":
		if computer_choice == 0:
			print "Lizard is squished by Rock - you lose!"
			losses += 1
			end(wins, losses, count)
		elif computer_choice == 1:
			print "Lizard eats Paper - you win!"
			wins += 1
			end(wins, losses, count)
		elif computer_choice == 2:
			print "Lizard is decapitated by Scissors - you lose!"
			losses += 1
			end(wins, losses, count)
		elif computer_choice == 3:
			print "You both picked Lizard - it's a draw!"
			end(wins, losses, count)
		elif computer_choice == 4:
			print "Lizard poisons Spock - you win!"
			wins += 1
			end(wins, losses, count)

	if player_choice == "spock":
		if computer_choice == 0:
			print "Spock vaporizes Rock - you win!"
			wins += 1
			end(wins, losses, count)
		elif computer_choice == 1:
			print "Spock is disproven by Paper - you lose!"
			losses += 1
			end(wins, losses, count)
		elif computer_choice == 2:
			print "Spock smashes Scissors - you win!"
			wins += 1
			end(wins, losses, count)
		elif computer_choice == 3:
			print "Spock is poisoned by Lizard - you lose!"
			losses += 1
			end(wins, losses, count)
		elif computer_choice == 4:
			print "You both picked Spock - HIGHLY ILLOGICAL! It's a draw!"
			end(wins, losses, count)


def end(wins, losses, count):
		count+=1
		print "Wins: " + str(wins) + " Losses: " + str(losses)
		print "That was fun! Do you want to play again?"
		yes_or_no(raw_input().lower(), count, wins, losses)
	

def yes_or_no(input_value, count, wins, losses):
	yes_no_responses = ['yes', 'no']
	while input_value not in yes_no_responses:
		if input_value.startswith(('y', 'n')):
			print 'You need to type out "yes" or "no", I am but a simple program who only does what my mom said I could do.'
		#print 'I don\'t know what that means - talk to me in computerdummyspeak. You gotta type "yes" or "no"'
		input_value = raw_input().lower()
	if input_value == "yes":
		game(wins, losses, count)
	elif input_value == 'no' and count >= 1:
		print "Alas - how will I ever understand humanity? Goodbye."        
		exit()
	else:
		print "FINE, THEN! I DIDN'T WANT TO SHOW YOU MY COOL PROGRAM ANYWAY! GOOD DAY!"
		exit()


if __name__ == '__main__':
	wins = 0
	losses = 0
	round_counter = 0
	yes_or_no(raw_input("Hi there! Would you like to play Rock Paper Scissors Lizard Spock?").lower(),round_counter, wins, losses)
	player_input = player_input.lower()
	
	if player_input:
		game(wins, losses, 0)
	else:  
		print "FINE, THEN! I DIDN'T WANT TO SHOW YOU MY COOL PROGRAM ANYWAY! GOOD DAY!"      
		exit()

###Current issues:
#At "That was fun! Do you want to play again?" system does not recognize garbage text that is entered or just hitting enter
#At "Hi there! Would you like to play Rock Paper Scissors Lizard Spock?" system does not recognize garbage text that is entered	or just hitting enter
#unit test, maybe?

