nums = [1, 2]

num_one = 0

num_two = 1

while True:
	nums.append(nums[num_one]+nums[num_two])
	if len(nums) == 15:
		break
	# if nums[num_one]+nums[num_two] >= 4000000:
	# 	break
	num_one = num_one + 1
	num_two = num_two + 1

print nums

# even_nums = []

# even_ints = ['0', '2', '4', '6', '8']

# for num in nums:
# 	if str(num).endswith(tuple(even_ints)):
# 		even_nums.append(int(num))

# print even_nums, '\n', len(even_nums), 'characters in list', '\n', 'Sum:', sum(even_nums)


