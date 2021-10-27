Osn_list=[]
One_list=[]
Two_list=[]
Three_list=[]
def add_list (Osn_list):
    for i in Osn_list:
        if i%2==0:
            One_list.append(i)
        if i%3==0:
            Two_list.append(i)
        if i%5==0:
            Three_list.append(i)

    print (One_list);
    print (Two_list);
    print (Three_list);

