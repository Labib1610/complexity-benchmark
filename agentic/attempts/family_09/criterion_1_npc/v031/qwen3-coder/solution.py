import sys
from itertools import combinations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    # Build adjacency list for dangerous reactions
    adj = [set() for _ in range(n + 1)]
    idx = 3
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        adj[u].add(v)
        adj[v].add(u)
        idx += 2
    
    # If k == 1, just pick any compound
    if k == 1:
        print("YES")
        print(1)
        return
    
    # For small n, we can check all combinations
    # But since n up to 46, we need a smarter approach
    # We'll use meet-in-the-middle for larger cases
    
    if n <= 25:
        # Brute-force for smaller n
        compounds = list(range(1, n + 1))
        for combo in combinations(compounds, k):
            valid = True
            combo_list = list(combo)
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
    else:
        # Meet-in-the-middle approach
        mid = n // 2
        left_compounds = list(range(1, mid + 1))
        right_compounds = list(range(mid + 1, n + 1))
        
        # Generate all subsets of left and right parts
        left_subsets = []
        for i in range(1 << len(left_compounds)):
            subset = []
            for j in range(len(left_compounds)):
                if i & (1 << j):
                    subset.append(left_compounds[j])
            left_subsets.append(subset)
            
        right_subsets = []
        for i in range(1 << len(right_compounds)):
            subset = []
            for j in range(len(right_compounds)):
                if i & (1 << j):
                    subset.append(right_compounds[j])
            right_subsets.append(subset)
        
        # Map each valid left subset to its size
        left_valid = {}
        for subset in left_subsets:
            valid = True
            for i in range(len(subset)):
                for j in range(i+1, len(subset)):
                    if subset[j] in adj[subset[i]]:
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                size = len(subset)
                if size not in left_valid:
                    left_valid[size] = []
                left_valid[size].append(set(subset))
        
        # Map each valid right subset to its size
        right_valid = {}
        for subset in right_subsets:
            valid = True
            for i in range(len(subset)):
                for j in range(i+1, len(subset)):
                    if subset[j] in adj[subset[i]]:
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                size = len(subset)
                if size not in right_valid:
                    right_valid[size] = []
                right_valid[size].append(set(subset))
        
        # Check all combinations of left and right sizes that sum to k
        for left_size in range(k + 1):
            right_size = k - left_size
            if left_size in left_valid and right_size in right_valid:
                for left_set in left_valid[left_size]:
                    for right_set in right_valid[right_size]:
                        # Check if there's any edge between left and right sets
                        conflict = False
                        for u in left_set:
                            for v in right_set:
                                if v in adj[u]:
                                    conflict = True
                                    break
                            if conflict:
                                break
                        if not conflict:
                            result = sorted(list(left_set) + list(right_set))
                            print("YES")
                            print(' '.join(map(str, result)))
                            return
        
        print("NO")

if __name__ == "__main__":
    main()