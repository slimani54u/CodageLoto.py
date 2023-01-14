def fac(n):
    a=1
    if n==0 :
        return 1
    else:
        for i in range (n,0,-1):
            a=i*a
        return a



if __name__ == '__main__':
    print(fac(4))