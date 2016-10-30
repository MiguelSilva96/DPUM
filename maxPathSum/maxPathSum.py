import fileinput

'''
	Problem:
		- Finding maximum sum from top
		to bottom of a triangle of ints
	It's problem number 67 from project euler
'''

l_str = list()
l_int = list()
size = 0

#bottom-up method
def calc_max_sum():
	point = size - 2
	max_n = 0
	while point >= 0:
		for i in range(0, len(l_int[point])):
			max_n = max(l_int[point + 1][i], l_int[point + 1][i + 1])
			l_int[point][i] += max_n
		point -= 1

#reading
for line in fileinput.input():
	l_str.append(line.split(" "))

size = len(l_str)

#parsing
for i in range(0, size):
	l_int.append([])
	for element in l_str[i]:
		l_int[i].append(int(element))

calc_max_sum()

#solution
print(l_int[0][0])