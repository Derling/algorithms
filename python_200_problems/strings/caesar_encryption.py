# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
# Write a Python program to create a Caesar encryption

# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
# For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.
# The method is named after Julius Caesar, who used it in his private correspondence.

# plaintext:  defend the east wall of the castle
# ciphertext: efgfoe uif fbtu xbmm pg uif dbtumf

def caesar(text, shift=0):
    encrypted_message = ''
    for  char in text:
        if char == ' ':
            encrypted_message = encrypted_message + char
            continue
        numerical_value = ord(char) + shift
        encrypted_message = encrypted_message + chr(numerical_value)
    return encrypted_message

def solution(realText, step):
    # course solution
	outText = []
	cryptText = []
	
	uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	for eachLetter in realText:
		if eachLetter in uppercase:
			index = uppercase.index(eachLetter)
			crypting = (index + step) % 26
			cryptText.append(crypting)
			newLetter = uppercase[crypting]
			outText.append(newLetter)
		elif eachLetter in lowercase:
			index = lowercase.index(eachLetter)
			crypting = (index + step) % 26
			cryptText.append(crypting)
			newLetter = lowercase[crypting]
			outText.append(newLetter)
	return outText

if __name__ == '__main__':
    msg = 'defend the east wall of the castle'
    print(msg, 'encrypted is {0}'.format(
            caesar(msg, shift=1)))
            