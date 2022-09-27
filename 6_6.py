number_list = [4, 1, 5, 8, 2, 9, 3, 10, 7, 6]
number2_list = [*sorted(filter(lambda x: x % 2 == 0, number_list)), *sorted(filter(lambda x: x % 2, number_list))]
print(number2_list)
