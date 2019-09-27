import random
import sys

wordList = [ "car", "balloon", "red", "computer", "mathematics", "flower",
"turtle", "clothing", "hero", "phone", "octopus", "bat", "apple", "rat"]
word = random.choice(wordList)
guesses = []
underscore = ["_"]
maxfails = 7
wordGuess = []
alphabet = "abcdefghijklmnopqrstuvwxyz"
for letters in word:
	wordGuess.append("_")
print(wordGuess)
done = False
while not done:
	guess = input("Guess a letter:")
	guess = guess.lower()
	if not guess in alphabet:
		print("That is not a letter. Try again!")
	if guess in guesses:
		print("You've guessed that already. Try again!")
	if(guess in word):
		print("You got a letter!")
		guesses.append(guess)
		for i in range(len(word)):
			if (word[i] == guess):
				wordGuess[i] = guess
		print(wordGuess)
	else:
		maxfails -= 1
		guesses.append(guess)
		print("This letter is incorrect.")
		print("You have", maxfails, "lives remaining.")
		print(wordGuess)
	if not ("_" in wordGuess):
		done = True
	if (maxfails == 0):
		done = True
