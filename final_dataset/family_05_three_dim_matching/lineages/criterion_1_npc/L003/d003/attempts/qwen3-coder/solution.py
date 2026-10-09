from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    triplets = []
    index = 2
    for _ in range(t):
        x = int(data[index])
        y = int(data[index+1])
        z = int(data[index+2])
        triplets.append((x, y, z))
        index += 3
    
    # Try to find a perfect matching using backtracking
    # We need to match each left pillar, right pillar, and keystone exactly once
    
    # Used flags for each type
    used_left = [False] * (k + 1)
    used_right = [False] * (k + 1)
    used_keystone = [False] * (k + 1)
    
    result = []
    
    def backtrack(pos):
        if pos == k:
            return True
            
        for i in range(len(triplets)):
            x, y, z = triplets[i]
            if not used_left[x] and not used_right[y] and not used_keystone[z]:
                used_left[x] = True
                used_right[y] = True
                used_keystone[z] = True
                result.append((x, y, z))
                
                if backtrack(pos + 1):
                    return True
                    
                result.pop()
                used_left[x] = False
                used_right[y] = False
                used_keystone[z] = False
        
        return False
    
    if backtrack(0):
        print("YES")
        for triplet in result:
            print(triplet[0], triplet[1], triplet[2])
    else:
        print("NO")

solve()