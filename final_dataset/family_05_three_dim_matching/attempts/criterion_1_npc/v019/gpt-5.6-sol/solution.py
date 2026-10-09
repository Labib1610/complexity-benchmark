import sys

sys.setrecursionlimit(1_000_000)


def has_perfect_matching(adj, n):
    match = [-1] * n

    def augment(u, seen):
        candidates = adj[u]
        while candidates:
            bit = candidates & -candidates
            candidates -= bit
            v = bit.bit_length() - 1
            if seen[v]:
                continue
            seen[v] = True
            if match[v] == -1 or augment(match[v], seen):
                match[v] = u
                return True
        return False

    for u in range(n):
        if not augment(u, [False] * n):
            return False
    return True


def solve_component(component_columns, component_rows, triples):
    column_index = {c: i for i, c in enumerate(component_columns)}
    column_count = len(component_columns)
    row_count = len(component_rows)

    row_columns = [None] * row_count
    column_rows = [0] * column_count

    for local_row, original_row in enumerate(component_rows):
        x, y, z = triples[original_row]
        cols = (
            column_index[x],
            column_index[y + K],
            column_index[z + 2 * K]
        )
        row_columns[local_row] = cols
        bit = 1 << local_row
        column_rows[cols[0]] |= bit
        column_rows[cols[1]] |= bit
        column_rows[cols[2]] |= bit

    for rows in column_rows:
        if rows == 0:
            return None

    degrees = [rows.bit_count() for rows in column_rows]
    row_score = [
        degrees[a] + degrees[b] + degrees[c]
        for a, b, c in row_columns
    ]

    all_columns = (1 << column_count) - 1
    all_rows = (1 << row_count) - 1
    failed = set()
    memo_limit = 1_500_000
    path = []

    def dfs(covered, active):
        if covered == all_columns:
            return True
        if covered in failed:
            return False

        uncovered = all_columns ^ covered
        best_candidates = 0
        best_count = row_count + 1

        bits = uncovered
        while bits:
            col_bit = bits & -bits
            bits -= col_bit
            col = col_bit.bit_length() - 1
            candidates = column_rows[col] & active
            count = candidates.bit_count()
            if count == 0:
                if len(failed) < memo_limit:
                    failed.add(covered)
                return False
            if count < best_count:
                best_count = count
                best_candidates = candidates
                if count == 1:
                    break

        candidates_list = []
        bits = best_candidates
        while bits:
            row_bit = bits & -bits
            bits -= row_bit
            row = row_bit.bit_length() - 1
            candidates_list.append(row)

        if len(candidates_list) > 1:
            candidates_list.sort(key=row_score.__getitem__)

        for row in candidates_list:
            a, b, c = row_columns[row]
            new_covered = covered | (1 << a) | (1 << b) | (1 << c)
            conflicts = column_rows[a] | column_rows[b] | column_rows[c]
            new_active = active & ~conflicts
            path.append(row)
            if dfs(new_covered, new_active):
                return True
            path.pop()

        if len(failed) < memo_limit:
            failed.add(covered)
        return False

    if not dfs(0, all_rows):
        return None
    return [component_rows[r] for r in path]


data = list(map(int, sys.stdin.buffer.read().split()))
if len(data) < 2:
    sys.exit()

K, t = data[0], data[1]
triples = []

xy = [0] * K
xz = [0] * K
yz = [0] * K

parent = list(range(3 * K))
size = [1] * (3 * K)


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if size[a] < size[b]:
        a, b = b, a
    parent[b] = a
    size[a] += size[b]


pos = 2
for _ in range(t):
    x = data[pos] - 1
    y = data[pos + 1] - 1
    z = data[pos + 2] - 1
    pos += 3

    triples.append((x, y, z))
    xy[x] |= 1 << y
    xz[x] |= 1 << z
    yz[y] |= 1 << z

    union(x, y + K)
    union(x, z + 2 * K)

if t < K:
    print("NO")
    sys.exit()

if (not has_perfect_matching(xy, K) or
        not has_perfect_matching(xz, K) or
        not has_perfect_matching(yz, K)):
    print("NO")
    sys.exit()

component_columns = {}
for column in range(3 * K):
    root = find(column)
    component_columns.setdefault(root, []).append(column)

component_rows = {root: [] for root in component_columns}
for i, (x, y, z) in enumerate(triples):
    component_rows[find(x)].append(i)

components = []
for root, columns in component_columns.items():
    count_x = sum(c < K for c in columns)
    count_y = sum(K <= c < 2 * K for c in columns)
    count_z = len(columns) - count_x - count_y

    if count_x != count_y or count_x != count_z:
        print("NO")
        sys.exit()

    rows = component_rows[root]
    if not rows:
        print("NO")
        sys.exit()

    components.append((len(rows) / count_x, columns, rows))

components.sort(key=lambda item: item[0])

answer = []
for _, columns, rows in components:
    selected = solve_component(columns, rows, triples)
    if selected is None:
        print("NO")
        sys.exit()
    answer.extend(selected)

if len(answer) != K:
    print("NO")
else:
    output = ["YES"]
    for row in answer:
        x, y, z = triples[row]
        output.append(f"{x + 1} {y + 1} {z + 1}")
    print("\n".join(output))