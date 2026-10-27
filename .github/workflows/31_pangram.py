import string

def is_pangram(sentence):
    letters = set(sentence.lower())
    return all(ch in letters for ch in string.ascii_lowercase)