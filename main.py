def wordCount(text):
	words = text.split()
	print(f"Count: {len(words)}")

def characterCount(text):
	characters = {}
	lower_txt = text.lower()
	for char in lower_txt:
		if char.isalpha():
			if char in characters:
				characters[char] += 1
			else:
				characters[char] = 1
	return characters

def report(char_count):
	print(f"Dictionary: {char_count}")
	charList = []
	for key, value in char_count.items():
		mini_dict = {"character": key, "num": value}  # Create mini dictionary
		charList.append(mini_dict)  # Append mini dictionary to list
	for char in charList:
		print(char)
	charList.sort(reverse=True, key = sort_on)
	for char in charList:
		print(f"The {char['character']} character was found {char['num']} times")

#	print(charList)

def sort_on(dict):
    return dict["num"]

def main():
	with open("books/frankenstein.txt") as f:
		file_contents = f.read()
	report(characterCount(file_contents))
	#characterCount(file_contents)
	#wordcount(file_contents)
	#print(file_contents)
main()