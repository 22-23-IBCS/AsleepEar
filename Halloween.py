import random
import copy
import time

class House:

    def __init__(self):
        self.value = random.randint(1,10)

#memoization not yet implemented

def shortestPath(depth, l, path, pos):

    if(depth <= 0):
        v = 0
        for i in path:
            v += l[i[0]][i[1]].value

        v /= len(path)
        a=(v,path)
        return a

            
    possibles = [(pos[0]-1,pos[1]), (pos[0]+1,pos[1]), (pos[0],pos[1]-1), (pos[0],pos[1]+1)]
    #visit = ((visit+l[pos[0]][pos[1]].value)/2) if len(path) != 0 else visit

    
    
    path.append(pos)
    p = []
    v = []
    for i in range(4):
        if (possibles[i] not in path and (possibles[i][0] <= 4 and possibles[i][0] >= 0 and possibles[i][1] <= 4 and possibles[i][1] >= 0)):
            s = shortestPath(depth-1, l, copy.deepcopy(path), (possibles[i][0],possibles[i][1]))
            v.append(s[0])
            p.append(s[1])
            

    if(len(p) == 0 and depth > 0):
        return(-float('inf'), path)
    
    
    return (max(v),p[v.index(max(v))])
    

def main():
    
    neighborhood = []


    nAvg = 0
    for i in range(5):
        neighborhood.append([])
        for j in range(5):
            neighborhood[i].append(House())
            nAvg += neighborhood[i][len(neighborhood[i])-1].value
    nAvg /= 25

    
    for i in neighborhood:
        for j in i:
            print(j.value, end=" ")
        print()
    


    

        
    n = input("How many houses would you like to visit?\n")
    if n == "0":
        print("no candy for you this year :(")
        return 0
    w = 0
    while True:
        w = input("Where would you like to start?\n(top left = \"0,0\", bottom right = \"4,4\")\n")
        try:
            w = (int(w[0]),int(w[2]))
            break
        except ValueError:
            print("You cannot wander outside the neighborhood")
        except:
            print("I don't know where that is")
            
        
        
    

    
    blorp = time.time()
    a = shortestPath(int(n), neighborhood, [], (w[0],w[1]))
    print(time.time()-blorp)
    temp = 0
    for i in a[1]:
        temp += neighborhood[i[0]][i[1]].value
    ave = temp/len(a[1])
    print("Neighborhood Average: " + str(nAvg))
    print("Your Average: " + str(ave))

    if(ave >= nAvg):
        print("Path required to take: " + str(a[1]))
        print("Worth It!!!!!")
    else:
        print("Path required to take: " + str(a[1]))
        print("Not Worth It :(")
        
    
            
    
    


if __name__ == "__main__":
    main()
