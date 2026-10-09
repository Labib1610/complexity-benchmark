import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[0], data[1]

    parent = list(range(n))
    size = [1] * n
    parity = [0] * n  # parity[x] = value[x] XOR value[parent[x]]

    def find(x):
        root = x
        total = 0
        while parent[root] != root:
            total ^= parity[root]
            root = parent[root]

        cur = x
        prefix = 0
        while parent[cur] != cur:
            nxt = parent[cur]
            edge = parity[cur]
            parent[cur] = root
            parity[cur] = total ^ prefix
            prefix ^= edge
            cur = nxt

        return root, total

    pos = 2
    for _ in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2

        ru, pu = find(u)
        rv, pv = find(v)

        if ru == rv:
            if (pu ^ pv) != 1:
                print("NO")
                return
        else:
            relation = pu ^ pv ^ 1
            if size[ru] < size[rv]:
                parent[ru] = rv
                parity[ru] = relation
                size[rv] += size[ru]
            else:
                parent[rv] = ru
                parity[rv] = relation
                size[ru] += size[rv]

    orientation = [-1] * n
    answer = [0] * n

    for i in range(n):
        root, p = find(i)
        if orientation[root] == -1:
            orientation[root] = p
        answer[i] = 1 + (p ^ orientation[root])

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, answer)))

if __name__ == "__main__":
    main()