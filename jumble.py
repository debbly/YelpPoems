import random

def main():
	lines = jumble()
	return lines

def jumble():
	#look at a corpus of words that are positive or negative and have the words bolded or removed
	random1 = random.randint(1, len(all_words_dict))
	random2 = random.randint(1, len(all_words_dict))

	line1 = all_words_dict[random1]
	all_words_dict[random1] = all_words_dict[random2]
	all_words_dict[random2] = line1

	return all_words_dict
