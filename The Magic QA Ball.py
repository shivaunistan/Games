
import random
import time
import sys


QA_QUESTION = "What is it that you wish to learn about your bug?"
PROMPT = "> "
WORKING_MSG = "Let us ask the QA fates..."
RESPONSES = [
	"It is certain...that it's a bug",
	"It is decidedly a feature",
	"Without a doubt: won't fix",
	"Yes, definitely check on an earlier version",
	"You may rely on it...being punted to the next release",
	"As I see it, we do not have that device for repro",
	"Most likely a bug",
	"Outlook good for needing more info",
	"Yes - but not a blocker",
	"Signs point to yes, this is a bug" ,
	"Reply hazy - try again after all-hands meeting",
	"Ask again later",
	"Better not tell you now - Scotch Friday is starting",
	"Cannot predict now - in new hire dance practice",
	"Concentrate and ask again",
	"Don't count on it",
	"My reply is that something is wonky on the backend",
	"My sources say no, but set them as watchers",
	"Outlook not so good. Gmail is superior. Check with me later.",
	"Very doubtful that this is a blocker"]
TRY_AGAIN = "Would you like to ask about another bug? (y/n)"

def fortune():
	print(QA_QUESTION)
	raw_input(PROMPT)
	print(WORKING_MSG)
	time.sleep(2)
	print
	print(random.choice(RESPONSES))
	do_over()

def do_over():
	print(TRY_AGAIN)
	answer = raw_input(PROMPT)
	if answer.strip()[0] == "y":
		fortune()
	else:
		print("May the QA fates favor you with perfect builds forever!")
		sys.exit(0)

# App
print("=== MAGIC QA BALL ===")
fortune()
