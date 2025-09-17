# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # store word in lowercase for consistency

    def match(self, word_list):
        matches = []
        # sorted letters of the original word
        sorted_word = sorted(self.word)

        for candidate in word_list:
            # avoid matching the word with itself
            if candidate.lower() != self.word and sorted(candidate.lower()) == sorted_word:
                matches.append(candidate)

        return matches
