import random
import sys

basicChars = [chr(i) for i in range(ord('a'), ord('z') + 1)] + ['-', "'"]
startChar = '0'
endChar = '1'
chars = basicChars + [startChar, endChar]

def allStringsOfLength(length, prefix=''):
    return [prefix + ''.join(i) for i in itertools.product(basicChars, repeat=length)]

class Markov:
    def __init__(self, lookahead=2):
        self.counts = {}
        self.probs = {}

        self.l = lookahead

        self.recalcProbs()

    def recalcProbs(self):
        for c in self.counts:
            tot = 0
            for c2 in self.counts[c]:
                tot += self.counts[c][c2]
            for c2 in self.counts[c]:
                self.probs[c][c2] = self.counts[c][c2] / tot

    def readChar(self, given, char):
        if not given in self.counts:
            self.counts[given] = {}
            self.probs[given] = {}

        if not char in self.counts[given]:
            self.counts[given][char] = 1
        else:
            self.counts[given][char] += 1

    def readWord(self, word, recalc=True):
        word = word.lower()
        cur = startChar * self.l
        for c in word:
            self.readChar(cur, c)
            cur = cur[1:] + c
        self.readChar(cur, endChar)

        if recalc:
            self.recalcProbs()

    def readFile(self, filename):
        inFile = open(filename, 'r')
        words = inFile.read().split()
        inFile.close()

        for w in words:
            self.readWord(w, False)

        self.recalcProbs()
        return words

    def generate(self, start=startChar):
        name = ''
        cur = startChar * (self.l - 1) + start

        while not endChar in cur:
            nextChar = cur[-1:]
            if nextChar != startChar:
                name += nextChar
            roll = random.random()
            for c in self.probs[cur]:
                p = self.probs[cur][c]
                if roll <= p:
                    cur = cur[1:] + c
                    break
                else:
                    roll -= p

        return name[0:1].upper() + name[1:]

def main(args):
    n = 10
    s = startChar
    l = 2
    if len(args) > 0:
        n = int(args[0])
    if len(args) > 1:
        l = int(args[1])
    if len(args) > 2:
        s = args[2]


    m = Markov(l)
    words = m.readFile('names.txt')

    for i in range(n):
        name = m.generate(s)
        if name in words:
            name += " (!)" # flag non-original names

        print('{:3}'.format(i + 1), ':', name)

if __name__ == '__main__':
    main(sys.argv[1:])
