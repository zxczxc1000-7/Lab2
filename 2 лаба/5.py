def sim_num():
    value=int(input('Введимте целое число: '))
    if value<2:
        return False
    if value==2:
        return True
    lim = value**(1/2)
    i=2
    while (i<=lim):
        if value%i==0:
            return False
        i+=1
        return True
        
