import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        k = int(next(iterator))
        t = int(next(iterator))
    except StopIteration:
        return
    
    # Maps to store the unique cruiser for each captain and vice versa
    captain_to_cruiser = {}
    cruiser_to_captain = {}
    
    # List to store all configurations
    configs = []
    
    # Adjacency list for the bipartite graph: captain -> list of sectors
    adj = [[] for _ in range(k + 1)]
    
    for _ in range(t):
        c = int(next(iterator))
        v = int(next(iterator))
        s = int(next(iterator))
        
        # Record the hardware binding
        if c not in captain_to_cruiser:
            captain_to_cruiser[c] = v
            cruiser_to_captain[v] = c
        
        configs.append((c, v, s))
        adj[c].append(s)
    
    # If not all captains are present, mobilization is impossible
    if len(captain_to_cruiser) != k:
        print("NO")
        return
    
    # Bipartite matching between captains (left) and sectors (right)
    # matchR[s] stores the captain matched to sector s
    matchR = [0] * (k + 1)
    
    def bfs():
        dist = [-1] * (k + 1)
        queue = deque()
        for u in range(1, k + 1):
            if pairU[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = -1
        
        found_augmenting_path = False
        while queue:
            u = queue.popleft()
            for s in adj[u]:
                v = matchR[s]
                if v != 0:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        queue.append(v)
                else:
                    if not found_augmenting_path:
                        found_augmenting_path = True
        return dist
    
    def dfs(u):
        for s in adj[u]:
            v = matchR[s]
            if v == 0 or (dist[v] == dist[u] + 1 and dfs(v)):
                matchR[s] = u
                pairU[u] = s
                return True
        dist[u] = -1
        return False
    
    pairU = [0] * (k + 1)
    matching = 0
    
    while True:
        dist = bfs()
        if not dist:
            break
        
        for u in range(1, k + 1):
            if pairU[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching != k:
        print("NO")
        return
    
    print("YES")
    
    # Output the selected configurations
    # matchR[s] gives the captain assigned to sector s
    # We need to find the cruiser for that captain and verify the triplet exists
    for s in range(1, k + 1):
        c = matchR[s]
        v = captain_to_cruiser[c]
        print(f"{c} {v} {s}")

if __name__ == "__main__":
    solve()