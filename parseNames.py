basicChars = [chr(i) for i in range(ord('a'), ord('z') + 1)] + ['-', "'"]

def main():
	inFile = open('names_pre.txt', 'r')
	words = inFile.read().split()
	inFile.close()

	outFile = open('names.txt', 'w')
	for word in words:
		valid = True
		for c in word.lower():
			if not c in basicChars:
				valid = False
				break
		if valid:
			outFile.write(word + '\n')
	outFile.close()

if __name__ == '__main__':
	main()