import sys
sys.setrecursionlimit(1 << 20)

def main():
    input = sys.stdin.readline
    q, t = map(int, input().split())
    adj = [[] for _ in range(q + 1)]
    for _ in range(t):
        a, b = map(int, input().split())
        adj[a].append(b - q)  # store platform index 1..q

    match_platform = [0] * (q + 1)  # which controller is matched to platform
    match_controller = [0] * (q + 1)  # which platform is matched to controller

    def dfs(controller, visited):
        for platform in adj[controller]:
            if visited[platform]:
                continue
            visited[platform] = True
            if match_platform[platform] == 0 or dfs(match_platform[platform], visited):
                match_platform[platform] = controller
                match_controller[controller] = platform
                return True
        return False

    for c in range(1, q + 1):
        visited = [False] * (q + 1)
        if not dfs(c, visited):
            print("NO")
            return

    print("YES")
    for c in range(1, q + 1):
        print(c, match_controller[c] + q)

if __name__ == "__main__":
    main()