import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx])
    idx += 1
    m = int(input_data[idx])
    idx += 1
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(input_data[idx]) - 1
        idx += 1
        v = int(input_data[idx]) - 1
        idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    priorities = [-1] * n
    # domains[i] is a bitmask: bit 0 = color 1, bit 1 = color 2, bit 2 = color 3
    domains = [0b111 for _ in range(n)]
    
    def backtrack(task):
        if task == n:
            return True
        
        for p in [1, 2, 3]:
            bit = 1 << (p - 1)
            if domains[task] & bit:
                priorities[task] = p
                
                # Forward checking
                valid = True
                removed = []
                for neighbor in adj[task]:
                    if priorities[neighbor] == -1 and (domains[neighbor] & bit):
                        domains[neighbor] &= ~bit
                        removed.append(neighbor)
                        if domains[neighbor] == 0:
                            valid = False
                            break
                
                if valid:
                    if backtrack(task + 1):
                        return True
                
                # Restore domains
                for neighbor in removed:
                    domains[neighbor] |= bit
                priorities[task] = -1
        
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, priorities)))
    else:
        print("NO")

solve()