class Node

	def initialize(value, next_node=nil)
		@value = value
		@next = next_node
	end

	def value
		@value
	end

	def get_next
		@next
	end

	def set_next(node)
		@next = node
	end

	def set_value(new_value)
		@value = new_value
	end

end

def create_list(arr = [])
	list = Node.new(0)
	dummy = list

	arr.each do |i|
		list.set_next Node.new(i)
		list = list.get_next
	end

	return dummy.get_next
end

def get_list(node)
	values = []
	
	while node do
		values.append node.value
		node = node.get_next
	end

	return values
end


def merge_lists(list1, list2)
	unless list1 then return list2 end
	unless list2 then return list1 end

	new_list = Node.new(0)
	dummy = new_list

	while list1 or list2 do
		val1 = nil
		val2 = nil

		if list1
			val1 = list1.value
		end
		if list2
			val2 = list2.value
		end

		if list1 and list2
			if val1 < val2
				new_list.set_next Node.new(val1)
				list1 = list1.get_next
			else
				new_list.set_next Node.new(val2)
				list2 = list2.get_next
			end
		elsif list1
			new_list.set_next Node.new(val1)
			list1 = list1.get_next
		elsif list2
			new_list.set_next Node.new(val1)
			list2 = list2.get_next
		end

		new_list = new_list.get_next
	end

	return dummy.get_next
end

if __FILE__ == $0 then
	arr1 = [1, 3, 6, 9, 10]
	arr2 = [2, 4, 5, 7, 8]
	list1 = create_list(arr1)
	list2 = create_list(arr2)
	puts "merged arrays = #{get_list(merge_lists(list1, list2)).to_s}"
	puts "list1 null list2 = #{get_list(merge_lists(list1, nil)).to_s}"
	puts "list2 null list1 = #{get_list(merge_lists(nil, list2)).to_s}"
	puts "list2 null list1 null = #{get_list(merge_lists(nil, nil)).to_s}"
end