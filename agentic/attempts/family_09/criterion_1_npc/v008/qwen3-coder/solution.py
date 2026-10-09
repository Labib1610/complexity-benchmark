from itertools import combinations
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n, m, k = map(int, data[:3])
    edges = []
    idx = 3
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        edges.append((u, v))
        idx += 2
    
    # Create adjacency set for quick lookup
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # Special case: k == 1
    if k == 1:
        print("YES")
        print(1)
        return
    
    # Generate all combinations of k nodes and check if they form an independent set
    # For efficiency, we'll use a meet-in-the-middle approach for larger n
    if n <= 25:
        # Brute force for smaller n
        for combo in combinations(range(n), k):
            valid = True
            for i in range(k):
                for j in range(i+1, k):
                    u = combo[i]
                    v = combo[j]
                    if v in adj[u]:
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                print("YES")
                print(' '.join(str(x+1) for x in combo))
                return
        print("NO")
    else:
        # Meet-in-the-middle approach for larger n
        mid = n // 2
        left_nodes = list(range(mid))
        right_nodes = list(range(mid, n))
        
        # Precompute all independent sets in the left half
        left_sets = []
        # We only need sets of size up to k
        def generate_left(subset, start, max_size):
            if len(subset) > max_size:
                return
            if len(subset) <= max_size:
                left_sets.append(subset[:])
            for i in range(start, len(left_nodes)):
                # Check if node i can be added
                valid_add = True
                for node in subset:
                    if left_nodes[i] in adj[node]:
                        valid_add = False
                        break
                if valid_add:
                    subset.append(left_nodes[i])
                    generate_left(subset, i+1, max_size)
                    subset.pop()
        
        generate_left([], 0, k)
        
        # Map each left set to its neighbors in the right part
        left_map = {}
        for s in left_sets:
            neighbors = set()
            for node in s:
                neighbors.update(adj[node])
            key = tuple(s)
            left_map[key] = neighbors
        
        # Now iterate over subsets of right nodes
        def generate_right(subset, start, max_size):
            if len(subset) > max_size:
                return []
            res = [subset[:]]
            for i in range(start, len(right_nodes)):
                # Check if node i can be added
                valid_add = True
                for node in subset:
                    if right_nodes[i] in adj[node]:
                        valid_add = False
                        break
                if valid_add:
                    subset.append(right_nodes[i])
                    res.extend(generate_right(subset, i+1, max_size))
                    subset.pop()
            return res
        
        right_subsets = generate_right([], 0, k)
        
        # Check all combinations
        for r_subset in right_subsets:
            r_set = set(r_subset)
            # Check if r_subset itself is independent
            valid_r = True
            for i in range(len(r_subset)):
                for j in range(i+1, len(r_subset)):
                    if r_subset[j] in adj[r_subset[i]]:
                        valid_r = False
                        break
                if not valid_r:
                    break
            if not valid_r:
                continue
            
            r_neighbors = set()
            for node in r_subset:
                r_neighbors.update(adj[node])
            
            r_size = len(r_subset)
            needed = k - r_size
            if needed < 0:
                continue
            if needed == 0:
                # Check if this subset has no edges within
                print("YES")
                print(' '.join(str(x+1) for x in sorted(r_subset)))
                return
            # Look for a left subset of size 'needed' that doesn't conflict
            for l_key, l_neighbors in left_map.items():
                l_subset = list(l_key)
                if len(l_subset) != needed:
                    continue
                # Check if any node in l_subset is adjacent to any node in r_subset
                conflict = False
                for l_node in l_subset:
                    if l_node in r_neighbors:
                        conflict = True
                        break
                if conflict:
                    continue
                # Also check if l_subset has internal edges with r_subset  
                # Actually, since both are independent sets, we just need to ensure 
                # no edge between them
                print("YES")
                result = sorted([x+1 for x in l_subset + r_subset])
                print(' '.join(map(str, result)))
                return
        
        print("NO")

if __name__ == "__main__":
    main()