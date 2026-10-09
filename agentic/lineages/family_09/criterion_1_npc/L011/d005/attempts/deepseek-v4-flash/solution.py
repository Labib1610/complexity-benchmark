import sys

def main():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    # Try to find independent set of size k
    # Use backtracking with pruning
    # We'll try to pick vertices in order
    
    # Precompute possible candidates for each position
    # Use recursion
    
    # For n <= 46, we can use meet-in-the-middle:
    # Split vertices into two halves, find all independent sets in each half,
    # then combine.
    
    left_n = n // 2
    right_n = n - left_n
    
    left_adj = [0] * left_n
    right_adj = [0] * right_n
    for i in range(left_n):
        for j in range(left_n):
            if (adj[i] >> j) & 1:
                left_adj[i] |= (1 << j)
    for i in range(right_n):
        for j in range(right_n):
            if (adj[left_n + i] >> (left_n + j)) & 1:
                right_adj[i] |= (1 << j)
    
    # Generate all independent sets for left half
    left_sets = {}  # size -> list of (mask, vertices)
    for mask in range(1 << left_n):
        ok = True
        for i in range(left_n):
            if (mask >> i) & 1:
                if (left_adj[i] & mask) != 0:
                    ok = False
                    break
        if ok:
            size = bin(mask).count('1')
            left_sets.setdefault(size, []).append(mask)
    
    # Generate all independent sets for right half
    right_sets = {}
    for mask in range(1 << right_n):
        ok = True
        for i in range(right_n):
            if (mask >> i) & 1:
                if (right_adj[i] & mask) != 0:
                    ok = False
                    break
        if ok:
            size = bin(mask).count('1')
            right_sets.setdefault(size, []).append(mask)
    
    # For each left mask, compute which right vertices are forbidden
    # For each left mask, we can combine with right masks that have no edges to left
    
    # Precompute for each left mask the forbidden right mask
    forbidden_right = {}
    for lmask in range(1 << left_n):
        forb = 0
        for i in range(left_n):
            if (lmask >> i) & 1:
                # add right neighbors of i
                for j in range(right_n):
                    if (adj[i] >> (left_n + j)) & 1:
                        forb |= (1 << j)
        forbidden_right[lmask] = forb
    
    # Now search for combination
    for lsize in range(max(0, k - right_n), min(k, left_n) + 1):
        rsize = k - lsize
        if lsize not in left_sets or rsize not in right_sets:
            continue
        for lmask in left_sets[lsize]:
            forb = forbidden_right[lmask]
            for rmask in right_sets[rsize]:
                if (rmask & forb) == 0:
                    # Found
                    panel = []
                    for i in range(left_n):
                        if (lmask >> i) & 1:
                            panel.append(i + 1)
                    for j in range(right_n):
                        if (rmask >> j) & 1:
                            panel.append(left_n + j + 1)
                    print("YES")
                    print(" ".join(map(str, panel)))
                    return
    
    print("NO")

if __name__ == "__main__":
    main()