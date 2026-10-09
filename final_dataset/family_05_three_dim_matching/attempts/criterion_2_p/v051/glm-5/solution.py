import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # For each scholar x, list of (manuscript z, proposal_index)
    scholar_proposals = [[] for _ in range(k + 1)]
    
    for i in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        scholar_proposals[x].append((z, i))
    
    # Build bipartite graph: left = scholars, right = manuscripts
    # Edge from scholar x to manuscript z if there's a proposal (x, y, z)
    # Since each scholar has exactly one archive, matching scholar->manuscript
    # automatically determines the archive.
    
    # Hopcroft-Karp for maximum bipartite matching
    # Left nodes: 1..k (scholars), Right nodes: 1..k (manuscripts)
    
    adj = [[] for _ in range(k + 1)]
    for x in range(1, k + 1):
        for z, idx in scholar_proposals[x]:
            adj[x].append((z, idx))
    
    # pairU[x] = manuscript matched to scholar x (0 if unmatched)
    # pairV[z] = scholar matched to manuscript z (0 if unmatched)
    pairU = [0] * (k + 1)
    pairV = [0] * (k + 1)
    dist = [0] * (k + 1)
    
    from collections import deque
    
    INF = float('inf')
    
    def bfs():
        queue = deque()
        for u in range(1, k + 1):
            if pairU[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while queue:
            u = queue.popleft()
            if dist[u] < dist[0]:
                for z, idx in adj[u]:
                    v = pairV[z]
                    if dist[v] == INF:
                        dist[v] = dist[u] + 1
                        queue.append(v)
        return dist[0] != INF
    
    def dfs(u):
        if u != 0:
            for z, idx in adj[u]:
                v = pairV[z]
                if dist[v] == dist[u] + 1:
                    if dfs(v):
                        pairV[z] = u
                        pairU[u] = z
                        # Store the proposal index
                        proposal_idx[u] = idx
                        return True
            dist[u] = INF
            return False
        return True
    
    proposal_idx = [0] * (k + 1)
    
    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if pairU[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching == k:
        print("YES")
        # Reconstruct proposals
        # We need to output x, y, z for each approved proposal
        # We stored proposal_idx[u] for each scholar u
        # But we need to re-read or store the proposals
        # Let's re-read from input
        # Actually, let's store proposals during first read
        # We already have scholar_proposals with indices
        # proposal_idx[u] gives the index of the proposal for scholar u
        # But we need x, y, z - we need to store them
        
        # Re-read input to get proposals
        # Actually, let's just store them in a list
        # We'll re-parse
        pass
    else:
        print("NO")
        return
    
    # Re-read to get proposal details
    data2 = sys.stdin.buffer.read().split()
    # Wait, we already consumed the iterator. Let's re-read from the stored data.
    # Actually data is still available.
    it2 = iter(data)
    k2 = int(next(it2))
    t2 = int(next(it2))
    
    proposals = []
    for i in range(t2):
        x = int(next(it2))
        y = int(next(it2))
        z = int(next(it2))
        proposals.append((x, y, z))
    
    out = []
    for u in range(1, k + 1):
        idx = proposal_idx[u]
        x, y, z = proposals[idx]
        out.append(f"{x} {y} {z}")
    
    print("\n".join(out))

def solve2():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    proposals = []
    # adj[x] = list of (z, proposal_index)
    adj = [[] for _ in range(k + 1)]
    
    for i in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        proposals.append((x, y, z))
        adj[x].append((z, i))
    
    pairU = [0] * (k + 1)
    pairV = [0] * (k + 1)
    dist = [0] * (k + 1)
    proposal_idx = [0] * (k + 1)
    
    from collections import deque
    INF = float('inf')
    
    def bfs():
        queue = deque()
        for u in range(1, k + 1):
            if pairU[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while queue:
            u = queue.popleft()
            if dist[u] < dist[0]:
                for z, idx in adj[u]:
                    v = pairV[z]
                    if dist[v] == INF:
                        dist[v] = dist[u] + 1
                        queue.append(v)
        return dist[0] != INF
    
    def dfs(u):
        if u != 0:
            for z, idx in adj[u]:
                v = pairV[z]
                if dist[v] == dist[u] + 1:
                    if dfs(v):
                        pairV[z] = u
                        pairU[u] = z
                        proposal_idx[u] = idx
                        return True
            dist[u] = INF
            return False
        return True
    
    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if pairU[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching == k:
        print("YES")
        out = []
        for u in range(1, k + 1):
            idx = proposal_idx[u]
            x, y, z = proposals[idx]
            out.append(f"{x} {y} {z}")
        print("\n".join(out))
    else:
        print("NO")

solve2()