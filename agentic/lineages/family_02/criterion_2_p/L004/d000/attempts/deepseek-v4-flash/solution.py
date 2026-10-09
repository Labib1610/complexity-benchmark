import sys
sys.setrecursionlimit(1 << 25)

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    N = 2 * n  # each variable has two nodes: x_i and ~x_i
    g = [[] for _ in range(N)]
    rg = [[] for _ in range(N)]

    def node(lit):
        # positive literal -> index (var-1)*2 + 1
        # negative literal -> index (var-1)*2
        var = abs(lit) - 1
        if lit > 0:
            return 2 * var + 1
        else:
            return 2 * var

    def add_imp(u, v):
        g[u].append(v)
        rg[v].append(u)

    for _ in range(m):
        a, b = map(int, input().split())
        # clause (a or b) => (~a -> b) and (~b -> a)
        add_imp(node(-a), node(b))
        add_imp(node(-b), node(a))

    # Tarjan SCC
    index = 0
    indices = [-1] * N
    lowlink = [0] * N
    onstack = [False] * N
    stack = []
    comp = [-1] * N
    comp_count = 0

    def strongconnect(v):
        nonlocal index, comp_count
        indices[v] = index
        lowlink[v] = index
        index += 1
        stack.append(v)
        onstack[v] = True

        for w in g[v]:
            if indices[w] == -1:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif onstack[w]:
                lowlink[v] = min(lowlink[v], indices[w])

        if lowlink[v] == indices[v]:
            while True:
                w = stack.pop()
                onstack[w] = False
                comp[w] = comp_count
                if w == v:
                    break
            comp_count += 1

    for v in range(N):
        if indices[v] == -1:
            strongconnect(v)

    # Check satisfiability
    assignment = [False] * n
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
        # In SCC order, comp with larger id is earlier in topological order
        # We assign false if comp[2*i] > comp[2*i+1] (i.e., ~x_i comes before x_i)
        assignment[i] = comp[2 * i] > comp[2 * i + 1]

    print("YES")
    print(" ".join("1" if assignment[i] else "0" for i in range(n)))

if __name__ == "__main__":
    main()