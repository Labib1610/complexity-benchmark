import sys


def main():
    sys.setrecursionlimit(2000)
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    k = int(input_data[0])
    t = int(input_data[1])

    by_x = [[] for _ in range(k)]
    by_y = [[] for _ in range(k)]
    by_z = [[] for _ in range(k)]

    idx = 2
    for _ in range(t):
        x = int(input_data[idx]) - 1
        y = int(input_data[idx + 1]) - 1
        z = int(input_data[idx + 2]) - 1
        idx += 3
        triple = (x, y, z)
        by_x[x].append(triple)
        by_y[y].append(triple)
        by_z[z].append(triple)

    solution = []

    def backtrack(used_x, used_y, used_z, count_covered):
        if count_covered == k:
            return True

        best_type = -1
        best_val = -1
        best_triples = None
        min_deg = 1000000

        # Check Specialists (X)
        for x in range(k):
            if not (used_x & (1 << x)):
                valid = [
                    (cx, cy, cz)
                    for cx, cy, cz in by_x[x]
                    if not (used_y & (1 << cy)) and not (used_z & (1 << cz))
                ]
                cnt = len(valid)
                if cnt == 0:
                    return False
                if cnt < min_deg:
                    min_deg = cnt
                    best_triples = valid
                    if cnt == 1:
                        break

        # Check Machinery (Y)
        if min_deg > 1:
            for y in range(k):
                if not (used_y & (1 << y)):
                    valid = [
                        (cx, cy, cz)
                        for cx, cy, cz in by_y[y]
                        if not (used_x & (1 << cx)) and not (used_z & (1 << cz))
                    ]
                    cnt = len(valid)
                    if cnt == 0:
                        return False
                    if cnt < min_deg:
                        min_deg = cnt
                        best_triples = valid
                        if cnt == 1:
                            break

        # Check Shifts (Z)
        if min_deg > 1:
            for z in range(k):
                if not (used_z & (1 << z)):
                    valid = [
                        (cx, cy, cz)
                        for cx, cy, cz in by_z[z]
                        if not (used_x & (1 << cx)) and not (used_y & (1 << cy))
                    ]
                    cnt = len(valid)
                    if cnt == 0:
                        return False
                    if cnt < min_deg:
                        min_deg = cnt
                        best_triples = valid
                        if cnt == 1:
                            break

        for cx, cy, cz in best_triples:
            solution.append((cx + 1, cy + 1, cz + 1))
            if backtrack(
                used_x | (1 << cx),
                used_y | (1 << cy),
                used_z | (1 << cz),
                count_covered + 1,
            ):
                return True
            solution.pop()

        return False

    if backtrack(0, 0, 0, 0):
        print("YES")
        for cx, cy, cz in solution:
            print(f"{cx} {cy} {cz}")
    else:
        print("NO")


if __name__ == "__main__":
    main()