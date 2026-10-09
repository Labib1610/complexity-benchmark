import sys

def main():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    used = [False] * (n + 1)
    result = []
    
    for u, v in edges:
        if not used[u] and not used[v]:
            used[u] = True
            used[v] = True
            result.append((u, v))
            if len(result) == k + 1:
                break
    
    for u, v in result:
        print(u, v)

if __name__ == "__main__":
    main()