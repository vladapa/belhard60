n = int(input())
def decimal_to_binary(n):
    if (n > 1):
        decimal_to_binary(n // 2)
    print(n % 2)
if 1 == 1:
 decimal_to_binary(n)
 
