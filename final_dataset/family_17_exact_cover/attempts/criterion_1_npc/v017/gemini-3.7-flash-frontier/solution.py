import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    q = int(input_data[0])
    t = int(input_data[1])
    
    idx = 2
    raw_triplets = []
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        raw_triplets.append((a, b, c))
    
    # Remove duplicates
    triplets = list(set(raw_triplets))
    num_triplets = len(triplets)
    
    n = 3 * q
    # element -> list of triplet indices
    elem_to_triplets = [[] for _ in range(n + 1)]
    for i, (a, b, c) in enumerate(triplets):
        elem_to_triplets[a].append(i)
        elem_to_triplets[b].append(i)
        elem_to_triplets[c].append(i)
    
    # Check if any element has 0 triplets
    for i in range(1, n + 1):
        if not elem_to_triplets[i]:
            print("NO")
            return

    covered = [False] * (n + 1)
    # Count of valid sets per element (can be dynamically pruned or checked)
    # Using simple recursive backtracking with MRV:
    solution = []
    
    # Find uncovered elements
    # We can maintain an active set/list of uncovered elements
    uncovered = set(range(1, n + 1))
    
    def search():
        if not uncovered:
            return True
        
        # MRV: pick element in uncovered with fewest available valid triplets
        best_elem = -1
        best_count = float('inf')
        best_triplets = []
        
        for elem in uncovered:
            # count valid triplets
            valid = []
            for t_idx in elem_to_triplets[elem]:
                a, b, c = triplets[t_idx]
                if (not covered[a]) and (not covered[b]) and (not covered[c]):
                    valid.append(t_idx)
            
            cnt = len(valid)
            if cnt == 0:
                return False
            if cnt < best_count:
                best_count = cnt
                best_elem = elem
                best_triplets = valid
                if cnt == 1:
                    break
        
        for t_idx in best_triplets:
            a, b, c = triplets[t_idx]
            # Check again because previous loop iterations in this frame might have changed state?
            # No, state is restored after recursion. But other elements in best_triplets might overlap with nothing since they share best_elem which is currently uncovered.
            # However, a, b, c must all be uncovered.
            if covered[a] or covered[b] or covered[c]:
                continue
            
            # Apply
            covered[a] = covered[b] = covered[c] = True
            uncovered.remove(a)
            uncovered.remove(b)
            uncovered.remove(c)
            solution.append(t_idx)
            
            if search():
                return True
            
            # Revert
            solution.pop()
            uncovered.add(a)
            uncovered.add(b)
            uncovered.add(c)
            covered[a] = covered[b] = covered[c] = False
            
        return False

    sys.setrecursionlimit(2000)
    if search():
        print("YES")
        for t_idx in solution:
            a, b, c = triplets[t_idx]
            print(f"{a} {b} {c}")
    else:
        print("NO")

if __name__ == '__main__':
    solve()