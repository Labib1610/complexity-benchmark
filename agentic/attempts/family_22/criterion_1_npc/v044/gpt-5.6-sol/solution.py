import sys
import heapq
import itertools

sys.setrecursionlimit(1_000_000)

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

it = iter(data)
n = next(it)
M = next(it)
T = next(it)
m = next(it)

adj = [[] for _ in range(n)]
radj = [[] for _ in range(n)]
indeg = [0] * n
outdeg = [0] * n

for _ in range(m):
    a = next(it) - 1
    b = next(it) - 1
    adj[a].append(b)
    radj[b].append(a)
    indeg[b] += 1
    outdeg[a] += 1

if M <= 0 or T <= 0 or n > M * T:
    print("NO")
    sys.exit()

# Topological ordering and cycle detection.
deg = indeg[:]
q = [i for i in range(n) if deg[i] == 0]
heapq.heapify(q)
topo = []

while q:
    u = heapq.heappop(q)
    topo.append(u)
    for v in adj[u]:
        deg[v] -= 1
        if deg[v] == 0:
            heapq.heappush(q, v)

if len(topo) != n:
    print("NO")
    sys.exit()

# Earliest possible slot and longest remaining path.
earliest = [1] * n
for u in topo:
    nu = earliest[u] + 1
    for v in adj[u]:
        if earliest[v] < nu:
            earliest[v] = nu

bottom = [1] * n
for u in reversed(topo):
    best = 1
    for v in adj[u]:
        x = bottom[v] + 1
        if x > best:
            best = x
    bottom[u] = best

if max(earliest, default=0) > T:
    print("NO")
    sys.exit()

latest = [T - bottom[i] + 1 for i in range(n)]

def valid(ans):
    if ans is None:
        return False
    count = [0] * (T + 1)
    for x in ans:
        if x < 1 or x > T:
            return False
        count[x] += 1
        if count[x] > M:
            return False
    for u in range(n):
        au = ans[u]
        for v in adj[u]:
            if au >= ans[v]:
                return False
    return True

def hash_key(x, seed):
    z = (x + 1) * 0x9E3779B185EBCA87 + seed * 0xC2B2AE3D27D4EB4F
    z &= (1 << 64) - 1
    z ^= z >> 30
    z = (z * 0xBF58476D1CE4E5B9) & ((1 << 64) - 1)
    z ^= z >> 27
    z = (z * 0x94D049BB133111EB) & ((1 << 64) - 1)
    z ^= z >> 31
    return z

def greedy_forward(mode):
    d = indeg[:]
    h = []

    def key(u):
        if mode == 0:
            return (-bottom[u], -outdeg[u], u)
        if mode == 1:
            return (-outdeg[u], -bottom[u], u)
        return (hash_key(u, mode), -bottom[u], u)

    for u in range(n):
        if d[u] == 0:
            heapq.heappush(h, (key(u), u))

    ans = [0] * n
    done = 0
    slot = 1

    while h:
        if slot > T:
            return None
        batch = []
        for _ in range(min(M, len(h))):
            _, u = heapq.heappop(h)
            batch.append(u)
            ans[u] = slot
        done += len(batch)
        for u in batch:
            for v in adj[u]:
                d[v] -= 1
                if d[v] == 0:
                    heapq.heappush(h, (key(v), v))
        slot += 1

    return ans if done == n else None

def greedy_backward(mode):
    d = outdeg[:]
    h = []

    def key(u):
        if mode == 0:
            return (-earliest[u], -indeg[u], u)
        if mode == 1:
            return (-indeg[u], -earliest[u], u)
        return (hash_key(u, mode + 17), -earliest[u], u)

    for u in range(n):
        if d[u] == 0:
            heapq.heappush(h, (key(u), u))

    ans = [0] * n
    done = 0
    slot = T

    while h:
        if slot < 1:
            return None
        batch = []
        for _ in range(min(M, len(h))):
            _, u = heapq.heappop(h)
            batch.append(u)
            ans[u] = slot
        done += len(batch)
        for u in batch:
            for p in radj[u]:
                d[p] -= 1
                if d[p] == 0:
                    heapq.heappush(h, (key(p), p))
        slot -= 1

    return ans if done == n else None

