number1 = int(input("введите первое число: "))
do = str(input("введите действие(+, -, /, *): "))
number2 = int(input("введите второе число: "))
if do == '+':
    print('ответ: '+ number1 + number2)
elif do == '*':
    print('ответ: '+ number1 * number2)
elif do == '-':
    print('ответ: '+ number1 - number2)
elif do == '/':
    print('ответ: '+ number1/number2)