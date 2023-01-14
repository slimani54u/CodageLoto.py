


def TriBulle(list) :
    for i in range (0,len(list)):
        for j in range(i+1,len(list)):
            if list [i]>list[j] :
                tmp=list[j]
                list[j]=list[i]
                liste[i]=tmp
    return list


def TriBulleAmeliore(list) :
    for i in range (0,len(list)-1):
        for j in range(i+1,len(list)):
            if list [i]>list[j] :
                tmp=list[j]
                list[j]=list[i]
                liste[i]=tmp
    return list


if __name__ == '__main__':
        liste=[3,9,1,5]
        print(TriBulle(liste))