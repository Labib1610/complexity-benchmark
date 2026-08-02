def is_valid_assignment(n, m, restrictions):
    from collections import defaultdict
    
    graph = defaultdict(list)
    for u, v in restrictions:
        graph[u].append(v)
        graph[v].append(u)
    
    states = [0] * (n + 1)

    def backtrack(module):
        if module > n:
            return True
        for state in range(1, 4):
            valid = True
            for neighbor in graph[module]:
                if states[neighbor] == state:
                    valid = False
                    break
            if valid:
                states[module] = state
                if backtrack(module + 1):
                    return True
                states[module] = 0
        return False

    if backtrack(1):
        return "YES", states[1:]
    else:
        return "NO",

# Reading input
import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
restrictions = [tuple(map(int, line.split())) for line in data[1:m + 1]]

# Get result
result = is_valid_assignment(n, m, restrictions)

# Output result
if result[0] == "NO":
    print("NO")
else:
    print("YES")
    print(" ".join(map(str, result[1])))