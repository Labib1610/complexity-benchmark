import sys
import heapq

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    indeg = [0] * n
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        adj[a].append(b)
        indeg[b] += 1
    
    # Compute longest path length from each node (for priority)
    # We'll do a reverse topological order using Kahn's algorithm
    rev_adj = [[] for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            rev_adj[v].append(u)
    
    # Compute longest path to end
    outdeg = [len(adj[u]) for u in range(n)]
    queue = [u for u in range(n) if outdeg[u] == 0]
    dist = [0] * n
    while queue:
        u = queue.pop()
        for p in rev_adj[u]:
            if dist[p] < dist[u] + 1:
                dist[p] = dist[u] + 1
            outdeg[p] -= 1
            if outdeg[p] == 0:
                queue.append(p)
    
    # Kahn's algorithm with capacity
    heap = []
    for i in range(n):
        if indeg[i] == 0:
            heapq.heappush(heap, (-dist[i], i))
    
    slot = [0] * n
    for t in range(1, T + 1):
        if not heap:
            break
        count = 0
        temp = []
        while heap and count < M:
            neg_d, u = heapq.heappop(heap)
            slot[u] = t
            count += 1
            temp.append(u)
        for u in temp:
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    heapq.heappush(heap, (-dist[v], v))
    
    if any(s == 0 for s in slot):
        print("NO")
    else:
        print("YES")
        print(" ".join(str(s) for s in slot))

if __name__ == "__main__":
    solve()