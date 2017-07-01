def collatzTags(string):
    alphabet={'a':'bc','b':'a','c':'aaa'}
    while len(string)>1:
        string=string[2:]+alphabet[string[0]]
        print(string)

if __name__ == '__main__':
	collatzTags('aaa')