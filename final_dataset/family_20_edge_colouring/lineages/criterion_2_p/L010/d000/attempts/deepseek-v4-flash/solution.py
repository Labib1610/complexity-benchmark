import sys
import heapq

def solve():
    input = sys.stdin.readline
    nL, nR, m = map(int, input().split())
    total = nL + nR
    # vertices: 1..nL (left), nL+1..nL+nR (right)
    edges = []
    deg = [0] * (total + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        v2 = nL + v
        edges.append((u, v2))
        deg[u] += 1
        deg[v2] += 1

    Delta = max(deg) if m > 0 else 0

    # used colors per vertex
    used = [set() for _ in range(total + 1)]
    # min-heap of free colors per vertex
    free_heap = [list(range(1, Delta + 1)) for _ in range(total + 1)]
    for i in range(total + 1):
        heapq.heapify(free_heap[i])

    # edge_color[vertex][color] = neighbor
    edge_color = [dict() for _ in range(total + 1)]
    color_of_edge = [0] * m

    def get_free(vertex):
        h = free_heap[vertex]
        while h and h[0] in used[vertex]:
            heapq.heappop(h)
        if not h:
            return Delta + 1
        return h[0]

    def assign(vertex, neighbor, color):
        used[vertex].add(color)
        used[neighbor].add(color)
        edge_color[vertex][color] = neighbor
        edge_color[neighbor][color] = vertex

    def flip_path(start, c1, c2):
        cur = start
        col1, col2 = c1, c2
        while True:
            nxt = edge_color[cur].get(col1)
            if nxt is None:
                break
            # remove old color
            used[cur].discard(col1)
            used[nxt].discard(col1)
            del edge_color[cur][col1]
            del edge_color[nxt][col1]
            heapq.heappush(free_heap[cur], col1)
            heapq.heappush(free_heap[nxt], col1)
            # add new color
            used[cur].add(col2)
            used[nxt].add(col2)
            edge_color[cur][col2] = nxt
            edge_color[nxt][col2] = cur
            # move to next
            cur = nxt
            col1, col2 = col2, col1

    for idx, (u, v) in enumerate(edges):
        c1 = get_free(u)
        c2 = get_free(v)
        if c1 != c2:
            assign(u, v, c1)
            color_of_edge[idx] = c1
        else:
            c = c1
            # find a color d free at v
            d = c
            while d in used[v]:
                d += 1
            # flip alternating path from u with colors c and d
            flip_path(u, c, d)
            # now assign c to (u,v)
            assign(u, v, c)
            color_of_edge[idx] = c

    out = ["YES", " ".join(map(str, color_of_edge))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()