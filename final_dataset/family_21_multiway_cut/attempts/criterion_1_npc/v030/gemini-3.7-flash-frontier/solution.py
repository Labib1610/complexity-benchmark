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
    
    anchors = [int(next(it)) for _ in range(k)]
    anchor_set = set(anchors)
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
        adj[u].append((v, w))
        adj[v].append((u, w))

    # Dinic's Max Flow
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
            # forward
            self.to.append(v)
            self.cap.append(c)
            self.nxt.append(self.head[u])
            self.head[u] = len(self.to) - 1
            # backward
            self.to.append(u)
            self.cap.append(0)
            self.nxt.append(self.head[v])
            self.head[v] = len(self.to) - 1

        def bfs(self, s, t):
            for i in range(self.n):
                self.level[i] = -1
            self.level[s] = 0
            q = deque([s])
            while q:
                v = q.popleft()
                e = self.head[v]
                while e != -1:
                    nxt_node = self.to[e]
                    if self.cap[e] > 0 and self.level[nxt_node] < 0:
                        self.level[nxt_node] = self.level[v] + 1
                        q.append(nxt_node)
                    e = self.nxt[e]
            return self.level[t] != -1

        def dfs(self, v, t, pushed):
            if pushed == 0 or v == t:
                return pushed
            e = self.ptr[v]
            while e != -1:
                nxt_node = self.to[e]
                tr = self.cap[e]
                if self.level[nxt_node] == self.level[v] + 1 and tr > 0:
                    tr = self.dfs(nxt_node, t, min(pushed, tr))
                    if tr > 0:
                        self.cap[e] -= tr
                        self.cap[e ^ 1] += tr
                        return tr
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

        def min_cut_reachable(self, s):
            visited = [False] * self.n
            visited[s] = True
            q = deque([s])
            while q:
                v = q.popleft()
                e = self.head[v]
                while e != -1:
                    nxt_node = self.to[e]
                    if self.cap[e] > 0 and not visited[nxt_node]:
                        visited[nxt_node] = True
                        q.append(nxt_node)
                    e = self.nxt[e]
            return visited

    # Terminal index mapping: anchor -> 0..k-1
    t_idx = {anchors[i]: i for i in range(k)}

    # Initial assignment using multiway cut heuristic (isolating cuts)
    # Assign each node to the closest terminal by isolating cut distance
    labels = [0] * (n + 1)
    for i in range(k):
        labels[anchors[i]] = i

    # Alpha-expansion to optimize labeling
    # Labels are 0..k-1
    # Initialize non-terminals to label 0
    for v in range(1, n + 1):
        if v in t_idx:
            labels[v] = t_idx[v]
        else:
            labels[v] = 0

    INF = 10**15

    def alpha_expansion_step(alpha):
        # We construct a graph for binary energy minimization
        # Nodes: 1..n plus auxiliary nodes for edges where neither endpoint currently has label alpha
        # Source S (keep old label / 0), Sink T (switch to alpha / 1)
        # S = 0, T = n + 1
        # Additional nodes for edges
        aux_nodes = 0
        edge_aux = {}
        for u, v, w in edges:
            if labels[u] != alpha and labels[v] != alpha and labels[u] != labels[v]:
                aux_nodes += 1
                edge_aux[(u, v)] = n + 1 + aux_nodes

        dinic = Dinic(n + 2 + aux_nodes)
        S = 0
        T = n + 1

        for u in range(1, n + 1):
            if u in t_idx:
                if t_idx[u] == alpha:
                    dinic.add_edge(S, u, INF)
                else:
                    dinic.add_edge(u, T, INF)
            else:
                if labels[u] == alpha:
                    dinic.add_edge(S, u, INF)

        for u, v, w in edges:
            lu = labels[u]
            lv = labels[v]
            if lu == alpha and lv == alpha:
                continue
            elif lu == alpha and lv != alpha:
                # u stays alpha (in S). If v switches to alpha (to S), cost 0. If v stays (to T), cost w.
                dinic.add_edge(S, v, w)
            elif lu != alpha and lv == alpha:
                dinic.add_edge(S, u, w)
            elif lu == lv:
                # Both have same label != alpha
                # If one switches to alpha and the other doesn't, cost w.
                dinic.add_edge(u, v, w)
                dinic.add_edge(v, u, w)
            else:
                # lu != lv, and neither is alpha
                aux = edge_aux[(u, v)]
                dinic.add_edge(u, aux, w)
                dinic.add_edge(v, aux, w)
                dinic.add_edge(aux, T, w)

        dinic.max_flow(S, T)
        reachable = dinic.min_cut_reachable(S)
        
        improved = False
        for u in range(1, n + 1):
            if u not in t_idx:
                # If reachable from S, it stays/moves to alpha
                new_l = alpha if reachable[u] else labels[u]
                if new_l != labels[u]:
                    labels[u] = new_l
                    improved = True
        return improved

    # Run alpha-expansion iterations
    for _ in range(20):
        changed = False
        for a in range(k):
            if alpha_expansion_step(a):
                changed = True
        if not changed:
            break

    # Calculate cost with current labels
    cut_edges = []
    total_cost = 0
    for u, v, w in edges:
        if labels[u] != labels[v]:
            total_cost += w
            cut_edges.append((u, v))

    # Branch and bound if not yet <= B and n is small
    best_cost = total_cost
    best_labels = list(labels)

    if best_cost > B and n <= 35:
        # Exact branch and bound for small graphs
        non_terminals = [v for v in range(1, n + 1) if v not in t_idx]
        cur_labels = [0] * (n + 1)
        for i in range(k):
            cur_labels[anchors[i]] = i

        def bnb(idx, cur_cost):
            nonlocal best_cost, best_labels
            if cur_cost >= best_cost:
                return
            if idx == len(non_terminals):
                if cur_cost < best_cost:
                    best_cost = cur_cost
                    best_labels = list(cur_labels)
                return
            
            u = non_terminals[idx]
            for c in range(k):
                cur_labels[u] = c
                # calculate added cost for edges to already assigned neighbors
                added = 0
                for v, w in adj[u]:
                    if v in t_idx or (v in non_terminals and non_terminals.index(v) < idx):
                        if cur_labels[v] != c:
                            added += w
                bnb(idx + 1, cur_cost + added)

        bnb(0, 0)
        labels = best_labels
        cut_edges = []
        total_cost = 0
        for u, v, w in edges:
            if labels[u] != labels[v]:
                total_cost += w
                cut_edges.append((u, v))

    if total_cost <= B:
        print("YES")
        print(len(cut_edges))
        for u, v in cut_edges:
            print(f"{u} {v}")
    else:
        print("NO")

if __name__ == '__main__':
    solve()