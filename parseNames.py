import sys

basicChars = [chr(i) for i in range(ord('a'), ord('z') + 1)] + ['-', "'"]

def main(args):
	if len(args) < 2:
		print('Usage: parseNames [input filename] [output filename]')
		return

	inDoc = args[0]
	outDoc = args[1]

	inFile = open(inDoc, 'r')
	words = inFile.read().split()
	inFile.close()

	outFile = open(outDoc, 'w')
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
	main(sys.argv[1:])