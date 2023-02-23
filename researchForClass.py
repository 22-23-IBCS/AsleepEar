def stringPermutations(n, ans):
    if len(n) == 0:
        #print answer here
        print(ans)
        return 0
    
    for i in range(len(n)):
        a = n[0:i] # left substring
        b = n[i+1:] # right substring
        char = n[i] # char at index i
        remaining = a + b # concatenate left and right substrings
        stringPermutations(remaining, ans + char) # recurse adding character and passed through answer
        
        
    
    

def main():
    
    stringPermutations("the", "")


if __name__ == "__main__":
    main()
