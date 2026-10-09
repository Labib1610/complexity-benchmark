INF = large
match_A = [0]*(nA+1)  # 0 = unmatched, else vertex in B
match_B = [0]*(nB+1)

def bfs():
    queue = deque
    for a in 1..nA:
        if match_A[a] == 0:
            dist[a] = 0
            queue.append(a)
        else:
            dist[a] = INF
    found = False
    while queue:
        a = queue.popleft()
        for b in adj[a]:
            mb = match_B[b]
            if mb == 0:
                found = True
            elif dist[mb] == INF:
                dist[mb] = dist[a] + 1
                queue.append(mb)
    return found

def dfs(a):
    for b in adj[a]:
        mb = match_B[b]
        if mb == 0 or (dist[mb] == dist[a] + 1 and dfs(mb)):
            match_A[a] = b
            match_B[b] = = a
            return True
    dist[a] = INF
    return False