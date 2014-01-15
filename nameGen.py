import random
import sys

basicChars = [chr(i) for i in range(ord('a'), ord('z') + 1)] + ['-', "'"]
startChar = '0'
endChar = '1'
chars = basicChars + [startChar, endChar]

class Markov:
	def __init__(self):
		self.counts = {}
		self.probs = {}
		for c in chars[:-1]:
			self.counts[c] = {}
			self.probs[c] = {}
			for c2 in chars:
				self.counts[c][c2] = 1
		self.recalcProbs()

	def recalcProbs(self):
		for c in chars[:-1]:
			tot = 0
			for c2 in chars:
				tot += self.counts[c][c2]
			for c2 in chars:
				self.probs[c][c2] = self.counts[c][c2] / tot

	def readWord(self, word, recalc=False):
		word = word.lower()
		cur = startChar
		for c in word:
			self.counts[cur][c] += 1
			cur = c
		self.counts[cur][endChar] += 1

		if recalc:
			self.recalcProbs()

	def readFile(self, filename):
		inFile = open(filename, 'r')
		words = inFile.read().split()
		inFile.close()

		for w in words:
			self.readWord(w)

		self.recalcProbs()

	def generate(self):
		name = ''
		cur = startChar

		while cur != endChar:
			if cur != startChar:
				name += cur
			roll = random.random()
			for c in chars:
				p = self.probs[cur][c]
				if roll <= p:
					cur = c
					break
				else:
					roll -= p

		return name[0:1].upper() + name[1:]

def main(args):
	m = Markov()
	m.readFile('names.txt')

	n = 10
	if len(args) > 0:
		n = int(args[0])

	for i in range(n):
		print(i + 1, ':', m.generate())

if __name__ == '__main__':
	main(sys.argv[1:])
