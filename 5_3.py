n = int(input())
number_list = [i for i in range(1, n + 1)]
number_list2=[]
for i in number_list:
    if i % 2 == 0:
        number_list2.append(i)
print(number_list2)
