import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    B = int(next(it))

    terminals = [int(next(it)) - 1 for _ in range(k)]
    
    # Store edges: original list for output, and adjacency list for min-cut
    original_edges = []
    adj = [[] for _ in range(n)]
    
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        original_edges.append((u, v, w))
        adj[u].append((v, w))
        adj[v].append((u, w))

    if k <= 1:
        print("YES")
        print(0)
        return

    # Dinic's algorithm for Min Cut
    class Dinic:
        def __init__(self, num_nodes):
            self.n = num_nodes
            self.head = [-1] * num_nodes
            self.to = []
            self.cap = []
            self.nxt = []
            self.level = [-1] * num_nodes
            self.ptr = [0] * num_nodes

        def add_edge(self, u, v, c):
            self.nxt.append(self.head[u])
            self.head[u] = len(self.to)
            self.to.append(v)
            self.cap.append(c)

            self.nxt.append(self.head[v])
            self.head[v] = len(self.to)
            self.to.append(u)
            self.cap.append(0)

        def bfs(self, s, t):
            for i in range(self.n):
                self.level[i] = -1
            self.level[s] = 0
            q = deque([s])
            while q:
                v = q.popleft()
                e = self.head[v]
                while e != -1:
                    nxt_v = self.to[e]
                    if self.cap[e] > 0 and self.level[nxt_v] < 0:
                        self.level[nxt_v] = self.level[v] + 1
                        q.append(nxt_v)
                    e = self.nxt[e]
            return self.level[t] >= 0

        def dfs(self, v, t, pushed):
            if pushed == 0 or v == t:
                return pushed
            e = self.ptr[v]
            while e != -1:
                nxt_v = self.to[e]
                tr = self.cap[e]
                if tr > 0 and self.level[nxt_v] == self.level[v] + 1:
                    push = self.dfs(nxt_v, t, min(pushed, tr))
                    if push > 0:
                        self.cap[e] -= push
                        self.cap[e ^ 1] += push
                        return push
                e = self.nxt[e]
                self.ptr[v] = e
            return 0

        def max_flow(self, s, t):
            flow = 0
            while self.bfs(s, t):
                for i in range(self.n):
                    self.ptr[i] = self.head[i]
                while True:
                    pushed = self.dfs(s, t, float('inf'))
                    if pushed == 0:
                        break
                    flow += pushed
            return flow

        def get_reachable_from_source(self, s):
            visited = [False] * self.n
            visited[s] = True
            q = deque([s])
            while q:
                v = q.popleft()
                e = self.head[v]
                while e != -1:
                    nxt_v = self.to[e]
                    if self.cap[e] > 0 and not visited[nxt_v]:
                        visited[nxt_v] = True
                        q.append(nxt_v)
                    e = self.nxt[e]
            return visited

    # Function to evaluate assignment partition
    def evaluate_partition(assignment):
        cost = 0
        cut_edges = []
        for u, v, w in original_edges:
            if assignment[u] != assignment[v]:
                cost += w
                cut_edges.append((u, v))
        return cost, cut_edges

    # Compute isolating cuts lower bound and greedy assignment
    # assignment: array of size n, where -1 means unassigned, 0..k-1 means assigned to terminal
    def isolating_cuts(assignment):
        cuts = []
        reachable_sets = []
        
        # Super source S = n, Super sink T = n + 1
        S = n
        T = n + 1
        
        for i in range(k):
            dinic = Dinic(n + 2)
            # Add original edges (bidirectional)
            for u in range(n):
                for v, w in adj[u]:
                    if u < v:
                        dinic.add_edge(u, v, w)
                        dinic.add_edge(v, u, w)
            
            # Connect terminals/assigned vertices to S and T
            for u in range(n):
                if assignment[u] == i:
                    dinic.add_edge(S, u, float('inf'))
                elif assignment[u] != -1:
                    dinic.add_edge(u, T, float('inf'))
            
            flow = dinic.max_flow(S, T)
            cuts.append(flow)
            reach = dinic.get_reachable_from_source(S)
            reachable_sets.append([reach[u] for u in range(n)])
            
        return cuts, reachable_sets

    best_cost = [float('inf')]
    best_assignment = [None]

    # Initial terminal assignment
    initial_assignment = [-1] * n
    for i, t in enumerate(terminals):
        initial_assignment[t] = i

    # Try heuristic from isolating cuts
    cuts, reach_sets = isolating_cuts(initial_assignment)
    
    # Greedy partition from isolating cuts
    # Sort terminals by cut size ascending, assign vertices
    sorted_terminals = sorted(range(k), key=lambda i: cuts[i])
    greedy_assign = [-1] * n
    for i in sorted_terminals[:-1]:
        for u in range(n):
            if reach_sets[i][u] and greedy_assign[u] == -1:
                greedy_assign[u] = i
    last_t = sorted_terminals[-1]
    for u in range(n):
        if greedy_assign[u] == -1:
            greedy_assign[u] = last_t
            
    c, _ = evaluate_partition(greedy_assign)
    if c < best_cost[0]:
        best_cost[0] = c
        best_assignment[0] = list(greedy_assign)

    if best_cost[0] <= B:
        print("YES")
        _, cut_edges = evaluate_partition(best_assignment[0])
        print(len(cut_edges))
        for u, v in cut_edges:
            print(f"{u + 1} {v + 1}")
        return

    # Branch and bound search for exact solution
    def dfs_bb(curr_assignment, assigned_count):
        if assigned_count == n:
            c, _ = evaluate_partition(curr_assignment)
            if c < best_cost[0]:
                best_cost[0] = c
                best_assignment[0] = list(curr_assignment)
            return

        cuts, reach_sets = isolating_cuts(curr_assignment)
        lb = sum(cuts) // 2
        if lb >= best_cost[0] or lb > B:
            return

        # Check greedy completion
        sorted_t = sorted(range(k), key=lambda i: cuts[i])
        g_assign = list(curr_assignment)
        for i in sorted_t[:-1]:
            for u in range(n):
                if g_assign[u] == -1 and reach_sets[i][u]:
                    g_assign[u] = i
        last = sorted_t[-1]
        for u in range(n):
            if g_assign[u] == -1:
                g_assign[u] = last
                
        c, _ = evaluate_partition(g_assign)
        if c < best_cost[0]:
            best_cost[0] = c
            best_assignment[0] = list(g_assign)
            if best_cost[0] <= B:
                return

        # Pick an unassigned vertex that is connected to the maximum weight of assigned vertices
        best_u = -1
        max_conn = -1
        for u in range(n):
            if curr_assignment[u] == -1:
                conn = 0
                for v, w in adj[u]:
                    if curr_assignment[v] != -1:
                        conn += w
                if conn > max_conn:
                    max_conn = conn
                    best_u = u

        if best_u == -1:
            return

        # Try assigning best_u to each terminal
        # Order branches by connection weight to that terminal
        weights = [0] * k
        for v, w in adj[best_u]:
            if curr_assignment[v] != -1:
                weights[curr_assignment[v]] += w

        branch_order = sorted(range(k), key=lambda i: weights[i], reverse=True)
        for t in branch_order:
            curr_assignment[best_u] = t
            dfs_bb(curr_assignment, assigned_count + 1)
            curr_assignment[best_u] = -1
            if best_cost[0] <= B:
                return

    dfs_bb(initial_assignment, k)

    if best_cost[0] <= B:
        print("YES")
        _, cut_edges = evaluate_partition(best_assignment[0])
        print(len(cut_edges))
        for u, v in cut_edges:
            print(f"{u + 1} {v + 1}")
    else:
        print("NO")

if __name__ == '__main__':
    solve()