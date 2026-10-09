import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(input_data[2 + 2*i])
        v = int(input_data[2 + 2*i + 1])
        edges.append((u, v))
        adj[u].append(i)
        adj[v].append(i)
    
    # Build line graph
    lg_adj = [set() for _ in range(m)]
    for u in range(1, n + 1):
        e = adj[u]
        for i in range(3):
            for j in range(i+1, 3):
                lg_adj[e[i]].add(e[j])
                lg_adj[e[j]].add(e[i])
    
    # Find connected components of line graph
    comp = [-1] * m
    comp_id = 0
    for i in range(m):
        if comp[i] == -1:
            queue = [i]
            comp[i] = comp_id
            head = 0
            while head < len(queue):
                x = queue[head]
                head += 1
                for y in lg_adj[x]:
                    if comp[y] == -1:
                        comp[y] = comp_id
                        queue.append(y)
            comp_id += 1
    
    # For each component, find a 6-cycle (line graph of triangle)
    # and do BFS 3-coloring
    color = [0] * m
    possible = True
    
    for c in range(comp_id):
        # Collect vertices in this component
        vertices = [i for i in range(m) if comp[i] == c]
        vset = set(vertices)
        
        # Find a 6-cycle
        cycle = None
        for s in vertices:
            for t in lg_adj[s]:
                for u in lg_adj[t]:
                    if u == s:
                        continue
                    for w in lg_adj[u]:
                        if w == t or w == s:
                            continue
                        for x in lg_adj[w]:
                            if x == u or x == t or x == s:
                                continue
                            for y in lg_adj[x]:
                                if y == w or y == u or y == t or y == s:
                                    continue
                                if y in lg_adj[s]:
                                    cycle = [s, t, u, w, x, y]
                                    break
                            if cycle:
                                break
                        if cycle:
                            break
                    if cycle:
                        break
                if cycle:
                    break
            if cycle:
                break
        
        if cycle is None:
            # Tree component, BFS 3-coloring
            color[vertices[0]] = 1
            queue = deque([vertices[0]])
            while queue:
                x = queue.popleft()
                for y in lg_adj[x]:
                    if color[y] == 0:
                        color[y] = color[x] % 3 + 1
                        queue.append(y)
        else:
            # 6-cycle found, color it 1,2,3,1,2,3
            for idx, v in enumerate(cycle):
                color[v] = (idx % 3) + 1
            
            # BFS from cycle vertices
            queue = deque(cycle)
            while queue:
                x = queue.popleft()
                for y in lg_adj[x]:
                    if color[y] == 0:
                        color[y] = color[x] % 3 + 1
                        queue.append(y)
    
    if not possible:
        print("NO")
        return
    
    # Check validity
    for u in range(1, n + 1):
        e = adj[u]
        c1, c2, c3 = color[e[0]], color[e[1]], color[e[2]]
        if c1 == c2 or c1 == c3 or c2 == c3:
            print("NO")
            return
    
    # Count colors
    cnt = [0, 0, 0, 0]
    for i in range(m):
        cnt[color[i]] += 1
    
    target = m // 3
    if cnt[1] == target and cnt[2] == target and cnt[3] == target:
        print("YES")
        print(' '.join(map(str, color)))
        return
    
    # Need to balance. Find components with surplus/deficit
    # For each component, compute (cnt1 - target, cnt2 - target, cnt3 - target)
    # and the 6 permutations of colors
    
    comp_verts = [[] for _ in range(comp_id)]
    for i in range(m):
        comp_verts[comp[i]].append(i)
    
    # For each component, compute color counts and all 6 permutations
    comp_perms = []
    for c in range(comp_id):
        verts = comp_verts[c]
        ccnt = [0, 0, 0, 0]
        for v in verts:
            ccnt[color[v]] += 1
        perms = []
        for p in [(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)]:
            vals = (ccnt[p[0]], ccnt[p[1]], ccnt[p[2]])
            perms.append((p, vals))
        comp_perms.append(perms)
    
    # DP over components
    # State: (diff1, diff2) where diff = cnt - target
    # cnt1 + cnt2 + cnt3 = m always, so diff1 + diff2 + diff3 = 0, diff3 = -diff1 - diff2
    # Range: -m to m, use dict
    
    # Initialize
    dp = [dict() for _ in range(comp_id + 1)]
    dp[0][(0, 0)] = None  # (prev_comp, perm_index)
    
    for c in range(comp_id):
        for (d1, d2) in list(dp[c].keys()):
            for pi, (perm, vals) in enumerate(comp_perms[c]):
                nd1 = d1 + (vals[0] - target)
                nd2 = d2 + (vals[1] - target)
                if (nd1, nd2) not in dp[c+1]:
                    dp[c+1][(nd1, nd2)] = (c, pi, (d1, d2))
    
    if (0, 0) not in dp[comp_id]:
        print("NO")
        return
    
    # Reconstruct
    chosen_perms = [None] * comp_id
    cur = (0, 0)
    for c in range(comp_id, 0, -1):
        prev_c, pi, prev_state = dp[c][cur]
        chosen_perms[prev_c] = comp_perms[prev_c][pi][0]
        cur = prev_state
    
    # Apply permutations
    new_color = [0] * m
    for c in range(comp_id):
        perm = chosen_perms[c]
        # perm[i] = new color for old color i+1
        mapping = {i+1: perm[i] for i in range(3)}
        for v in comp_verts[c]:
            new_color[v] = mapping[color[v]]
    
    # Verify
    cnt2 = [0, 0, 0, 0]
    for i in range(m):
        cnt2[new_color[i]] += 1
    
    if cnt2[1] != target or cnt2[2] != target or cnt2[3] != target:
        print("NO")
        return
    
    for u in range(1, n + 1):
        e = adj[u]
        c1, c2, c3 = new_color[e[0]], new_color[e[1]], new_color[e[2]]
        if c1 == c2 or c1 == c3 or c2 == c3:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, new_color)))

solve()