import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n, m, k = map(int, data[:3])
    conflict = [[False] * n for _ in range(n)]
    idx = 3
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        idx += 2
        conflict[u][v] = True
        conflict[v][u] = True

    # Build adjacency for "no conflict"
    adj = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and not conflict[i][j]:
                adj[i][j] = True

    # If k == 1, always possible
    if k == 1:
        print("YES")
        print(1)
        return

    # Backtracking to find clique of size k
    candidates = list(range(n))
    clique = []

    def backtrack(start, clique):
        if len(clique) == k:
            return True
        # Prune: not enough remaining vertices
        if len(clique) + (n - start) < k:
            return False
        for i in range(start, n):
            # Check if i is connected to all in clique
            ok = True
            for v in clique:
                if not adj[i][v]:
                    ok = False
                    break
            if ok:
                clique.append(i)
                if backtrack(i + 1, clique):
                    return True
                clique.pop()
        return False

    if backtrack(0, clique):
        print("YES")
        print(" ".join(str(x + 1) for x in clique))
    else:
        print("NO")

if __name__ == "__main__":
    main()