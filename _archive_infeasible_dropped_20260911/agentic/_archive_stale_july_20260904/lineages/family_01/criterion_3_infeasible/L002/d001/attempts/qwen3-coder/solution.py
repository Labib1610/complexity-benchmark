import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    index = 2
    conflicts = set()
    adj = defaultdict(set)
    
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        if u > v:
            u, v = v, u
        conflicts.add((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Convert sets to lists for faster intersection
    adj_list = {}
    for node in adj:
        adj_list[node] = list(adj[node])
    
    # Iterate through all possible triplets (i, j, k) in lexicographical order
    for i in range(1, n+1):
        if i not in adj_list:
            continue
        neighbors_i = adj_list[i]
        for idx_j in range(len(neighbors_i)):
            j = neighbors_i[idx_j]
            if j <= i:
                continue
            if j not in adj_list:
                continue
            neighbors_j = adj_list[j]
            # Use two pointers or set intersection to find common neighbors
            # But since we want the lexicographically smallest, we iterate normally
            for k in neighbors_j:
                if k <= j:
                    continue
                # Check if (i,k) and (j,k) are conflicts
                if (i, k) in conflicts and (j, k) in conflicts:
                    print(i, j, k)
                    return

if __name__ == "__main__":
    main()