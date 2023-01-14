def occurence(tab):
    t=[]
    T_unique=[]
    for i in range (0,len(tab)):
        a=0
        for j in range (0,len(tab)):
            if tab[i]==tab[j]:
                a=a+1
        if a >=1 :
            t.append(f"{tab[i]} a {a} occurence")
    t=list(set(t))
    return t



if __name__ == '__main__':
    tab=[3,8,8,9,9,3232,2331,2331]
    print(occurence(tab))