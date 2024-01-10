my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
def weight_average(my_list):
	sum1 = 0
	sum2 = 0
	for i in my_list:
		number1, number2 = i
		mul = number1 * number2
		sum1 += mul
		sum2 += number2
	print(sum1 / sum2)

weight_average(my_list)