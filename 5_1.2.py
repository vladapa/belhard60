a_list = [i for i in range(1, 5)]
print(a_list)
a = 1
do = str(input())
n = 0
while do != 'stop':
 if do == ">":
     if n == 4:
         print(a_list[0])
     else:
       a_list.index(n+1)
       print(a_list[n+1])
       do = str(input())
     n += 1
 elif do == '<':
     if n == 0:
         print(a_list[4])
     else:
      a_list.index(n-1)
      print(a_list[n-1])
      do = str(input())
      n -= 1




