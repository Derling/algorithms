# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically)
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red

def unique_words(string):
    return ','.join(sorted(set(w for w in string.split(','))))

def solution():
    # course solution
    items = input("Input comma separated sequence of words")
    words = [word for word in items.split(",")]
    print(",".join(sorted(list(set(words)))))

if __name__ == '__main__':
    print(unique_words('red, white, black, red, green, black'))