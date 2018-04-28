=begin
src => https://www.reddit.com/r/dailyprogrammer/comments/76qk58/20171016_challenge_336_easy_cannibal_numbers/

Imagine a given set of numbers wherein some are cannibals. We define a cannibal as a larger number can eat a smaller number and increase its value by 1. There are no restrictions on how many numbers any given number can consume. A number which has been consumed is no longer available.

Your task is to determine the number of numbers which can have a value equal to or greater than a specified value. 

=end

def get_cannibals(numbers, q)
	# assuming the numbers are sorted
	# all the cannibals will be at the end of the array
	# and all the sacrifices will be at the beginning of the array
	cannibals = 0
	next_cannibal = numbers.length - 1
	next_sacrifice = 0

	while next_cannibal > next_sacrifice
		if numbers[next_cannibal] >= q
			next_cannibal -= 1
			cannibals += 1
		else
			numbers[next_cannibal] += 1
			next_sacrifice += 1
		end
	end

	# last number does not get valuated as while loop exits prematurelty
	if numbers[next_cannibal] >= q then cannibals += 1 end

	return cannibals
end

if __FILE__ == $0
	numbers = "21 9 5 8 10 1 3".split.map{|i| i.to_i}.sort
	queries = 15, 10
	queries.each do |q|
		puts "For the query #{q} there are #{get_cannibals(numbers, q)} cannibals"
	end
end