def obr_num (x):
    y=0;
    x1=0;
    if x>0:
        while x>0:
            digit=x%10;
            x=x//10;
            y=y*10;
            y=y+digit;
        print (y)
    if x<0:
        x1=abs(x);
        while x1>0:
            digit=x1%10;
            x1=x1//10;
            y=y*10;
            y=y+digit;
        print (y*(-1))
        
