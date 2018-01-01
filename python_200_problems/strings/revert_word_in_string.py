# 'The quick brown fox jumps over the lazy dog.'
# input : "The quick brown fox jumps over the lazy dog."
# output : "dog. lazy the over jumps fox brown quick The "

def revert_word_in_string(string):
    return ' '.join(string.split()[::-1])

def solution(text):
    # course solution
     for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))

if __name__ == '__main__':
    print(revert_word_in_string("The quick brown fox jumps over the lazy dog."))