from collections import defaultdict, deque
import sys

def solve():
    n, m, k = map(int, input().split())
    
    orders = []
    for _ in range(k):
        s, t, d = map(int, input().split())
        orders.append((s-1, t-1, d))  # Convert to 0-indexed
    
    lanes = []
    lane_graph = defaultdict(list)  # adjacency list for flow network
    for i in range(m):
        u, v, c = map(int, input().split())
        lanes.append((u-1, v-1, c))  # Convert to 0-indexed
        lane_graph[u-1].append((v-1, i))  # node -> list of (next_node, lane_index)
    
    # For each order, we need to find a flow that satisfies the constraints
    # This is a multi-commodity flow problem, but we can solve it by trying to find flows independently
    # and then check if the total usage of each edge doesn't exceed capacity
    
    # We'll use a greedy approach: for each order, find a path from source to target and send flow along it
    
    def bfs_flow(source, target, amount):
        # Find a path from source to target using BFS
        # Returns a list of lane indices that form the path
        if source == target:
            return []
            
        queue = deque([(source, [])])  # (current_node, path_of_lane_indices)
        visited = set([source])
        
        while queue:
            node, path = queue.popleft()
            
            for next_node, lane_idx in lane_graph[node]:
                if next_node not in visited:
                    new_path = path + [lane_idx]
                    if next_node == target:
                        return new_path
                    visited.add(next_node)
                    queue.append((next_node, new_path))
        
        return None  # No path found
    
    # Try to assign flows for each order
    flow_assignments = []  # flow_assignments[order][lane] = amount
    lane_usage = [0] * m  # Total usage of each lane
    
    for order_idx, (s, t, d) in enumerate(orders):
        # For this order, we need to send d units from s to t
        # We'll decompose this into paths
        
        # First, let's see if there's even a path from s to t
        path = bfs_flow(s, t, d)
        if path is None:
            print("NO")
            return
            
        # For simplicity, we'll just use one path and send all d units along it
        # In a more complex solution, we might need to decompose the flow
        assignment = [0] * m
        for lane_idx in path:
            assignment[lane_idx] = d
            lane_usage[lane_idx] += d
            
        flow_assignments.append(assignment)
    
    # Check if any lane exceeds its capacity
    for i in range(m):
        if lane_usage[i] > lanes[i][2]:  # lanes[i][2] is the capacity
            print("NO")
            return
    
    # If we get here, we have a valid assignment
    print("YES")
    for assignment in flow_assignments:
        print(' '.join(map(str, assignment)))

def main():
    solve()

if __name__ == "__main__":
    main()