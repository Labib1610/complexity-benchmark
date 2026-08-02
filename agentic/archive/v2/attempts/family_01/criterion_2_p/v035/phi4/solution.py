from sys import stdin, stdout

def solve():
    import sys
    from collections import defaultdict
    
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    index = 2
    graph = defaultdict(list)
    degrees = [0] * (n + 1)
    
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        graph[u].append(v)
        graph[v].append(u)
        degrees[u] += 1
        degrees[v] += 1
        index += 2
    
    shift_assignment = [-1] * (n + 1)
    
    def dfs(node, current_shift):
        if shift_assignment[node] != -1:
            return shift_assignment[node] == current_shift
        
        shift_assignment[node] = current_shift
        for neighbor in graph[node]:
            if not dfs(neighbor, 3 - current_shift):  # Switch between shifts 1 and 2 (3-1=2, 3-2=1)
                return False
        return True
    
    valid = True
    for i in range(1, n + 1):
        if shift_assignment[i] == -1:
            if not dfs(i, 1):
                valid = False
                break
    
    if not valid:
        stdout.write("NO\n")
    else:
        result = [1 if x == 1 else 2 for x in shift_assignment[1:]]
        stdout.write("YES\n" + ' '.join(map(str, result)) + '\n')

solve()