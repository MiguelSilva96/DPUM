import sys

#To avoid doing what was already done on another iteration 
done = {1: 1}

def base_algorithm(number):
	if number in done:
		return done[number]
	if number % 2 == 0:
		s = base_algorithm(number / 2)
	else:
		s = base_algorithm(number * 3 + 1)
	done[number] = s + 1	
	return done[number]

def calc_biggest_cycle(first_number, second_number):
	max_sum = 0
	curr_sum = 0
	if first_number > second_number:
		aux = first_number
		first_number  = second_number
		second_number = aux
	for value in range(first_number, second_number + 1):
		curr_sum = base_algorithm(value)
		if curr_sum > max_sum:
			max_sum = curr_sum
	return max_sum

for line in sys.stdin.readlines():
	first_number, second_number = [int(a) for a in line.split()]
	result = calc_biggest_cycle(first_number, second_number)
	print('{} {} {}'.format(first_number, second_number, result))