for mode in (0, 1, 2, 3):
    ans = greedy_forward(mode)
    if valid(ans):
        print("YES")
        print(*ans)
        sys.exit()

for mode in (0, 1, 2, 3):
    ans = greedy_backward(mode)
    if valid(ans):
        print("YES")
        print(*ans)
        sys.exit()

# Necessary feasibility check using precedence-derived release times/deadlines.
jobs = sorted(range(n), key=lambda x: earliest[x])
deadline_heap = []
window_ans = [0] * n
pos = 0
time = 1
window_possible = True

while pos < n or deadline_heap:
    if not deadline_heap and pos < n and time < earliest[jobs[pos]]:
        time = earliest[jobs[pos]]

    while pos < n and earliest[jobs[pos]] <= time:
        u = jobs[pos]
        heapq.heappush(deadline_heap, (latest[u], u))
        pos += 1

    for _ in range(M):
        if not deadline_heap:
            break
        d, u = heapq.heappop(deadline_heap)
        if d < time:
            window_possible = False
            break
        window_ans[u] = time

    if not window_possible:
        break
    time += 1
    if time > T + 1 and (pos < n or deadline_heap):
        window_possible = False
        break

if not window_possible:
    print("NO")
    sys.exit()

if valid(window_ans):
    print("YES")
    print(*window_ans)
    sys.exit()

# Exact search over non-delay schedules.
# Search in the direction having fewer initially available operations.
reverse_search = sum(x == 0 for x in outdeg) < sum(x == 0 for x in indeg)

if not reverse_search:
    search_adj = adj
    search_pred = radj
    search_bottom = bottom
    search_latest = latest
else:
    search_adj = radj
    search_pred = adj
    search_bottom = earliest
    search_latest = [T - earliest[i] + 1 for i in range(n)]

pred_mask = [0] * n
for u in range(n):
    mask = 0
    for p in search_pred[u]:
        mask |= 1 << p
    pred_mask[u] = mask

all_mask = (1 << n) - 1
assignment = [0] * n
failed = set()

def exact(mask, slot):
    if mask == all_mask:
        return True
    if slot > T:
        return False

    remaining = n - mask.bit_count()
    if remaining > (T - slot + 1) * M:
        return False

    state = (mask, slot)
    if state in failed:
        return False

    available = []
    mandatory = []

    unseen = all_mask ^ mask
    x = unseen
    while x:
        bit = x & -x
        u = bit.bit_length() - 1
        x -= bit

        if search_latest[u] < slot:
            failed.add(state)
            return False

        is_available = (pred_mask[u] & ~mask) == 0
        if search_latest[u] == slot:
            if not is_available:
                failed.add(state)
                return False
            mandatory.append(u)
        if is_available:
            available.append(u)

    if not available or len(mandatory) > M:
        failed.add(state)
        return False

    available.sort(key=lambda u: (-search_bottom[u], -len(search_adj[u]), u))

    if len(available) <= M:
        chosen = available
        new_mask = mask
        for u in chosen:
            assignment[u] = slot
            new_mask |= 1 << u
        if exact(new_mask, slot + 1):
            return True
        for u in chosen:
            assignment[u] = 0
        failed.add(state)
        return False

    mandatory_set = set(mandatory)
    optional = [u for u in available if u not in mandatory_set]
    need = M - len(mandatory)

    for extra in itertools.combinations(optional, need):
        chosen = mandatory + list(extra)
        new_mask = mask
        for u in chosen:
            assignment[u] = slot
            new_mask |= 1 << u

        if exact(new_mask, slot + 1):
            return True

        for u in chosen:
            assignment[u] = 0

    failed.add(state)
    return False

if exact(0, 1):
    if reverse_search:
        assignment = [T + 1 - x for x in assignment]
    if valid(assignment):
        print("YES")
        print(*assignment)
        sys.exit()

print("NO")