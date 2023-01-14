# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def factorielle(n):
    if n==0 :
        return 1
    else :
        return n*factorielle(n-1)

if __name__ == '__main__':
    print(factorielle(4))