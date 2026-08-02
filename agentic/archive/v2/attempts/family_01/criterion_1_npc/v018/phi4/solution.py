from sys import stdin

def assign(worker, schedule, compatibility):
    for time_window in range(1, 4):
        if all(time_window != schedule[other_worker] or not (worker, other_worker) in compatibility and not (other_worker, worker) in compatibility for other_worker in range(len(schedule))):
            schedule[worker] = time_window
            return True
    return False

def solve(n, m, incompatible_pairs):
    compatibility = set(incompatible_pairs)
    schedule = [0] * n
    
    if all(assign(worker, schedule, compatibility) for worker in range(n)):
        print("YES")
        print(*schedule)
    else:
        print("NO")

if __name__ == "__main__":
    input_data = stdin.read().strip().split()
    index = 0
    n = int(input_data[index])
    m = int(input_data[index + 1])
    index += 2
    
    incompatible_pairs = []
    for _ in range(m):
        u = int(input_data[index]) - 1
        v = int(input_data[index + 1]) - 1
        incompatible_pairs.append((u, v))
        index += 2

    solve(n, m, incompatible_pairs)