import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    k = int(data[0])
    t = int(data[1])
    idx = 2
    # For each extraction site e (1..k), collect list of injection wells i
    sites = [[] for _ in range(k + 1)]
    for _ in range(t):
        e = int(data[idx]); d = int(data[idx+1]); i = int(data[idx+2])
        idx += 3
        sites[e].append(i)
    
    # Bipartite matching: left = extraction sites 1..k, right = injection wells 1..k
    # Since e->d is fixed and bijective, matching e to i means selecting blueprint (e, d(e), i)
    matchR = [0] * (k + 1)  # matchR[i] = e matched to injection well i
    matchL = [0] * (k + 1)  # matchL[e] = i matched to extraction site e
    
    def try_kuhn(e, visited):
        for i in sites[e]:
            if not visited[i]:
                visited[i] = True
                if matchR[i] == 0 or try_kuhn(matchR[i], visited):
                    matchR[i] = e
                    matchL[e] = i
                    return True
        return False
    
    result = 0
    for e in range(1, k + 1):
        visited = [False] * (k + 1)
        if try_kuhn(e, visited):
            result += 1
        else:
            break
    
    if result == k:
        out = ["YES"]
        for e in range(1, k + 1):
            out.append(f"{e} {e} {matchL[e]}")
        sys.stdout.write("\n".join(out))
    else:
        sys.stdout.write("NO")

solve()