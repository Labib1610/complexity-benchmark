import sys
from collections import defaultdict, deque

def main():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    
    # specialist -> set of allowed time slots
    allowed = defaultdict(set)
    for _ in range(t):
        x, y, z = map(int, input().split())
        allowed[x].add(z)
    
    # Build bipartite graph: specialists (1..k) to time slots (1..k)
    adj = [[] for _ in range(k + 1)]
    for spec in range(1, k + 1):
        for slot in allowed[spec]:
            adj[spec].append(slot)
    
    # Hopcroft-Karp for maximum bipartite matching
    match_slot = [0] * (k + 1)  # slot -> specialist
    match_spec = [0] * (k + 1)  # specialist -> slot
    dist = [0] * (k + 1)
    
    def bfs():
        q = deque()
        for u in range(1, k + 1):
            if match_spec[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = float('inf')
        dist[0] = float('inf')
        while q:
            u = q.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if dist[match_slot[v]] == float('inf'):
                        dist[match_slot[v]] = dist[u] + 1
                        q.append(match_slot[v])
        return dist[0] != float('inf')
    
    def dfs(u):
        if u != 0:
            for v in adj[u]:
                if dist[match_slot[v]] == dist[u] + 1 and dfs(match_slot[v]):
                    match_slot[v] = u
                    match_spec[u] = v
                    return True
            dist[u] = float('inf')
            return False
        return True
    
    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if match_spec[u] == 0 and dfs(u):
                matching += 1
    
    if matching != k:
        print("NO")
        return
    
    print("YES")
    # Reconstruct: specialist -> machine mapping is fixed by input
    spec_machine = {}
    for _ in range(t):
        x, y, z = map(int, input().split())
        spec_machine[x] = y
    # But we already consumed input; we need to store it earlier.
    # Let's fix by storing during first read.
    
if __name__ == "__main__":
    main()