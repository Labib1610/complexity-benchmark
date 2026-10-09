import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    jobs_count = next(it)
    machines_count = next(it)
    deadline = next(it)

    machines = []
    durations = []
    total_operations = 0

    for _ in range(jobs_count):
        count = next(it)
        job_machines = []
        job_durations = []
        for _ in range(count):
            job_machines.append(next(it) - 1)
            job_durations.append(next(it))
        machines.append(job_machines)
        durations.append(job_durations)
        total_operations += count

    suffix = []
    for job in range(jobs_count):
        count = len(durations[job])
        values = [0] * (count + 1)
        for k in range(count - 1, -1, -1):
            values[k] = values[k + 1] + durations[job][k]
        suffix.append(values)
        if values[0] > deadline:
            print("NO")
            return

    machine_load = [0] * machines_count
    for job in range(jobs_count):
        for machine, duration in zip(machines[job], durations[job]):
            machine_load[machine] += duration
    if any(load > deadline for load in machine_load):
        print("NO")
        return

    if total_operations == 0:
        out = ["YES"] + [""] * jobs_count
        sys.stdout.write("\n".join(out) + "\n")
        return

    sys.setrecursionlimit(max(10000, total_operations + 100))

    next_operation = [0] * jobs_count
    job_ready = [0] * jobs_count
    machine_ready = [0] * machines_count
    remaining_machine_load = machine_load[:]
    starts = [[0] * len(durations[j]) for j in range(jobs_count)]

    failed = set()
    cache_limit = 300000
    use_strong_bounds = total_operations <= 400

    def strong_bounds():
        per_machine = [[] for _ in range(machines_count)]

        for j in range(jobs_count):
            k = next_operation[j]
            release = job_ready[j]
            count = len(durations[j])
            while k < count:
                machine = machines[j][k]
                duration = durations[j][k]
                tail = suffix[j][k + 1]
                per_machine[machine].append((release, duration, tail))
                release += duration
                k += 1

        for machine, operations in enumerate(per_machine):
            if not operations:
                continue

            available = machine_ready[machine]

            by_release = sorted(operations, key=lambda x: x[0], reverse=True)
            load = 0
            for release, duration, _ in by_release:
                load += duration
                if max(available, release) + load > deadline:
                    return False

            by_tail = sorted(operations, key=lambda x: x[2], reverse=True)
            load = 0
            for _, duration, tail in by_tail:
                load += duration
                if available + load + tail > deadline:
                    return False

        return True

    def dfs(done):
        if done == total_operations:
            return True

        for j in range(jobs_count):
            k = next_operation[j]
            if k < len(durations[j]) and job_ready[j] + suffix[j][k] > deadline:
                return False

        for machine in range(machines_count):
            if machine_ready[machine] + remaining_machine_load[machine] > deadline:
                return False

        if use_strong_bounds and not strong_bounds():
            return False

        key = tuple(next_operation) + tuple(job_ready) + tuple(machine_ready)
        if key in failed:
            return False

        available_operations = []
        minimum_finish = None
        pivot_index = -1

        for j in range(jobs_count):
            k = next_operation[j]
            if k >= len(durations[j]):
                continue
            machine = machines[j][k]
            duration = durations[j][k]
            start = max(job_ready[j], machine_ready[machine])
            finish = start + duration
            index = len(available_operations)
            available_operations.append((j, k, machine, duration, start, finish))
            if minimum_finish is None or finish < minimum_finish:
                minimum_finish = finish
                pivot_index = index

        if minimum_finish is None or minimum_finish > deadline:
            if len(failed) < cache_limit:
                failed.add(key)
            return False

        pivot_machine = available_operations[pivot_index][2]
        candidates = []

        for index, operation in enumerate(available_operations):
            j, k, machine, duration, start, finish = operation
            if machine == pivot_machine and (
                index == pivot_index or start < minimum_finish
            ):
                tail = suffix[j][k + 1]
                if finish + tail <= deadline:
                    slack = deadline - finish - tail
                    candidates.append((slack, -tail, -duration, operation))

        candidates.sort(key=lambda x: (x[0], x[1], x[2]))

        for _, _, _, operation in candidates:
            j, k, machine, duration, start, finish = operation

            old_job_ready = job_ready[j]
            old_machine_ready = machine_ready[machine]

            next_operation[j] = k + 1
            job_ready[j] = finish
            machine_ready[machine] = finish
            remaining_machine_load[machine] -= duration
            starts[j][k] = start

            if dfs(done + 1):
                return True

            next_operation[j] = k
            job_ready[j] = old_job_ready
            machine_ready[machine] = old_machine_ready
            remaining_machine_load[machine] += duration

        if len(failed) < cache_limit:
            failed.add(key)
        return False

    if not dfs(0):
        print("NO")
        return

    output = ["YES"]
    for job_starts in starts:
        output.append(" ".join(map(str, job_starts)))
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()