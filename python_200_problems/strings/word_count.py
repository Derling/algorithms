#  Write a Python program to count the occurrences of each word in a given sentence

def word_count(sentence):
    words = {}
    for word in sentence.split():
        words[word] = words.get(word, 0) + 1
    return words

def solution(string):
    # course solution
    counts = dict()
    words = string.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

if __name__ == '__main__':
    print(word_count('the quick brown fox jumps over the lazy dog.'))