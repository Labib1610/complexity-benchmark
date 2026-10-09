import sys
from itertools import combinations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    edges = []
    adj = [set() for _ in range(n+1)]
    
    idx = 3
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # If m == 0, any combination of k variables will result in f = 0
    if m == 0:
        print("YES")
        print(' '.join(map(str, range(1, k+1))))
        return
    
    # For small n, we can check all combinations
    if n <= 20:
        for comb in combinations(range(1, n+1), k):
            selected = set(comb)
            total = 0
            for u, v in edges:
                if u in selected and v in selected:
                    total += 1
            if total == 0:
                print("YES")
                print(' '.join(map(str, comb)))
                return
        print("NO")
        return
    
    # For larger n, use meet-in-the-middle approach
    mid = n // 2
    left_vars = list(range(1, mid+1))
    right_vars = list(range(mid+1, n+1))
    
    # Precompute for all subsets of left_vars with size i
    left_subsets = {}
    for i in range(min(k+1, len(left_vars)+1)):
        left_subsets[i] = []
        for comb in combinations(left_vars, i):
            count = 0
            selected = set(comb)
            for u, v in edges:
                if u in selected and v in selected:
                    count += 1
            left_subsets[i].append((set(comb), count))
    
    # Precompute for all subsets of right_vars with size i
    right_subsets = {}
    for i in range(min(k+1, len(right_vars)+1)):
        right_subsets[i] = []
        for comb in combinations(right_vars, i):
            count = 0
            selected = set(comb)
            for u, v in edges:
                if u in selected and v in selected:
                    count += 1
            right_subsets[i].append((set(comb), count))
    
    # Now check all valid splits
    for left_size in range(min(k+1, len(left_vars)+1)):
        right_size = k - left_size
        if right_size < 0 or right_size > len(right_vars):
            continue
        
        # Get all left subsets of size left_size
        if left_size not in left_subsets:
            continue
        # Get all right subsets of size right_size
        if right_size not in right_subsets:
            continue
            
        for left_set, left_count in left_subsets[left_size]:
            for right_set, right_count in right_subsets[right_size]:
                # Count cross edges between left_set and right_set
                cross_count = 0
                for u in left_set:
                    for v in adj[u]:
                        if v in right_set:
                            cross_count += 1
                
                total = left_count + right_count + cross_count
                if total == 0:
                    result = list(left_set) + list(right_set)
                    print("YES")
                    print(' '.join(map(str, result)))
                    return
                    
    print("NO")

if __name__ == "__main__":
    main()