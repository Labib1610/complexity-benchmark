import sys
import itertools

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    edges = []
    adj = [[] for _ in range(n)]
    for _ in range(m):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        edges.append((x, y))
        adj[x].append(y)
        adj[y].append(x)
    
    # If n is small, brute force all permutations
    if n <= 10:
        best_perm = None
        for perm in itertools.permutations(range(n)):
            pos = [0] * n
            for idx, val in enumerate(perm):
                pos[val] = idx
            cost = 0
            for u, v in edges:
                cost += abs(pos[u] - pos[v])
                if cost > B:
                    break
            if cost <= B:
                best_perm = perm
                break
        if best_perm is None:
            print("NO")
        else:
            print("YES")
            print(' '.join(str(p + 1) for p in best_perm))
    else:
        # Fallback: greedy heuristic (e.g., BFS ordering)
        # This is not guaranteed optimal, but we try.
        # For larger n, we can use a simple constructive heuristic.
        # We'll try to place high-degree nodes in center.
        from collections import deque
        # Simple heuristic: sort by degree descending, place in center
        deg = [len(adj[i]) for i in range(n)]
        order = sorted(range(n), key=lambda x: -deg[x])
        # Place in order: center out
        perm = [0] * n
        left = (n - 1) // 2
        right = left + 1
        # Fill from center outward
        idx = 0
        for i in range(left, -1, -1):
            perm[i] = order[idx]
            idx += 1
        for i in range(left + 1, n):
            perm[i] = order[idx]
            idx += 1
        # perm is position -> module
        pos = [0] * n
        for p, mod in enumerate(perm):
            pos[mod] = p
        cost = sum(abs(pos[u] - pos[v]) for u, v in edges)
        if cost <= B:
            print("YES")
            print(' '.join(str(p + 1) for p in perm))
        else:
            # Try reverse
            perm = perm[::-1]
            pos = [0] * n
            for p, mod in enumerate(perm):
                pos[mod] = p
            cost = sum(abs(pos[u] - pos[v]) for u, v in edges)
            if cost <= B:
                print("YES")
                print(' '.join(str(p + 1) for p in perm))
            else:
                print("NO")

if __name__ == "__main__":
    main()