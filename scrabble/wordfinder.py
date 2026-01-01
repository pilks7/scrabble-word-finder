'''
0.5. implement IO option to take an argument when executing program
1. Prompt user for letters, (and wildcards)
1.1 sanitise user data
2. check letters against scabble wordlist (most complicated logic step)
3. return all possibilities, possibly highlighting wildcards

'''

'''
anagram solver  -  iterate through 'word'. number of letters that require matching with 'board' == len(word) MINUS number of question marks in 'board'
'''

from collections import Counter

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
