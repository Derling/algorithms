# Write a Python function to create the HTML string with tags around the word(s).
# Sample function and result : 
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

def html_tags(tag, string):
    return '<{tag}>{string}</{tag}>'.format(tag=tag, string=string)

def solution(tag, word):
    # course solution
	return "<%s>%s</%s>" % (tag, word, tag)

if __name__ == '__main__':
    print(html_tags('i', 'Python'))
    print(html_tags('b', 'Python Tutorial'))