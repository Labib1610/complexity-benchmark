import sys
from itertools import permutations

def total_length(perm, edges, n):
    pos = [0] * (n + 1)
    for i, p in enumerate(perm, 1):
        pos[p] = i
    total = 0
    for u, v in edges:
        total += abs(pos[u] - pos[v])
    return total

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n, m, B = map(int, data[:3])
    edges = []
    idx = 3
    for _ in range(m):
        u, v = int(data[idx]), int(data[idx+1])
        edges.append((u, v))
        idx += 2

    # Greedy: place high-degree nodes first, then neighbors
    from collections import defaultdict, deque
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    degree = {i: len(adj[i]) for i in range(1, n+1)}
    # Sort by degree descending
    order = sorted(range(1, n+1), key=lambda x: -degree[x])

    pos = [0] * (n + 1)
    used = [False] * (n + 1)
    # Place first node at position 1
    pos[order[0]] = 1
    used[1] = True
    next_pos = 2

    # BFS-like placement
    placed = {order[0]}
    queue = deque([order[0]])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if v not in placed:
                # place v at next available position
                while next_pos <= n and used[next_pos]:
                    next_pos += 1
                if next_pos > n:
                    break
                pos[v] = next_pos
                used[next_pos] = True
                next_pos += 1
                placed.add(v)
                queue.append(v)

    # If some nodes not placed (disconnected), place them anywhere
    for i in range(1, n+1):
        if pos[i] == 0:
            while next_pos <= n and used[next_pos]:
                next_pos += 1
            if next_pos > n:
                break
            pos[i] = next_pos
            used[next_pos] = True
            next_pos += 1

    # Check total length
    total = 0
    for u, v in edges:
        total += abs(pos[u] - pos[v])
    if total <= B:
        print("YES")
        print(" ".join(str(pos[i]) for i in range(1, n+1)))
        return

    # If greedy fails and n is small, brute force
    if n <= 9:
        for perm in permutations(range(1, n+1)):
            if total_length(perm, edges, n) <= B:
                print("YES")
                print(" ".join(map(str, perm)))
                return

    print("NO")

if __name__ == "__main__":
    solve()