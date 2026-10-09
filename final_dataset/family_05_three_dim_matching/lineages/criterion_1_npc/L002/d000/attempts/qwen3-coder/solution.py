from itertools import permutations

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    triplets = []
    index = 2
    for _ in range(t):
        m = int(data[index])
        p = int(data[index+1])
        s = int(data[index+2])
        triplets.append((m, p, s))
        index += 3
    
    # We need to find a permutation of k triplets such that:
    # - All membranes are 1..k each used exactly once
    # - All pathways are 1..k each used exactly once
    # - All sequences are 1..k each used exactly once
    
    # This is essentially finding a perfect matching in a 3-dimensional bipartite graph
    # Since k <= 22, we can try all permutations for small k, but that's too much.
    # Better approach: model as a matching problem or use backtracking with pruning.
    
    # Let's use backtracking with bitmasks for efficiency
    
    # Precompute which triplets involve each component
    mem_usage = [[] for _ in range(k + 1)]  # mem_usage[m] = list of indices of triplets using membrane m
    path_usage = [[] for _ in range(k + 1)]
    seq_usage = [[] for _ in range(k + 1)]
    
    for i in range(t):
        m, p, s = triplets[i]
        mem_usage[m].append(i)
        path_usage[p].append(i)
        seq_usage[s].append(i)
    
    # Backtracking: try to build a solution
    selected = []
    mem_used = [False] * (k + 1)
    path_used = [False] * (k + 1)
    seq_used = [False] * (k + 1)
    
    def backtrack(pos):
        if pos == k:
            return True
            
        # Try each triplet that hasn't been ruled out yet
        # For efficiency, try triplets that use currently needed membranes, etc.
        # But let's just iterate through all triplets and check constraints
        
        for i in range(t):
            m, p, s = triplets[i]
            if not mem_used[m] and not path_used[p] and not seq_used[s]:
                # Check if this triplet can be part of a solution
                # (i.e., there exist enough remaining triplets to cover remaining items)
                # This is complex to check precisely, so we'll just proceed and backtrack
                
                selected.append(i)
                mem_used[m] = True
                path_used[p] = True
                seq_used[s] = True
                
                if backtrack(pos + 1):
                    return True
                    
                selected.pop()
                mem_used[m] = False
                path_used[p] = False
                seq_used[s] = False
        
        return False
    
    # Optimization: sort triplets by frequency or some heuristic?
    
    if backtrack(0):
        print("YES")
        for idx in selected:
            m, p, s = triplets[idx]
            print(m, p, s)
    else:
        print("NO")

solve()