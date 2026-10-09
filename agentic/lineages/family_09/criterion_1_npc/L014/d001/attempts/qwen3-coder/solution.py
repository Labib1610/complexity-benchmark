from itertools import combinations

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    # Read edges and build adjacency list
    adj = [set() for _ in range(n+1)]
    index = 3
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        adj[u].add(v)
        adj[v].add(u)
        index += 2
    
    # Try all combinations of k nodes
    nodes = list(range(1, n+1))
    
    # Special case: k=1
    if k == 1:
        print("YES")
        print(1)
        return
    
    # For larger k, try combinations
    for combo in combinations(nodes, k):
        valid = True
        combo_list = list(combo)
        # Check all pairs in this combination
        for i in range(len(combo_list)):
            for j in range(i+1, len(combo_list)):
                if combo_list[j] in adj[combo_list[i]]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            print("YES")
            print(' '.join(map(str, combo_list)))
            return
    
    print("NO")

solve()