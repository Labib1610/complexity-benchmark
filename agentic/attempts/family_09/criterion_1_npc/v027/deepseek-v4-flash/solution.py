import sys

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    # Try to find an independent set of size k
    # Use backtracking with pruning
    # We'll store vertices in order of degree for better pruning
    vertices = list(range(n))
    vertices.sort(key=lambda x: adj[x].bit_count())
    
    chosen = []
    
    def backtrack(start, chosen_mask, chosen_count):
        if chosen_count == k:
            return True
        # Prune: if not enough remaining vertices
        if n - start < k - chosen_count:
            return False
        for i in range(start, n):
            v = vertices[i]
            if (chosen_mask & adj[v]) == 0:
                chosen.append(v + 1)
                if backtrack(i + 1, chosen_mask | (1 << v), chosen_count + 1):
                    return True
                chosen.pop()
        return False
    
    if backtrack(0, 0, 0):
        print("YES")
        print(" ".join(map(str, chosen)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()