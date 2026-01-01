'''
0.5. implement IO option to take an argument when executing program

3. return all possibilities, possibly highlighting wildcards
'''

from collections import Counter
import sys

def anagram_solver(board):
    hits = []

    board = board.upper()
    board_count = Counter(board)
    wildcards = board_count.pop('?', 0)

    with open("Collins Scrabble Words (2019).txt") as f:
        for raw_word in f:
            word = raw_word.strip().upper()

            word_count = Counter(word)

            needed_wildcards = 0
            for letter, count in word_count.items():
                available = board_count.get(letter, 0)
                if count > available:
                    needed_wildcards += count - available

            if needed_wildcards <= wildcards:
                hits.append(word)

    return hits
							



def main():
	allowed = "?QWERTYUIOPASDFGHJKLZXCVBNM"
	if sys.argv[1]:
		letters = sys.argv[1].upper()
		results = anagram_solver(letters)
	else:
		while True:
			letters = input("Type available letters without spaces, for unknown letters use wildcard '?'").upper()
			# if all(letter in allowed for letter in letters):
			# 	return letters
			for letter in letters:
				if letter not in allowed:
					print()
					break
			else:
				results = anagram_solver(letters)
				break
	for word in sorted(results):
		print(word)


main()
