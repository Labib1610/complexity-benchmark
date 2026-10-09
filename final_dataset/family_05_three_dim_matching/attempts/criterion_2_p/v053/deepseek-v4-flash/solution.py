import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # container -> set of vessels
    adj = [[] for _ in range(k + 1)]
    for _ in range(t):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        # v is the tag, but since each container has a unique tag,
        # we only care about container u and vessel w.
        adj[u].append(w)
    
    # match_vessel[v] = container assigned to vessel v, 0 if none
    match_vessel = [0] * (k + 1)
    
    def dfs(u, visited):
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                if match_vessel[v] == 0 or dfs(match_vessel[v], visited):
                    match_vessel[v] = u
                    return True
        return False
    
    match_count = 0
    for u in range(1, k + 1):
        visited = [False] * (k + 1)
        if dfs(u, visited):
            match_count += 1
    
    if match_count == k:
        print("YES")
        # We need to output container, tag, vessel.
        # Since container u has a unique tag, we need to know that tag.
        # We can reconstruct from input: store tag for each container.
        # Let's store tag_of_container from input.
        # We'll re-read input to get tags.
        # But we already consumed input. We'll store during reading.
        # Let's modify: store tag_of_container.
        # We'll do a second pass? Better: store while reading.
        # Since we already read, we can store in a dict.
        # Let's just store tag_of_container in the first loop.
        # We'll rewrite reading part.
        pass

# We need to redo reading to store tags.
# Let's rewrite properly.

def solve_final():
    import sys
    sys.setrecursionlimit(1000000)
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    adj = [[] for _ in range(k + 1)]
    tag_of = [0] * (k + 1)
    for _ in range(t):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        tag_of[u] = v
        adj[u].append(w)
    
    match_vessel = [0] * (k + 1)
    
    def dfs(u, visited):
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                if match_vessel[v] == 0 or dfs(match_vessel[v], visited):
                    match_vessel[v] = u
                    return True
        return False
    
    match_count = 0
    for u in range(1, k + 1):
        visited = [False] * (k + 1)
        if dfs(u, visited):
            match_count += 1
    
    if match_count < k:
        print("NO")
        return
    
    print("YES")
    # match_vessel[v] = container assigned to vessel v
    for v in range(1, k + 1):
        u = match_vessel[v]
        print(u, tag_of[u], v)

if __name__ == "__main__":
    solve_final()