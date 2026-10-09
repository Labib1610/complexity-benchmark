import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    m = int(next(it))

    ops = []                     # (job, machine, duration)
    job_ops = []                 # list of operation indices per job
    machine_ops = [[] for _ in range(m)]
    for job in range(j):
        o = int(next(it))
        cur = []
        for _ in range(o):
            mach = int(next(it)) - 1
            dur = int(next(it))
            idx = len(ops)
            ops.append((job, mach, dur))
            cur.append(idx)
            machine_ops[mach].append(idx)
        job_ops.append(cur)

    N = len(ops)

    # ----- initial DAG : only job arcs -----
    adj = [[] for _ in range(N)]          # outgoing edges
    indeg = [0] * N
    for job in range(j):
        seq = job_ops[job]
        for a, b in zip(seq, seq[1:]):
            adj[a].append(b)
            indeg[b] += 1

    # transitive closure as bitsets
    reach = [0] * N
    for u in range(N):
        for v in adj[u]:
            reach[u] |= 1 << v

    # Floyd‑Warshall like closure (N small)
    for k in range(N):
        mask = 1 << k
        for i in range(N):
            if reach[i] & mask:
                reach[i] |= reach[k]

    # ----- lower bound (critical path) -----
    dur = [ops[i][2] for i in range(N)]

    def critical_path(cur_adj, cur_indeg):
        # topological order
        from collections import deque
        q = deque([i for i in range(N) if cur_indeg[i] == 0])
        dist = [0] * N
        indeg_local = cur_indeg[:]          # copy
        while q:
            u = q.popleft()
            finish_u = dist[u] + dur[u]
            for v in cur_adj[u]:
                if dist[v] < finish_u:
                    dist[v] = finish_u
                indeg_local[v] -= 1
                if indeg_local[v] == 0:
                    q.append(v)
        return max(dist[i] + dur[i] for i in range(N))

    # ----- initial feasible schedule (list scheduling) -----
    mach_free = [0] * m
    job_free = [0] * j
    for job in range(j):
        for op in job_ops[job]:
            _, mach, d = ops[op]
            start = max(mach_free[mach], job_free[job])
            finish = start + d
            mach_free[mach] = finish
            job_free[job] = finish
    best = max(mach_free)

    # ----- helper to add an arc and update structures -----
    def add_arc(u, v, cur_reach, cur_adj, cur_indeg):
        # check for cycle
        if (cur_reach[v] >> u) & 1:
            return None
        # new adjacency / indegree
        new_adj = [lst[:] for lst in cur_adj]
        new_adj[u].append(v)
        new_indeg = cur_indeg[:]
        new_indeg[v] += 1
        # update transitive closure
        new_reach = cur_reach[:]
        # all i that can reach u (including u) get edges to v and everything v reaches
        mask_u = (1 << u)
        for i in range(N):
            if (new_reach[i] & mask_u) or i == u:
                new_reach[i] |= (1 << v) | new_reach[v]
        # propagate newly added reachability
        # simple O(N^2) closure recomputation (still cheap)
        for k in range(N):
            mk = 1 << k
            for i in range(N):
                if new_reach[i] & mk:
                    new_reach[i] |= new_reach[k]
        return new_reach, new_adj, new_indeg

    # ----- recursive search -----
    from functools import lru_cache

    # memoisation on reach bitsets to avoid recomputation of identical states
    @lru_cache(maxsize=None)
    def dfs(reach_tuple, indeg_tuple, adj_tuple):
        nonlocal best
        cur_reach = list(reach_tuple)
        cur_indeg = list(indeg_tuple)
        cur_adj = [list(x) for x in adj_tuple]

        lb = critical_path(cur_adj, cur_indeg)
        if lb >= best:
            return
        # find an unordered pair on some machine
        for mach in range(m):
            ops_m = machine_ops[mach]
            L = len(ops_m)
            for i in range(L):
                a = ops_m[i]
                for j2 in range(i + 1, L):
                    b = ops_m[j2]
                    if ((cur_reach[a] >> b) & 1) or ((cur_reach[b] >> a) & 1):
                        continue
                    # branch on a before b and b before a
                    for u, v in ((a, b), (b, a)):
                        res = add_arc(u, v, cur_reach, cur_adj, cur_indeg)
                        if res is None:
                            continue
                        nr, na, nd = res
                        dfs(tuple(nr), tuple(nd), tuple(tuple(x) for x in na))
                    return
        # no unordered pair -> complete schedule
        best = min(best, lb)

    dfs(tuple(reach), tuple(indeg), tuple(tuple(x) for x in adj))
    print(best)


if __name__ == "__main__":
    solve()