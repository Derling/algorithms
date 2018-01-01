# Write a Python function that takes a list of words and returns the length of the longest one

def longest_word(words):
    return sorted(words, key=len)[-1]

def solution(words_list):
    # course solution
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]


if __name__ == '__main__':
    print(longest_word(["PHP", "Exercices", "Backend"]))