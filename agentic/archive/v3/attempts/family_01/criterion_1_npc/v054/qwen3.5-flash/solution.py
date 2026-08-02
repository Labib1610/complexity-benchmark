import sys

# Increase recursion depth to handle deep recursion if necessary
sys.setrecursionlimit(5000)

def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    ans = [0] * (n + 1)
    
    class Solver:
        def __init__(self, n, adj):
            self.n = n
            self.adj = adj
            
        def check(self, current_ans):
            # Identify uncolored nodes
            uncolored = [u for u in range(1, self.n + 1) if current_ans[u] == 0]
            
            # If no uncolored nodes, we have a valid full assignment
            if not uncolored:
                return True
            
            # Initialize domains for all nodes (bitmask)
            # 1 -> 1, 2 -> 2, 3 -> 4. Available colors mask: 7
            domains = [7] * (self.n + 1)
            
            # Update domains based on fixed neighbors
            for u in uncolored:
                for v in self.adj[u]:
                    # If neighbor v is fixed, remove its color from u's domain
                    if current_ans[v] != 0:
                        domains[u] &= ~current_ans[v]
                
                # If any node has no available colors, return False immediately
                if domains[u] == 0:
                    return False
            
            # Run DFS to check if a valid coloring exists
            return self.dfs(domains, uncolored)

        def dfs(self, domains, uncolored):
            if not uncolored:
                return True
            
            # Find node with minimum remaining values (MRV)
            best_u = -1
            min_size = 8
            u_list = uncolored
            
            # Create a set for O(1) membership check
            S = set(u_list)
            
            for u in u_list:
                # Count set bits
                size = (domains[u] & 1) + ((domains[u] >> 1) & 1) + ((domains[u] >> 2) & 1)
                if size == 0:
                    return False
                if size < min_size:
                    min_size = size
                    best_u = u
            
            if best_u == -1:
                return False
            
            # If min_size == 1, we don't need to loop, just try the single color
            if min_size == 1:
                c = 0
                if domains[best_u] & 1: c = 1
                elif domains[best_u] & 2: c = 2
                elif domains[best_u] & 4: c = 4
                
                changes = []
                valid = True
                for v in self.adj[best_u]:
                    if v in S:
                        old_d = domains[v]
                        new_d = old_d & ~c
                        if new_d == 0:
                            valid = False
                            break
                        else:
                            domains[v] = new_d
                            changes.append((v, old_d))
                
                if valid:
                    new_u_list = [x for x in u_list if x != best_u]
                    if self.dfs(domains, new_u_list):
                        return True
                
                # Backtrack
                for v, old_d in changes:
                    domains[v] = old_d
                
                return False
            else:
                c_mask = domains[best_u]
                for c in [1, 2, 4]:
                    if c_mask & c:
                        changes = []
                        valid = True
                        for v in self.adj[best_u]:
                            if v in S:
                                old_d = domains[v]
                                new_d = old_d & ~c
                                if new_d == 0:
                                    valid = False
                                    break
                                else:
                                    domains[v] = new_d
                                    changes.append((v, old_d))
                        
                        if valid:
                            new_u_list = [x for x in u_list if x != best_u]
                            if self.dfs(domains, new_u_list):
                                return True
                        
                        # Backtrack
                        for v, old_d in changes:
                            domains[v] = old_d
                
                return False

    solver = Solver(n, adj)
    
    # Greedily assign colors to ensure lexicographically smallest sequence
    for i in range(1, n + 1):
        found = False
        for c in [1, 2, 4]:
            # Check compatibility with previously assigned nodes (1 to i-1)
            conflict = False
            for v in adj[i]:
                if ans[v] == c:
                    conflict = True
                    break
            
            if not conflict:
                ans[i] = c
                if solver.check(ans):
                    found = True
                    break
                else:
                    ans[i] = 0 # Backtrack
            else:
                ans[i] = 0
        
        if not found:
            print("NO")
            return

    print("YES")
    print(*(ans[1:]))

if __name__ == '__main__':
    solve()