import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    k = int(next(iterator))
    B = int(next(iterator))
    
    terminals = [int(next(iterator)) - 1 for _ in range(k)]
    
    edges = []
    adj = [[] for _ in range(n)]
    for i in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        w = int(next(iterator))
        edges.append((u, v, w))
        adj[u].append((v, w, i))
        adj[v].append((u, w, i))

    # Dinic's algorithm for Min s-t Cut
    class Dinic:
        def __init__(self, num_nodes):
            self.n = num_nodes
            self.graph = [[] for _ in range(num_nodes)]
            self.edges = []

        def add_edge(self, u, v, cap):
            self.graph[u].append(len(self.edges))
            self.edges.append([v, cap, 0])
            self.graph[v].append(len(self.edges))
            self.edges.append([u, 0, 0])

        def max_flow(self, s, t):
            flow = 0
            while True:
                level = [-1] * self.n
                level[s] = 0
                q = deque([s])
                while q:
                    u = q.popleft()
                    for e_idx in self.graph[u]:
                        v, cap, f = self.edges[e_idx]
                        if cap - f > 0 and level[v] == -1:
                            level[v] = level[u] + 1
                            q.append(v)
                if level[t] == -1:
                    break

                ptr = [0] * self.n
                def dfs(u, pushed):
                    if pushed == 0 or u == t:
                        return pushed
                    for cid in range(ptr[u], len(self.graph[u])):
                        ptr[u] = cid
                        e_idx = self.graph[u][cid]
                        v, cap, f = self.edges[e_idx]
                        tr = cap - f
                        if level[u] + 1 != level[v] or tr == 0:
                            continue
                        push = dfs(v, min(pushed, tr))
                        if push == 0:
                            continue
                        self.edges[e_idx][2] += push
                        self.edges[e_idx ^ 1][2] -= push
                        return push
                    return 0

                while True:
                    pushed = dfs(s, float('inf'))
                    if pushed == 0:
                        break
                    flow += pushed
            return flow

        def min_cut(self, s):
            visited = [False] * self.n
            q = deque([s])
            visited[s] = True
            while q:
                u = q.popleft()
                for e_idx in self.graph[u]:
                    v, cap, f = self.edges[e_idx]
                    if cap - f > 0 and not visited[v]:
                        visited[v] = True
                        q.append(v)
            return visited

    # Find lower bound using isolating cuts and get an initial solution
    def get_isolating_cut(t_idx):
        # source is terminals[t_idx], sink is super_sink connected from all other terminals
        s = terminals[t_idx]
        t = n
        dinic = Dinic(n + 1)
        for u, v, w in edges:
            dinic.add_edge(u, v, w)
            dinic.add_edge(v, u, w)
        for i, term in enumerate(terminals):
            if i != t_idx:
                dinic.add_edge(term, t, float('inf'))
        
        flow = dinic.max_flow(s, t)
        in_cut = dinic.min_cut(s)
        return flow, in_cut

    # If k <= 1, 0 cost
    if k <= 1:
        print("YES")
        print(0)
        return

    isolating_cuts = []
    for i in range(k):
        flow, in_cut = get_isolating_cut(i)
        isolating_cuts.append((flow, in_cut))

    # Multiway cut approximation: union of k-1 smallest cuts
    # Check if approximation is <= B
    isolating_cuts.sort(key=lambda x: x[0])
    
    # Let's also do a branch and bound to find the exact minimum multiway cut
    # Representation of partitions:
    # Each chamber is assigned a label in 0..k-1
    best_cost = [float('inf')]
    best_assignment = [None]

    # Quick check with isolating cuts heuristic to initialize best_cost
    # Assign components based on isolating cuts
    approx_assignment = [-1] * n
    for i in range(k - 1):
        _, in_cut = isolating_cuts[i]
        for u in range(n):
            if in_cut[u] and approx_assignment[u] == -1:
                approx_assignment[u] = i
    for u in range(n):
        if approx_assignment[u] == -1:
            approx_assignment[u] = k - 1
    
    # Calculate cost of approx_assignment
    approx_cost = 0
    for u, v, w in edges:
        if approx_assignment[u] != approx_assignment[v]:
            approx_cost += w
    
    best_cost[0] = approx_cost
    best_assignment[0] = list(approx_assignment)

    # If approx_cost <= B, we already have a valid solution!
    # But let's verify if exact search is needed when approx_cost > B
    if best_cost[0] > B:
        # Branch and bound search
        # Merge vertices approach:
        # We assign vertices connected to terminals.
        assignment = [-1] * n
        for i, term in enumerate(terminals):
            assignment[term] = i
        
        # Order unassigned vertices by degree / connectivity
        unassigned = [i for i in range(n) if assignment[i] == -1]
        
        def solve_bb(idx, current_cost):
            if current_cost >= best_cost[0]:
                return
            if idx == len(unassigned):
                if current_cost < best_cost[0]:
                    best_cost[0] = current_cost
                    best_assignment[0] = list(assignment)
                return
            
            u = unassigned[idx]
            
            # Count costs to already assigned neighbors for each possible choice
            cost_increase = [0] * k
            for v, w, _ in adj[u]:
                if assignment[v] != -1:
                    for c in range(k):
                        if c != assignment[v]:
                            cost_increase[c] += w
            
            # Try choices sorted by cost increase
            choices = sorted(range(k), key=lambda c: cost_increase[c])
            for c in choices:
                assignment[u] = c
                solve_bb(idx + 1, current_cost + cost_increase[c])
                assignment[u] = -1

        if len(unassigned) <= 30: # Only run full BB if graph is reasonably small
            solve_bb(0, 0)

    if best_cost[0] <= B:
        print("YES")
        cut_edges = []
        for u, v, w in edges:
            if best_assignment[0][u] != best_assignment[0][v]:
                cut_edges.append((u + 1, v + 1))
        print(len(cut_edges))
        for u, v in cut_edges:
            print(f"{u} {v}")
    else:
        print("NO")

if __name__ == '__main__':
    solve()