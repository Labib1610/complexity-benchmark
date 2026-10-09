import sys
sys.setrecursionlimit(10000)

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    pairs_by_x = [set() for _ in range(k+1)]
    for _ in range(t):
        x,y,z = map(int, input().split())
        # x,y,z in 1..k as per constraints
        pairs_by_x[x].add((y,z))
    # check each x has at least one
    for x in range(1,k+1):
        if not pairs_by_x[x]:
            print("NO")
            return
    # order x by length
    order = list(range(1,k+1))
    order.sort(key=lambda x: (len(pairs_by_x[x]), x))
    used_y = [False]*(k+1)
    used_z = [False]*(k+1)
    chosen = [None]*(k+1)

    def feasible(idx):
        # prune at this state
        rem = order[idx:]
        m = len(rem)
        if m == 0:
            return True
        unused_y = [y for y in range(1,k+1) if not used_y[y]]
        unused_z = [z for z in range(1,k+1) if not used_z[z]]
        # check each x has at least one option
        for x in rem:
            ok = False
            for y,z in pairs_by_x[x]:
                if not used_y[y] and not used_z[z]:
                    ok = True
                    break
            if not ok:
                return False
        # matching y
        y_pos = {y:i for i,y in enumerate(unused_y)}
        adj = []
        for x in rem:
            edges = []
            # for each unused y, if any z in unused_z with (y,z) in pairs
            for y in unused_y:
                # any z unused_z in pair set? We can check each z.
                for z in unused_z:
                    if (y,z) in pairs_by_x[x]:
                        edges.append(y_pos[y])
                        break
            adj.append(edges)
        match = [-1]*len(unused_y)
        # iterate all nodes
        def bpm(u, seen):
            for v in adj[u]:
                if not seen[v]:
                    seen[v]=True
                    if match[v]==-1 or bpm(match[v], seen):
                        match[v]=u
                        return True
            return False
        cnt = 0
        for u in range(m):
            seen = [False]*len(unused_y)
            if bpm(u, seen):
                cnt += 1
            else:
                # break early
                return False
        if cnt < m:
            return False
        # matching for z
        z_pos = {z:i for i,z in enumerate(unused_z)}
        adj_z = []
        for x in rem:
            edges_z = []
            for z in unused_z:
                # check any unused y with (y,z)
                for y in unused_y:
                    if (y,z) in pairs_by_x[x]:
                        edges_z.append(z_pos[z])
                        break
            adj_z.append(edges_z)
        match_z = [-1]*len(unused_z)
        def bpm2(u, seen):
            for v in adj_z[u]:
                if not seen[v]:
                    seen[v]=True
                    if match_z[v]==-1 or bpm2(match_z[v], seen):
                        match_z[v]=u
                        return True
            return False
        cnt2 = 0
        for u in range(m):
            seen = [False]*len(unused_z)
            if bpm2(u, seen):
                cnt2 += 1
            else:
                return False
        if cnt2 < m:
            return False
        return True

    def dfs(idx):
        if idx == k:
            return True
        if not feasible(idx):
            return False
        x = order[idx]
        # optional: sort options by the number of available y's/z's? not needed.
        for y,z in pairs_by_x[x]:
            if not used_y[y] and not used_z[z]:
                used_y[y] = True
                used_z[z] = True
                chosen[x] = (y,z)
                if dfs(idx+1):
                    return True
                chosen[x] = None
                used_y[y] = False
                used_z[z] = False
        return False

    if dfs(0):
        print("YES")
        out = []
        # output any order, but we have chosen per x
        for x in range(1,k+1):
            y,z = chosen[x]
            out.append(f"{x} {y} {z}")
        print("\n".join(out))
    else:
        print("NO")

if __name__ == "__main__":
    solve()