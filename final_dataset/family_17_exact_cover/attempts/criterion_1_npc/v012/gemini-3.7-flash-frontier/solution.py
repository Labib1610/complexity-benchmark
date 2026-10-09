import sys

# Increase recursion depth for deep search trees
sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    q = int(input_data[0])
    t = int(input_data[1])
    
    n = 3 * q
    triplets = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        c = int(input_data[idx + 2])
        idx += 3
        triplets.append((a, b, c))
        
    cand = [[] for _ in range(n + 1)]
    for i, (a, b, c) in enumerate(triplets):
        cand[a].append(i)
        cand[b].append(i)
        cand[c].append(i)
        
    for x in range(1, n + 1):
        if not cand[x]:
            print("NO")
            return

    used = [False] * (n + 1)
    selected = []

    def backtrack(remaining):
        if remaining == 0:
            return True
        
        # Choose the uncovered element with the fewest valid candidate sets
        best_x = -1
        best_valid_sets = None
        min_count = float('inf')
        
        for x in range(1, n + 1):
            if not used[x]:
                valid_sets = []
                for s_idx in cand[x]:
                    a, b, c = triplets[s_idx]
                    if not used[a] and not used[b] and not used[c]:
                        valid_sets.append(s_idx)
                
                count = len(valid_sets)
                if count == 0:
                    return False
                if count < min_count:
                    min_count = count
                    best_x = x
                    best_valid_sets = valid_sets
                    if min_count == 1:
                        break
        
        for s_idx in best_valid_sets:
            a, b, c = triplets[s_idx]
            if not used[a] and not used[b] and not used[c]:
                used[a] = used[b] = used[c] = True
                selected.append(s_idx)
                if backtrack(remaining - 3):
                    return True
                selected.pop()
                used[a] = used[b] = used[c] = False
                
        return False

    if backtrack(n):
        print("YES")
        for s_idx in selected:
            a, b, c = triplets[s_idx]
            print(f"{a} {b} {c}")
    else:
        print("NO")

if __name__ == '__main__':
    solve()