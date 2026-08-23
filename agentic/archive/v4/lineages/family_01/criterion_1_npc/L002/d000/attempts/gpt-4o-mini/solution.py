def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.read
    data = input().splitlines()

    n, m = map(int, data[0].split())
    incompatible_pairs = [tuple(map(int, line.split())) for line in data[1:m + 1]]

    graph = defaultdict(list)
    for u, v in incompatible_pairs:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    # To store the slot assignments
    slots = [-1] * n

    def can_assign(person):
        if person == n:
            return True  # All personnel are assigned

        if slots[person] != -1:
            return can_assign(person + 1)  # Already assigned, move to the next

        for slot in range(1, 4):
            # Check if this slot is compatible with all adjacent personnel
            if all(slots[neigh] != slot for neigh in graph[person]):
                slots[person] = slot
                if can_assign(person + 1):
                    return True
                slots[person] = -1  # Backtrack

        return False
    
    if can_assign(0):
        print("YES")
        print(" ".join(map(str, slots)))
    else:
        print("NO")

if __name__ == "__main__":
    main()