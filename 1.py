a,b,c = [input() for i in range(3)]


a,b = [float(i) for i in [a,b]]



try:   
    act = {
    '+': a+b,
    '-': a-b,
    '*': a*b,
    'mod': a%b,
    'pow': a**b,
    'div': a//b,
    '/':a/b
    }
    print(act[c])

except ZeroDivisionError as err:
    print('Деление на 0!')
 
