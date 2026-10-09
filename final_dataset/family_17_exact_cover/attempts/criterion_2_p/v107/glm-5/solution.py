import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    q = int(data[0])
    t = int(data[1])
    
    head = [-1] * (q + 1)
    to = [0] * t
    nxt = [0] * t
    
    idx = 2
    for i in range(t):
        a = int(data[idx]); b = int(data[idx+1]); idx += 2
        to[i] = b
        nxt[i] = head[a]
        head[a] = i
    
    matchL = [0] * (q + 1)
    matchR = [0] * (2 * q + 1)
    
    def try_kuhn(v, visited):
        e = head[v]
        while e != -1:
            u = to[e]
            if not visited[u]:
                visited[u] = True
                if matchR[u] == 0 or try_kuhn(matchR[u], visited):
                    matchL[v] = u
                    matchR[u] = v
                    return True
            e = nxt[e]
        return False
    
    for v in range(1, q + 1):
        visited = bytearray(2 * q + 1)
        if not try_kuhn(v, visited):
            sys.stdout.write("NO\n")
            return
    
    out = ["YES"]
    for v in range(1, q + 1):
        out.append(f"{v} {matchL[v]}")
    sys.stdout.write("\n".join(out) + "\n")

main()