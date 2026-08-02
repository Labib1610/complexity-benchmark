import sys
from itertools import permutations

def assign_operators(n, m, rules):
    adj = [set() for _ in range(n)]
    
    for u, v in rules:
        adj[u - 1].add(v - 1)
        adj[v - 1].add(u - 1)
        
    def is_valid(assignment):
        for i in range(n):
            if assignment[i] == 0:
                continue
            for j in adj[i]:
                if assignment[j] == assignment[i]:
                    return False
        return True
    
    windows = [1, 2, 3]
    
    # Try to assign operators in lexicographically smallest way
    result = [-1] * n
    
    def backtrack(i):
        if i == n:
            return is_valid(result)
        
        for window in windows:
            result[i] = window
            if backtrack(i + 1):
                return True
            result[i] = -1
        
        return False
    
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, result)))
    else:
        print("NO")

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    rules = []
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        rules.append((u, v))
        index += 2
        
    assign_operators(n, m, rules)