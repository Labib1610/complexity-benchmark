import sys
from array import array

def main():
    input_buffer = sys.stdin.buffer
    nA, nB, m = map(int, input_buffer.readline().split())
    n = nA + nB

    U = array('i')
    V = array('i')
    degree = array('i', [0]) * n
    delta = 0

    for _ in range(m):
        u, v = map(int, input_buffer.readline().split())
        u -= 1
        v = nA + v - 1
        U.append(u)
        V.append(v)
        degree[u] += 1
        degree[v] += 1
        if degree[u] > delta:
            delta = degree[u]
        if degree[v] > delta:
            delta = degree[v]

    if m == 0:
        sys.stdout.write("YES\n\n")
        return

    incident = [None] * n
    missing = [1] * n
    colors = array('i', [0]) * m

    def add_color(vertex, color, edge):
        d = incident[vertex]
        if d is None:
            d = {}
            incident[vertex] = d
        d[color] = edge

        if missing[vertex] == color:
            color += 1
            while color in d:
                color += 1
            missing[vertex] = color

    for edge in range(m):
        u = U[edge]
        v = V[edge]

        a = missing[u]
        b = missing[v]

        if a != b:
            path = []
            x = u
            wanted = b

            while True:
                d = incident[x]
                next_edge = None if d is None else d.get(wanted)
                if next_edge is None:
                    break

                path.append(next_edge)
                if U[next_edge] == x:
                    x = V[next_edge]
                else:
                    x = U[next_edge]
                wanted = a + b - wanted

            if path:
                end_vertex = x
                first_old = colors[path[0]]
                last_old = colors[path[-1]]

                for path_edge in path:
                    old_color = colors[path_edge]
                    new_color = a + b - old_color
                    p = U[path_edge]
                    q = V[path_edge]

                    dp = incident[p]
                    dq = incident[q]
                    del dp[old_color]
                    del dq[old_color]
                    dp[new_color] = path_edge
                    dq[new_color] = path_edge
                    colors[path_edge] = new_color

                if first_old < missing[u]:
                    missing[u] = first_old
                du = incident[u]
                c = missing[u]
                while c in du:
                    c += 1
                missing[u] = c

                if last_old < missing[end_vertex]:
                    missing[end_vertex] = last_old
                de = incident[end_vertex]
                c = missing[end_vertex]
                while c in de:
                    c += 1
                missing[end_vertex] = c

        colors[edge] = b
        add_color(u, b, edge)
        add_color(v, b, edge)

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, colors)))
    sys.stdout.write("\n")

if __name__ == "__main__":
    main()