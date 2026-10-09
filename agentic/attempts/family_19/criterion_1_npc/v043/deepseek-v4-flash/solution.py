import sys
import networkx as nx

def main():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    orders = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        orders.append((s, t, d))
    
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        c = int(next(it))
        edges.append((u, v, c))
    
    # Build graph with capacities
    G = nx.DiGraph()
    for idx, (u, v, c) in enumerate(edges):
        G.add_edge(u, v, capacity=c, index=idx)
    
    flow_matrix = [[0] * m for _ in range(k)]
    
    for order_idx, (s, t, d) in enumerate(orders):
        # Compute max flow from s to t
        flow_value, flow_dict = nx.maximum_flow(G, s, t, flow_func=nx.algorithms.flow.edmonds_karp)
        if flow_value < d:
            print("NO")
            return
        # Send exactly d units along the flow paths
        # We'll use the flow_dict to extract paths and amounts
        # But we need to send exactly d, not max. We'll use a min-cost flow with demand d.
        # Simpler: use nx.min_cost_flow with demand d on a copy.
        H = G.copy()
        # Add super source/sink? Actually we can set node demands.
        for node in H.nodes():
            H.nodes[node]['demand'] = 0
        H.nodes[s]['demand'] = -d
        H.nodes[t]['demand'] = d
        # Add cost 1 per unit for all edges
        for u, v, data in H.edges(data=True):
            data['cost'] = 1
        try:
            flow_dict = nx.min_cost_flow(H)
        except nx.NetworkXUnfeasible:
            print("NO")
            return
        
        # Record flows
        for u, v, data in G.edges(data=True):
            idx = data['index']
            f = flow_dict[u][v]
            flow_matrix[order_idx][idx] = f
            # Reduce capacity in original graph
            G[u][v]['capacity'] -= f
    
    print("YES")
    for row in flow_matrix:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()