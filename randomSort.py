import random

def main():
    l = [1,4,6,8,2,585,24,64,7]
    while True:
        a = random.randint(0,len(l)-1)
        b = random.randint(0,len(l)-1)
        l[a], l[b]  = l[b], l[a]
        isSorted = True
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                isSorted = False
                break
        if isSorted:
            break

    print(l)
        


if __name__ == "__main__":
    main()
