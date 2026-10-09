import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    k = int(input_data[0])
    t = int(input_data[1])
    
    if t < k:
        print("NO")
        return

    commands = []
    idx = 2
    for _ in range(t):
        x = int(input_data[idx]) - 1
        y = int(input_data[idx+1]) - 1
        z = int(input_data[idx+2]) - 1
        idx += 3
        commands.append((x, y, z))

    # Items: 0..k-1 for A, k..2k-1 for B, 2k..3k-1 for C
    num_items = 3 * k
    
    # Store options
    # Each option covers 3 items: x, k + y, 2k + z
    options = []
    for x, y, z in commands:
        options.append((x, k + y, 2k + z))

    # DLX structures using arrays
    item_options = [[] for _ in range(num_items)]
    for opt_idx, (c1, c2, c3) in enumerate(options):
        item_options[c1].append(opt_idx)
        item_options[c2].append(opt_idx)
        item_options[c3].append(opt_idx)

    # Quick check: if any item has 0 options, impossible
    for i in range(num_items):
        if not item_options[i]:
            print("NO")
            return

    # Algorithm X state
    item_active = [True] * num_items
    option_active = [True] * t
    chosen_options = []

    # To efficiently find the item with minimum remaining options,
    # we maintain counts of active options per item.
    item_count = [len(opts) for opts in item_options]

    def cover(item):
        item_active[item] = False
        for opt in item_options[item]:
            if option_active[opt]:
                option_active[opt] = False
                c1, c2, c3 = options[opt]
                item_count[c1] -= 1
                item_count[c2] -= 1
                item_count[c3] -= 1

    def uncover(item, deactivated_options):
        for opt in deactivated_options:
            option_active[opt] = True
            c1, c2, c3 = options[opt]
            item_count[c1] += 1
            item_count[c2] += 1
            item_count[c3] += 1
        item_active[item] = True

    # Iterative / recursive search with MRV
    def search(num_uncovered):
        if num_uncovered == 0:
            return True

        # Choose item with minimum remaining active options
        min_c = -1
        min_val = 1000000000

        for i in range(num_items):
            if item_active[i]:
                cnt = item_count[i]
                if cnt < min_val:
                    min_val = cnt
                    min_c = i
                    if min_val == 0:
                        break

        if min_val == 0 or min_c == -1:
            return False

        chosen_item = min_c

        # Candidates for chosen_item
        # We need to iterate over options that cover chosen_item and are currently active
        candidates = [opt for opt in item_options[chosen_item] if option_active[opt]]

        for opt in candidates:
            chosen_options.append(opt)
            c1, c2, c3 = options[opt]

            # Cover items c1, c2, c3
            # We record all newly deactivated options so we can backtrack
            newly_deactivated = []
            
            for c in (c1, c2, c3):
                item_active[c] = False
                for other_opt in item_options[c]:
                    if option_active[other_opt]:
                        option_active[other_opt] = False
                        c_a, c_b, c_c = options[other_opt]
                        item_count[c_a] -= 1
                        item_count[c_b] -= 1
                        item_count[c_c] -= 1
                        newly_deactivated.append(other_opt)

            if search(num_uncovered - 3):
                return True

            # Backtrack
            for other_opt in newly_deactivated:
                option_active[other_opt] = True
                c_a, c_b, c_c = options[other_opt]
                item_count[c_a] += 1
                item_count[c_b] += 1
                item_count[c_c] += 1

            for c in (c1, c2, c3):
                item_active[c] = True

            chosen_options.pop()

        return False

    if search(num_items):
        print("YES")
        out = []
        for opt in chosen_options:
            x, y, z = commands[opt]
            out.append(f"{x + 1} {y + 1} {z + 1}")
        print("\n".join(out))
    else:
        print("NO")

if __name__ == '__main__':
    solve()