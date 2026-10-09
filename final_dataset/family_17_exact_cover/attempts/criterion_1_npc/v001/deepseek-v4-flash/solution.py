import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    n = 3 * q
    groups = []
    for _ in range(t):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        c = int(next(it)) - 1
        groups.append((a, b, c))
    
    # Build adjacency: for each operator, list of group indices containing it
    adj = [[] for _ in range(n)]
    for idx, (a, b, c) in enumerate(groups):
        adj[a].append(idx)
        adj[b].append(idx)
        adj[c].append(idx)
    
    used = [False] * t
    chosen = []
    covered = 0
    
    # We'll use a recursive backtracking with heuristic: pick the operator with fewest available groups
    def backtrack():
        nonlocal covered
        if covered == n:
            return True
        # Find operator with smallest number of available groups
        best_op = -1
        best_count = 10**9
        for op in range(n):
            if (covered >> op) & 1:
                continue
            cnt = 0
            for gi in adj[op]:
                if not used[gi]:
                    cnt += 1
            if cnt < best_count:
                best_count = cnt
                best_op = op
                if cnt == 0:
                    break
        if best_count == 0:
            return False
        
        # Try groups covering best_op
        for gi in adj[best_op]:
            if used[gi]:
                continue
            a, b, c = groups[gi]
            if (covered >> a) & 1 or (covered >> b) & 1 or (covered >> c) & 1:
                continue
            # Use this group
            used[gi] = True
            chosen.append(gi)
            covered |= (1 << a) | (1 << b) | (1 << c)
            if backtrack():
                return True
            # Undo
            covered &= ~((1 << a) | (1 << b) | (1 << c))
            chosen.pop()
            used[gi] = False
        return False
    
    if backtrack():
        print("YES")
        for gi in chosen:
            a, b, c = groups[gi]
            print(a+1, b+1, c+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()