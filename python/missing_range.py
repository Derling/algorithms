def get_missing_nums(arr, missing=2):
	# default missing value to make function dynamic
	missing_nums = set()
	# max_range used to determine possible range of missing numbers
	max_range = arr[-1] + missing + 1

	for num in range(1, max_range):
		if len(missing_nums) == missing:
			break
		if num not in arr:
			missing_nums.add(num)
	return missing_nums

if __name__ == '__main__':
	tests = [
		[1, 3, 5, 6],
		[1, 2, 4],
		[1, 2]
	]
	for t in tests:
		print(get_missing_nums(t))