import sys
from array import array

def main():
    data = sys.stdin.buffer
    first = data.readline().split()
    if not first:
        return

    n_in, n_out, m = map(int, first)
    total_vertices = n_in + n_out

    left = array('I')
    right = array('I')
    degree = array('I', [0]) * total_vertices

    for _ in range(m):
        u, v = map(int, data.readline().split())
        u -= 1
        v = n_in + v - 1
        left.append(u)
        right.append(v)
        degree[u] += 1
        degree[v] += 1

    if m == 0:
        sys.stdout.write("YES\n\n")
        return

    delta = max(degree)
    colors = array('I', [0]) * m
    missing = array('I', [1]) * total_vertices

    shift = 20
    incidence = {}

    order = array('I', range(m))
    state = 0x9E3779B97F4A7C15
    mask64 = (1 << 64) - 1

    for i in range(m - 1, 0, -1):
        state ^= (state << 7) & mask64
        state ^= state >> 9
        state ^= (state << 8) & mask64
        j = state % (i + 1)
        order[i], order[j] = order[j], order[i]

    for edge_id in order:
        x = left[edge_id]
        y = right[edge_id]

        a = missing[x]
        while ((x << shift) | a) in incidence:
            a += 1
        missing[x] = a

        b = missing[y]
        while ((y << shift) | b) in incidence:
            b += 1
        missing[y] = b

        if a != b:
            path = []
            cur = x
            wanted = b

            while True:
                next_edge = incidence.get((cur << shift) | wanted, -1)
                if next_edge == -1:
                    break

                path.append(next_edge)
                if left[next_edge] == cur:
                    cur = right[next_edge]
                else:
                    cur = left[next_edge]

                wanted = a if wanted == b else b

            lost_at_end = b if wanted == a else a
            if lost_at_end < missing[cur]:
                missing[cur] = lost_at_end

            for pe in path:
                old_color = colors[pe]
                px = left[pe]
                py = right[pe]
                del incidence[(px << shift) | old_color]
                del incidence[(py << shift) | old_color]

            for pe in path:
                old_color = colors[pe]
                new_color = b if old_color == a else a
                colors[pe] = new_color
                px = left[pe]
                py = right[pe]
                incidence[(px << shift) | new_color] = pe
                incidence[(py << shift) | new_color] = pe

        colors[edge_id] = b
        incidence[(x << shift) | b] = edge_id
        incidence[(y << shift) | b] = edge_id

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, colors)))
    sys.stdout.write("\n")

if __name__ == "__main__":
    main()