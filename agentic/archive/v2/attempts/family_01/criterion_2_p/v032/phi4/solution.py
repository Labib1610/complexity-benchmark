import sys

def main():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    from collections import defaultdict
    
    graph = defaultdict(list)
    index = 2
    for _ in range(m):
        u, v = int(data[index]), int(data[index + 1])
        graph[u].append(v)
        graph[v].append(u)
        index += 2

    def dfs(node, state):
        visited[node] = state
        states[node] = state
        for neighbor in graph[node]:
            if visited[neighbor] == -1:
                if not dfs(neighbor, 3 - state):
                    return False
            elif visited[neighbor] == state:
                return False
        return True
    
    visited = [-1] * (n + 1)
    states = [0] * (n + 1)

    for i in range(1, n + 1):
        if visited[i] == -1:
            if not dfs(i, 1):
                print("NO")
                return
    
    result = ["YES"]
    for i in range(1, n + 1):
        result.append(str(states[i]))
    
    print("\n".join(result))

if __name__ == "__main__":
    main()