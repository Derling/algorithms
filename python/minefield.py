'''
	[2017-11-14] Challenge #340 [Intermediate] Walk in a Minefield

	src: https://www.reddit.com/r/dailyprogrammer/comments/7d4yoe/20171114_challenge_340_intermediate_walk_in_a/

	Challenge complete however it is a rough solution to the problem only solves the case presented in the porblem
'''


def walk_field(minefield, last_row= 0, last_col=0, current_row=0, current_col=0, exit_row=-1, exit_col=-1):
	# check if we have exitted the maze
	if current_row == exit_row and current_col == exit_col:
		return '-'
	# if first time in find entry and exit points
	if not current_row and not current_col:
		entry_row, entry_col = 0, 0
		for row in range(len(minefield)):
			if minefield[row][0] == 'M':
				entry_row = row
				entry_col = 0
				break
		exit_row, exit_col = 0, 0
		for row in range(len(minefield)):
			if minefield[row][-1] == '0':
				exit_row = row
				exit_col = len(minefield[row]) - 1
				break
		return 'I' + walk_field(minefield, current_row=entry_row, current_col=entry_col,
								exit_row=exit_row, exit_col=exit_col)
	# check if we can go up ( this will help us reach the row that the exit is on)
	# if the last thing we did was not to go up then we go up
	if (current_row > exit_row and can_go_there(minefield[current_row - 1][current_col])) and \
		(last_row != current_row - 1):
		return 'N' + walk_field(minefield, last_row=current_row, last_col=current_col,
								current_row = current_row - 1, current_col= current_col,
								exit_row=exit_row, exit_col=exit_col)
	# check if we can go right towards the exit ( this will lead us towards the exit)
	# if the last thing we did was not to go right then we go right
	elif (current_col < exit_col and can_go_there(minefield[current_row][current_col + 1])) and \
		(last_col != current_col + 1):
		return 'E' + walk_field(minefield, last_row=current_row, last_col=current_col,
								current_row = current_row, current_col= current_col + 1,
								exit_row=exit_row, exit_col=exit_col)

def can_go_there(asc_char_at_location):
	return asc_char_at_location == '0'

if __name__ == '__main__':
	test = '''
	+++++++++++++
	+000000000000
	+0000000*000+
	+00000000000+
	+00000000*00+
	+00000000000+
	M00000000000+
	+++++++++++++'''
	# ugly list comprehension because of the way the string is copied :(
	field = [[col for col in row if col != '\t'] for row in test.strip().split('\n')]
	print(walk_field(field))
