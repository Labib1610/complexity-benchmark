import sys
from itertools import combinations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    edge_set = set()
    adj = [set() for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        if u > v:
            u, v = v, u
        edges.append((u, v))
        edge_set.add((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Function to check if a triplet is locked
    def is_locked(a, b, c):
        # Get all edges among a, b, c
        edges_present = 0
        if (a, b) in edge_set or (b, a) in edge_set:
            edges_present += 1
        if (a, c) in edge_set or (c, a) in edge_set:
            edges_present += 1
        if (b, c) in edge_set or (c, b) in edge_set:
            edges_present += 1
        
        # If no edges, defect can be 0 (all different), so not locked
        if edges_present == 0:
            return False
            
        # If all edges present, every mapping has at least one edge with same values
        # For 3 nodes, there are 2^3 = 8 mappings
        # Only mappings with all different values have defect 0: impossible for 3 nodes
        # Actually, for 3 nodes, mappings with all different values: 001, 010, 100, etc.
        # But with 3 nodes, we can't assign all three different values from {0,1}
        # So mappings where all are same: 000, 111 => defect = 3
        # Mappings with two same: 001, 010, 100, 110, 101, 011 => defect >=1
        # Only mappings with all different: impossible with binary values on 3 nodes
        # So for 3 nodes, defect is always > 0 if at least one edge exists
        if edges_present == 3:
            return True
            
        # For 1 or 2 edges, check if all 8 mappings give defect > 0
        # Enumerate all mappings: 000, 001, 010, 011, 100, 101, 110, 111
        mappings = [
            {a:0, b:0, c:0},
            {a:0, b:0, c:1},
            {a:0, b:1, c:0},
            {a:0, b:1, c:1},
            {a:1, b:0, c:0},
            {a:1, b:0, c:1},
            {a:1, b:1, c:0},
            {a:1, b:1, c:1}
        ]
        
        for mapping in mappings:
            defect = 0
            if (a, b) in edge_set and mapping[a] == mapping[b]:
                defect += 1
            if (a, c) in edge_set and mapping[a] == mapping[c]:
                defect += 1
            if (b, c) in edge_set and mapping[b] == mapping[c]:
                defect += 1
            if defect == 0:
                return False  # Found a mapping with defect 0
        return True  # All mappings have defect > 0

    # Iterate through all triplets in lexicographical order
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                if is_locked(a, b, c):
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()