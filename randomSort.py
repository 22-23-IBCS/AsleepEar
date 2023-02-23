import random
import time

def main():
    n = 10
    l = [random.randint(0,n) for i in range(n)]
    print(l)
    t = time.time()
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

    print("time: " + str(time.time()-t))
    print(l)
        


if __name__ == "__main__":
    main()
