def solve_component_exact(edges of component):
    # edges: list; adj: vertex -> list of (edge_id)
    # color array; at each vertex, used colors set (bitmask)
    # MRV: pick uncolored edge with fewest available colors