import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    q = int(input_data[0])
    t = int(input_data[1])
    
    adj = [[] for _ in range(q + 1)]
    idx = 2
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        idx += 2
        adj[a].append(b)
    
    match_to = [0] * (2 * q + 1)
    match_from = [0] * (q + 1)
    
    for u in range(1, q + 1):
        visited = [False] * (2 * q + 1)
        stack = [(u, 0)]
        parent = {}
        found = -1
        while stack:
            node, state = stack.pop()
            if state == 0:
                stack.append((node, 1))
                for v in adj[node]:
                    if not visited[v]:
                        visited[v] = True
                        parent[v] = node
                        if match_to[v] == 0:
                            found = v
                            stack.clear()
                            break
                        else:
                            stack.append((match_to[v], 0))
            if found != -1:
                break
        
        if found == -1:
            print("NO")
            return
        
        cur = found
        while cur != 0:
            prev = parent[cur]
            old_match = match_from[prev]
            match_to[cur] = prev
            match_from[prev] = cur
            cur = old_match
    
    print("YES")
    out = []
    for u in range(1, q + 1):
        out.append(f"{u} {match_from[u]}")
    sys.stdout.write("\n".join(out) + "\n")

solve()