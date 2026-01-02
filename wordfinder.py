from collections import Counter
import sys

banner = """

*	▄   ▄  ▄▄▄   ▄▄▄ ▐▌   *▗▞▀▀▘▄ ▄▄▄▄     ▐▌▗▞▀▚▖ ▄▄▄     
	█ ▄ █ █   █ █    ▐▌    ▐▌   ▄ █   █    ▐▌▐▛▀▀▘█     *     
	█▄█▄█ ▀▄▄▄▀ █ ▗▞▀▜▌    ▐▛▀▘ █ █ * █ ▗▞▀▜▌▝▚▄▄▖█        
	              ▝▚▄▟▌    ▐▌   █       ▝▚▄▟▌ *             
                                                      
                 *                                     """
def anagram_solver(board):
	hits = []

	board = board.upper()
	board_count = Counter(board)
	wildcards = board_count.pop('?', 0)

	with open("Collins Scrabble Words (2019).txt") as f:
		for raw_word in f:
			word = raw_word.strip().upper()

			if len(word) > len(board):
				continue

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

	if len(sys.argv) == 2 and sys.argv[1] in ("-h", "--help"):
		print(banner)
		print("""
An anagram solver designed for Scrabble or similar games.
Type your anagram letters (with wildcards '?') either as an argument when executing the program
or when prompted after executing (without arguments).

options:
	-h, --help		show this help screen
		""")
		return

	elif len(sys.argv) == 2:
		letters = sys.argv[1].upper().replace(" ", "")
		for letter in letters:
			if letter not in allowed:
				print("Invalid character in input.")
				return
		results = anagram_solver(letters)

	else:
		print(banner)
		while True:
			letters = input("Type your letters here, for unknown letters use wildcard '?': ").upper().replace(" ", "")
			for letter in letters:
				if letter not in allowed:
					print("Invalid character in input.")
					break
			else:
				results = anagram_solver(letters)
				break

	if results:
		for word in sorted(results):
			print(word)
	else:
		print("No words possible from your selection!")


if __name__ == "__main__":
	main()
