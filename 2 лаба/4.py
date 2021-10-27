def newton():
    value=int(input('Введите число: '))
    x=value/2
    y=(x+value/x)/2
    while y!=x:
        x=y;
        y=(x+value/x)/2;
    print ('Корень введённого числа = ', x);
    return x
newton()
