import random, time
txt = "/Users/marwan/Documents/Code/list_of_words.txt"
def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words
words = readFile(txt)
def joe():
	line = ""
	print("joe's favorite numbers: ")
	while True:
		for i in range(204):
			line = line + str(random.choice([0,1])) + " "
		print(line)
		line = ""
		time.sleep((random.randint(1, 10)/50))

def joe_bo():
	line = ""
	while True:
		while True:
			line = line + words[random.randint(0, len(words)-1)] + " "
			if len(line)>=180:
				break
		print(line)
		print("")
		time.sleep(0.5)
		line=""

i = input("input: ")
if i == "1":
	joe()
else:
	joe_bo()