from itertools import combinations

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
        index += 3
        triplets.append((x, y, z))
    
    # Try all combinations of k triplets
    for combo in combinations(range(t), k):
        # Check if this combination uses each stimulus exactly once
        freq_used = [0] * (k + 1)
        path_used = [0] * (k + 1)
        thresh_used = [0] * (k + 1)
        
        valid = True
        selected_triplets = []
        
        for i in combo:
            x, y, z = triplets[i]
            if freq_used[x] or path_used[y] or thresh_used[z]:
                valid = False
                break
            freq_used[x] = 1
            path_used[y] = 1
            thresh_used[z] = 1
            selected_triplets.append((x, y, z))
        
        if valid:
            # Check if all stimuli are used
            if (all(freq_used[i] for i in range(1, k+1)) and 
                all(path_used[i] for i in range(1, k+1)) and 
                all(thresh_used[i] for i in range(1, k+1))):
                print("YES")
                for triplet in selected_triplets:
                    print(triplet[0], triplet[1], triplet[2])
                return
    
    print("NO")

solve()