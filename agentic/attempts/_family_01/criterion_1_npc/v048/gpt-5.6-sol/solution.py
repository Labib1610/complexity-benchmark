import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    adj = [0] * n
    pos = 2
    for _ in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2
        if u != v:
            adj[u] |= 1 << v
            adj[v] |= 1 << u

    def bipartition(mask):
        unseen = mask
        left = 0
        right = 0

        while unseen:
            seed = unseen & -unseen
            unseen ^= seed
            left |= seed
            stack = seed

            while stack:
                vb = stack & -stack
                stack ^= vb
                v = vb.bit_length() - 1
                neighbors = adj[v] & mask

                if left & vb:
                    if neighbors & left:
                        return None
                    new_vertices = neighbors & unseen
                    unseen ^= new_vertices
                    right |= new_vertices
                    stack |= new_vertices
                else:
                    if neighbors & right:
                        return None
                    new_vertices = neighbors & unseen
                    unseen ^= new_vertices
                    left |= new_vertices
                    stack |= new_vertices

        return left, right

    colors = [0] * n

    def assign(mask, color):
        while mask:
            bit = mask & -mask
            mask ^= bit
            colors[bit.bit_length() - 1] = color

    def solve_component(component):
        initial = bipartition(component)
        if initial is not None:
            assign(initial[0], 1)
            assign(initial[1], 2)
            return True

        vertices = component
        start = -1
        best_degree = -1
        while vertices:
            bit = vertices & -vertices
            vertices ^= bit
            v = bit.bit_length() - 1
            degree = (adj[v] & component).bit_count()
            if degree > best_degree:
                best_degree = degree
                start = v

        complement_neighbors = [0] * n
        vertices = component
        while vertices:
            bit = vertices & -vertices
            vertices ^= bit
            v = bit.bit_length() - 1
            complement_neighbors[v] = component & ~adj[v] & ~bit

        start_bit = 1 << start
        result = None

        def search(independent, candidates, excluded):
            nonlocal result

            fixed = component & ~(independent | candidates)
            fixed_partition = bipartition(fixed)
            if fixed_partition is None:
                return False

            remaining = component & ~independent
            if remaining == fixed:
                partition = fixed_partition
            else:
                partition = bipartition(remaining)

            if partition is not None:
                result = (independent, partition[0], partition[1])
                return True

            union = candidates | excluded
            if not union:
                return False

            pivot = -1
            max_count = -1
            temp = union
            while temp:
                bit = temp & -temp
                temp ^= bit
                u = bit.bit_length() - 1
                count = (candidates & complement_neighbors[u]).bit_count()
                if count > max_count:
                    max_count = count
                    pivot = u

            branch_vertices = candidates & ~complement_neighbors[pivot]

            while branch_vertices:
                bit = branch_vertices & -branch_vertices
                branch_vertices ^= bit
                v = bit.bit_length() - 1

                if search(
                    independent | bit,
                    candidates & complement_neighbors[v],
                    excluded & complement_neighbors[v]
                ):
                    return True

                candidates ^= bit
                excluded |= bit

            return False

        initial_candidates = complement_neighbors[start]
        if not search(start_bit, initial_candidates, 0):
            return False

        independent, left, right = result
        assign(left, 1)
        assign(right, 2)
        assign(independent, 3)
        return True

    unseen = (1 << n) - 1
    while unseen:
        seed = unseen & -unseen
        component = 0
        frontier = seed
        unseen ^= seed

        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            v = bit.bit_length() - 1
            component |= bit
            new_vertices = adj[v] & unseen
            unseen ^= new_vertices
            frontier |= new_vertices

        if not solve_component(component):
            print("NO")
            return

    print("YES")
    print(*colors)

if __name__ == "__main__":
    main()