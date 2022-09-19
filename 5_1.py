n = int(input())
number_list=[i for i in range(1, n + 1)]
second_list=[]
print(number_list)
m=int(input())
for i in number_list:
    if i%m==0:
        second_list.append(i)
print(second_list)
k=int(input())