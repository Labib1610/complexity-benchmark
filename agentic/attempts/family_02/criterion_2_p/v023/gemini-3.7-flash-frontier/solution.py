import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    m = int(input_data[1])

    adj = [[] for _ in range(2 * n)]
    radj = [[] for _ in range(2 * n)]

    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2

        lit1 = 2 * (u - 1) if u > 0 else 2 * (-u - 1) + 1
        lit2 = 2 * (v - 1) if v > 0 else 2 * (-v - 1) + 1

        nlit1 = lit1 ^ 1
        nlit2 = lit2 ^ 1

        adj[nlit1].append(lit2)
        adj[nlit2].append(lit1)
        radj[lit2].append(nlit1)
        radj[lit1].append(nlit2)

    visited = bytearray(2 * n)
    order = []
    it = [0] * (2 * n)

    for i in range(2 * n):
        if not visited[i]:
            visited[i] = 1
            st = [i]
            while st:
                u = st[-1]
                while it[u] < len(adj[u]):
                    nxt = adj[u][it[u]]
                    it[u] += 1
                    if not visited[nxt]:
                        visited[nxt] = 1
                        st.append(nxt)
                        break
                else:
                    st.pop()
                    order.append(u)

    scc = [-1] * (2 * n)
    scc_count = 0

    for i in reversed(order):
        if scc[i] == -1:
            st = [i]
            scc[i] = scc_count
            while st:
                u = st.pop()
                for nxt in radj[u]:
                    if scc[nxt] == -1:
                        scc[nxt] = scc_count
                        st.append(nxt)
            scc_count += 1

    ans = [0] * n
    for i in range(n):
        if scc[2 * i] == scc[2 * i + 1]:
            print("NO")
            return
        ans[i] = 1 if scc[2 * i] > scc[2 * i + 1] else 0

    print("YES")
    print(*(ans))


if __name__ == "__main__":
    solve()