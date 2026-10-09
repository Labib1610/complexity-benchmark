import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    degrees = [0] * n
    
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
        degrees[u] += 1
        degrees[v] += 1
    
    # We want lexicographically smallest assignment.
    # Assign 1 if possible, else 2.
    # Assigning 1 to u means all neighbors must be assigned 2.
    # This propagates constraints.
    # We process nodes in order 0 to n-1.
    # If a node is unassigned, we try to assign 1.
    # This forces all neighbors to be 2.
    # If a conflict arises (neighbor already 1), we backtrack and try 2.
    # If 2 also fails, it's impossible.
    
    assignment = [0] * n
    
    for i in range(n):
        if assignment[i] != 0:
            continue
        
        # Try to assign 1 to i
        # We need to check if this is possible
        # We use a queue to propagate constraints
        # We need to be able to backtrack
        # Let's use a stack of assignments made in this component
        
        # Actually, since we process in order, we can just try to assign 1
        # If it fails, we try 2.
        # If both fail, output NO.
        
        # To check if assignment is possible, we can use BFS/DFS
        # But we need to be careful about backtracking
        
        # Let's implement a recursive function with backtracking?
        # Or iterative with explicit stack
        
        # Since the graph is bipartite (if solution exists), 
        # we can just check if the component is bipartite.
        # But we also need the lexicographically smallest assignment.
        
        # The strategy of assigning 1 to the smallest index in a component
        # and propagating gives the lexicographically smallest assignment
        # for that component.
        
        # So we try to assign 1 to i.
        # If it leads to a conflict, we try 2.
        # If both lead to conflict, output NO.
        
        # We need to be able to undo assignments if we try 1 and it fails.
        
        # Let's implement a BFS that returns True if successful
        # and fills the assignment, or False and undoes changes.
        
        # We'll pass a copy of assignment? No, too slow.
        # We'll record changes and undo them.
        
        # Function to try assigning val to start node
        def try_assign(start_node, val):
            # Returns True if successful, False otherwise
            # If successful, assignment is updated
            # If not, assignment is unchanged
            changes = []
            q = deque()
            
            assignment[start_node] = val
            changes.append(start_node)
            q.append(start_node)
            
            possible = True
            while q:
                u = q.popleft()
                current_val = assignment[u]
                expected_neighbor_val = 3 - current_val
                
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = expected_neighbor_val
                        changes.append(v)
                        q.append(v)
                    elif assignment[v] != expected_neighbor_val:
                        possible = False
                        break
                if not possible:
                    break
            
            if possible:
                return True
            else:
                # Undo changes
                for node in changes:
                    assignment[node] = 0
                return False
        
        if try_assign(i, 1):
            continue
        elif try_assign(i, 2):
            continue
        else:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == '__main__':
    solve()