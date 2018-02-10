import time
word = input("Enter an English word: ")
count = len(word)
letter_correct = []
for i in range(1,count+1):
	letter_correct.append("__")
letter_incorrect = []
incorrect = 0
while incorrect < 5:
	letter = input("Enter an English letter: ")
	if letter.isalpha():
		if ((letter) in word.lower()):
			index = word.find(letter)
			letter_correct[index]=letter
			while word.rfind(letter) != index:
				index = word.find(letter, index+1)
				letter_correct[index]=letter
		else:
			letter_incorrect.append(letter)
			incorrect += 1
		print("Letters that are correct:", letter_correct)
		print("letters that are incorrect:", letter_incorrect)
	else:
		print("Please enter a letter in the English Alphabet")
		time.sleep(5)
		exit()
		

