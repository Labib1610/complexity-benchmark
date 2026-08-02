from sys import stdin

def assign_shifts(n, m, incompatibilities):
    graph = [[] for _ in range(n)]
    for u, v in incompatibilities:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    shifts = [0] * n
    def is_valid():
        for i in range(n):
            if shifts[i] == 0:
                return True
        for u in range(n):
            for v in graph[u]:
                if shifts[u] == shifts[v]:
                    return False
        return True

    def try_assign_shift(shift, staff):
        shifts[staff] = shift
        if is_valid():
            if shift == 3 or (staff + 1) < n:
                next_staff = staff + 1
                if try_assign_shift(1, next_staff):
                    return True
            if shift == 1 or (shift == 2 and try_assign_shift(3, staff)):
                if is_valid():
                    if shift == 2 or (staff + 1) < n:
                        next_staff = staff + 1
                        if try_assign_shift(1, next_staff):
                            return True
        shifts[staff] = 0
        return False

    if not try_assign_shift(1, 0):
        return "NO"
    
    return "YES\n" + ' '.join(map(str, shifts))

# Input reading and function execution
input_data = stdin.read().strip().split()
n = int(input_data[0])
m = int(input_data[1])
incompatibilities = []
index = 2
for _ in range(m):
    u = int(input_data[index])
    v = int(input_data[index + 1])
    incompatibilities.append((u, v))
    index += 2

result = assign_shifts(n, m, incompatibilities)
print(result)