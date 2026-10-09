import sys

def main():
    input = sys.stdin.readline
    j = int(input())
    ships = []
    total_p2 = 0
    for _ in range(j):
        p1, p2 = map(int, input().split())
        ships.append((p1 - p2, p1, p2))
        total_p2 += p2

    ships.sort(key=lambda x: x[0])  # ascending p1 - p2

    max_time = 0
    prefix_p1 = 0
    for d, p1, p2 in ships:
        prefix_p1 += p1
        # T(k) = prefix_p1 + (total_p2 - prefix_p2_so_far)
        # But we can also just track S + prefix_d
    # Easier: after sorting, compute prefix sums of d
    prefix_d = 0
    for d, _, _ in ships:
        prefix_d += d
        if prefix_d > max_time:
            max_time = prefix_d

    print(total_p2 + max_time)

if __name__ == "__main__":
    main()