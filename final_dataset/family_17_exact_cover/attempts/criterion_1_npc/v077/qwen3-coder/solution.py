from collections import defaultdict
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    if t < q:
        print("NO")
        return
    
    triplets = []
    index = 2
    for _ in range(t):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        triplets.append((a, b, c))
        index += 3
    
    # Build a graph where each node is a channel (1 to 3*q)
    # and edges represent which triplets contain that channel
    channel_to_triplets = defaultdict(list)
    for i in range(t):
        a, b, c = triplets[i]
        channel_to_triplets[a].append(i)
        channel_to_triplets[b].append(i)
        channel_to_triplets[c].append(i)
    
    # Try to model this as a matching problem
    # We want to select exactly q triplets such that each channel (1 to 3*q) is in exactly one triplet
    # This is equivalent to finding a perfect matching in a 3-uniform hypergraph where each hyperedge is a triplet
    
    # This is essentially the Exact Cover problem, which can be solved with Algorithm X / Dancing Links
    # But given the constraints (q <= 200), we can try a backtracking approach with optimizations
    
    # Let's use a greedy + backtracking approach
    
    # First, let's see if we can model it as a graph matching problem
    # Actually, since each triplet covers exactly 3 nodes and we need to cover 3*q nodes with q triplets,
    # this is a exact cover problem.
    
    # Use backtracking with pruning
    selected = [False] * t  # whether triplet i is selected
    covered = [False] * (3*q + 1)  # whether channel j is covered
    result = []
    
    def backtrack(pos):
        # If we've selected q triplets, check if all channels are covered
        if len(result) == q:
            # Check if all channels 1 to 3*q are covered
            for j in range(1, 3*q + 1):
                if not covered[j]:
                    return False
            return True
        
        # Pruning: if remaining positions cannot cover all, return False
        if len(result) + (t - pos) < q:
            return False
            
        # Try selecting triplets from position pos onwards
        for i in range(pos, t):
            a, b, c = triplets[i]
            # If any of a, b, c is already covered, skip this triplet
            if covered[a] or covered[b] or covered[c]:
                continue
                
            # Select this triplet
            selected[i] = True
            covered[a] = covered[b] = covered[c] = True
            result.append(i)
            
            if backtrack(i + 1):
                return True
                
            # Backtrack
            selected[i] = False
            covered[a] = covered[b] = covered[c] = False
            result.pop()
        
        return False
    
    # Optimization: sort triplets by some heuristic, e.g., by the minimum channel they contain
    # This might help in pruning earlier
    # But for now, let's just run the backtracking
    
    if backtrack(0):
        print("YES")
        for idx in result:
            a, b, c = triplets[idx]
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    main()