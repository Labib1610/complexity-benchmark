import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
resources = []
for _ in range(k):
    s, t, d = map(int, input().split())
    resources.append((s - 1, t - 1, d))

edges = []
for _ in range(m):
    u, v, cap = map(int, input().split())
    edges.append((u - 1, v - 1, cap))

# We'll use a max-flow with lower bounds approach.
# For each resource, we need to send d units from s to t.
# We can combine all resources into one super-source and super-sink.

# Build graph for max flow with lower bounds
# We'll use Dinic's algorithm for max flow.

class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
    
    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        backward = [fr, 0, forward]
        forward[2] = backward
        self.graph[fr].append(forward)
        self.graph[to].append(backward)
    
    def bfs(self, s, t):
        self.level = [-1] * self.n
        q = deque([s])
        self.level[s] = 0
        while q:
            v = q.popleft()
            for to, cap, rev in self.graph[v]:
                if cap > 0 and self.level[to] < 0:
                    self.level[to] = self.level[v] + 1
                    q.append(to)
        return self.level[t] >= 0
    
    def dfs(self, v, t, f):
        if v == t:
            return f
        for i in range(self.it[v], len(self.graph[v])):
            self.it[v] = i
            to, cap, rev = self.graph[v][i]
            if cap > 0 and self.level[v] + 1 == self.level[to]:
                ret = self.dfs(to, t, min(f, cap))
                if ret > 0:
                    self.graph[v][i][1] -= ret
                    rev[1] += ret
                    return ret
        return 0
    
    def max_flow(self, s, t):
        flow = 0
        INF = 10**18
        while self.bfs(s, t):
            self.it = [0] * self.n
            while True:
                f = self.dfs(s, t, INF)
                if f == 0:
                    break
                flow += f
        return flow

# We'll create a flow network:
# Super source -> each resource source with demand d
# Each resource target -> super sink with demand d
# Edges with capacity cap

# But we need to ensure each resource's flow is separate.
# We can do this by creating k copies of the network? That's too big.
# Instead, we can use a single network with lower bounds.

# Approach: For each resource i, we add an edge from super source to s_i with capacity d_i,
# and from t_i to super sink with capacity d_i.
# Then we run max flow from super source to super sink.
# If total flow == sum(d_i), then feasible.

# But this doesn't enforce that each resource's flow is separate — it just sends total flow.
# However, since each resource has its own source and sink, and flows are indistinguishable,
# we can just check if total flow can be routed respecting capacities.

# Actually, this is a single-commodity flow problem if we treat all canisters as identical.
# But the problem says different resources are independent — but they share capacities.
# So we can just send total sum(d_i) from all sources to all sinks.

# Let's build the network.

total_demand = sum(d for _, _, d in resources)
S = n
T = n + 1
dinic = Dinic(n + 2)

for s, t, d in resources:
    dinic.add_edge(S, s, d)
    dinic.add_edge(t, T, d)

for u, v, cap in edges:
    dinic.add_edge(u, v, cap)

flow = dinic.max_flow(S, T)

if flow != total_demand:
    print("NO")
else:
    print("YES")
    # Now we need to output the flow per resource per edge.
    # We can reconstruct by running flow for each resource separately.
    # But that's expensive. Instead, we can use the residual graph to decompose.
    # However, for simplicity, we can run a separate max flow for each resource
    # on the original capacities, subtracting used capacity.
    
    # We'll do a simple decomposition:
    # For each resource, run max flow from its source to its target on the original graph
    # with capacities reduced by already used flow.
    
    used = [[0]*m for _ in range(k)]
    remaining_cap = [cap for _, _, cap in edges]
    
    for idx, (s, t, d) in enumerate(resources):
        # Build a fresh Dinic for this resource
        dinic2 = Dinic(n)
        for j, (u, v, cap) in enumerate(edges):
            dinic2.add_edge(u, v, remaining_cap[j])
        # Add super source/sink? No, just run from s to t
        f = dinic2.max_flow(s, t)
        if f != d:
            print("NO")
            sys.exit()
        # Now extract flow on each edge
        # We need to know how much flow went through each edge.
        # We can inspect the residual graph.
        for j, (u, v, cap) in enumerate(edges):
            # Find the forward edge in dinic2.graph[u]
            for to, cap_left, rev in dinic2.graph[u]:
                if to == v:
                    # original cap = cap + cap_left? Actually cap_left is remaining capacity
                    # The flow used = original_cap - cap_left
                    flow_used = cap - cap_left
                    used[idx][j] = flow_used
                    remaining_cap[j] -= flow_used
                    break
    
    for row in used:
        print(' '.join(map(str, row)))