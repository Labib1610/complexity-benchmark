import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)

    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        indeg[b] += 

    # Kahn's algorithm to get a topological order
    q = deque([i for i in range(1, n + 1) if indeg[i] == 0])
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            indeg[v] -= 
            if indeg[v] == 0:
                q.append(v)

    if len(topo) < n:
        # cycle exists
        print("NO")
        return

    # earliest possible room for each artifact
    earliest = [1] * (n + 1)
    for u in topo:
        for v in adj[u]:
            if earliest[v] < earliest[u] + 1:
                earliest[v] = earliest[u] + 1

    # If any earliest exceeds T, impossible
    for i in range(1, n + 1):
        if earliest[i] > T:
            print("NO")
            return

    # Now assign rooms greedily from earliest to latest,
    # respecting capacity M per room.
 We process artifacts in topological order,
    # but we need to assign them to rooms >= earliest.
 To minimize
    # room usage, we can try to put as many as possible in the
    # earliest available room that is >= earliest[i].
    # Since all artifacts have the same size, a greedy assignment
    # by increasing earliest works: keep a pointer to current room,
    # fill it up to M, then move on.
 However, an artifact with
    # larger earliest may force us to skip rooms.
 We'll use a min-heap
    # of available rooms? Actually simpler: sort artifacts by earliest,
    # then assign each to the smallest room >= earliest[i] that still has
    # capacity. Because M is uniform, we can maintain for each room
    # how many used. Use a heap of (room, used) for rooms that are
    # not full and >= current earliest. But we need to be careful:
    # if the smallest available room is < earliest[i], we discard it.

    order = sorted(range(1, n + 1), key=lambda x: earliest[x])
    room_assign = [0] * (n + 1)
    # heap entries: (room, used)
    heap = []
    idx = 
    for i in order:
        # push rooms as needed: we can push all rooms from 1..T,
        # but that's O(T) which may be large (T up to? not specified,
        # but likely manageable). To be safe, we only push rooms when needed.
        # We'll maintain next_room_to_push.

    next_room = 1
    for i in order:
        # Ensure heap has rooms >= earliest[i] with capacity
        while next_room <= T and next_room < earliest[i]:
            # rooms before earliest[i] are useless for this and later artifacts
            # (since later artifacts have >= earliest), so we can skip them.

            next_room += 
        # Now push rooms from next_room up to T? We can push one at a time
        # as needed. But we need the smallest room >= earliest[i] with free space.

        # We'll maintain a heap of (room, used) for rooms that are >= current
        # earliest and have free space. When we move to a new artifact,
        # we may need to add rooms that are now >= earliest[i].
        while next_room <= T:
            if next_room >= earliest[i]:
                heapq.heappush(heap, (next_room, 0))
                next_room += 
                # We can break after pushing one? No, we need all rooms
                # that could be candidates. But we can push incrementally:
                # only push the next room if it's >= earliest[i]; if it's <,
                # skip it. We'll do a loop that pushes all rooms from current
                # next_room up to T? That could be O(T) per artifact.

                # Better: we only need the smallest room >= earliest[i] with
                # free space. We can maintain a pointer to the smallest room
                # that is >= current earliest and has free space. Since we process
                # in increasing earliest, the pointer only moves forward.

                # Let's implement a simpler O(n + T) approach:
                # Precompute for each room the number of artifacts assigned.

                # We'll just iterate rooms from 1 to T and fill them greedily.

                # Actually, because M is uniform, we can do:
                # Sort artifacts by earliest. Then iterate rooms from 1 to T,
                # and assign up to M artifacts whose earliest <= current room.

                # This is O(n + T) and works because we don't care about order
                # among artifacts with same earliest. Let's do that.

    # Simpler correct approach:
    # Sort artifacts by earliest. Then for room from 1 to T:
    #   take up to M artifacts from the sorted list whose earliest <= room.

    # This respects capacities and earliest constraints. Since all artifacts
    # are independent except for earliest bounds, this is optimal.


    # Let's implement that.


    order = sorted(range(1, n + 1), key=lambda x: earliest[x])
    room_assign = [0] * (n + 1)
    ptr = 
    for room in range(1, T + 1):
        cnt = 
        while ptr < n and cnt < M:
            art = order[ptr]
            if earliest[art] <= room:
                room_assign[art] = room
                ptr += 
                cnt += 
            else:
                # This artifact and all later ones have earliest > room,
                # so we cannot assign them to this room. Break.

                break
        # If we've assigned all artifacts, we can stop early
        if ptr == n:
            break

    # Check if all assigned
    if ptr < n:
        print("NO")
        return

    # Also need to ensure that the assignment respects the original edges:
    # Since we assigned each artifact to a room >= earliest[art],
    # and earliest was computed from the DAG, it automatically satisfies
    # all edges: for edge u->v, earliest[v] >= earliest[u]+1, so
    # room[v] >= earliest[v] >= earliest[u]+1 >= room[u]+1? Wait,
    # room[u] could be > earliest[u], so we need to check that room[v] > room[u].
    # Our greedy assignment by earliest does not guarantee that for every edge,
    # room[v] > room[u]. Because we assign in order of earliest, but
    # room[u] might be large while room[v] might be small? No, because
    # earliest[v] > earliest[u], so in sorted order v comes after u.

    # When we assign rooms in increasing order, we assign u to some room
    # <= room[v]? Actually, since v comes later in sorted order, it will be
    # assigned to a room >= the room assigned to u? Not necessarily: if u has
    # earliest=1 and v earliest=2, u could be assigned to room 1, v to room 2.

    # But if u is assigned to room 3 (because room 1,2 were full of other
    # artifacts with earlier earliest), then v (earliest=2) could be assigned to room 2?
    # No, because v comes after u in sorted order, and we assign rooms in increasing
    # order. When we are at room 2, u might not yet be assigned if it's
    # still in the queue? Let's think carefully.



    # The greedy "fill each room with up to M artifacts whose earliest <= room"
    # processes rooms in increasing order. For each room, it takes the next
    # artifacts from the sorted list that have earliest <= room. This means that
    # artifacts are assigned to the smallest possible room that can take them,
    # but not necessarily in topological order? Actually, because we take from
    # the sorted list in order of earliest, and we assign to the current room,
    # an artifact with larger earliest will never be assigned to a smaller room
    # than an artifact with smaller earliest? Let's see: Suppose earliest[u]=1,
    # earliest[v]=2. Sorted order: u, v. We process room 1: assign u to 1.

    # Then room 2: assign v to 2. Good. If room 1 was full before u,
    # u might be assigned to room 2. Then v (earliest=2) could be assigned
    # to room 2 as well? But room 2 has capacity M. If u took one spot,
    # v can take another if capacity allows. That would put u and v in same room,
    # violating edge u->v. So this greedy is not safe for edges.


    # We need a different approach. We need to assign rooms such that for every
    # edge u->v, room[v] > room[u]. This is equivalent to assigning each artifact
    # a room in [earliest[i], T] such that the partial order is respected. This is
    # a scheduling problem on a DAG with unit processing time and capacity M per
    # time slot. This is known to be solvable by a greedy algorithm: process
    # rooms from 1 to T, at each room choose up to M artifacts whose all
    # predecessors have been assigned to earlier rooms. This is like topological
    # sorting with capacity. We can do that using a priority queue of available
    # artifacts (those with indegree 0 in the remaining graph) sorted by
    # their earliest? Actually, we need to ensure we don't assign an artifact
    # before its earliest. But if we process rooms in order, we can only assign
    # artifacts whose earliest <= current room and whose predecessors are done.


    # So algorithm:
    # 1. Compute earliest as before.

    # 2. Build a list of artifacts sorted by earliest. But we need to
    #    respect dependencies. We'll do a topological sort with capacity:
    #    Maintain a min-heap of available artifacts (indegree 0) keyed by
    #    earliest. For each room from 1 to T:
    #        Take up to M artifacts from the heap whose earliest <= room.

    #        Assign them to this room. Then for each assigned artifact, reduce
    #        indegree of successors; if a successor becomes available, push it
    #        into the heap.

    #    If at any room we cannot assign an artifact because the heap is empty
    #    or the smallest earliest > room, then we might still be able to assign
    #    later? Actually, if the smallest earliest > room, then no artifact can
    #    be placed in this room, so we just skip the room (leave it empty).
    #    But we must continue to later rooms. If we finish all artifacts, YES.
    #    If we run out of rooms before assigning all, NO.


    # This is correct because at each room we assign as many as possible from
    # the available set, choosing those with smallest earliest to avoid blocking
    # later rooms. This is a standard greedy for scheduling with release times
    # (earliest) and precedence constraints on identical machines (rooms as
    # time slots). It works because all processing times are 1 and capacity is
    # uniform.


    # Let's implement this.


    # Recompute indeg for the greedy (we already destroyed indeg in Kahn's).
    indeg = [0] * (n + 1)
    for u in range(1, n + 1):
        for v in adj[u]:
            indeg[v] += 

    import heapq
    heap = []
    for i in range(1, n + 1):
        if indeg[i] == 0:
            heapq.heappush(heap, (earliest[i], i))

    room_assign = [0] * (n + 1)
    assigned_count = 
    for room in range(1, T + 1):
        if assigned_count == n:
            break
        # We can assign up to M artifacts this room
        take = []
        while len(take) < M and heap:
            e, art = heap[0]
            if e <= room:
                heapq.heappop(heap)
                take.append(art)
            else:
                break
        if not take:
            # No artifact can be placed this room; continue
            continue
        for art in take:
            room_assign[art] = room
            assigned_count += 
            for v in adj[art]:
                indeg[v] -= 
                if indeg[v] == 0:
                    heapq.heappush(heap, (earliest[v], v))

    if assigned_count < n:
        print("NO")
        return

    # Verify all edges
    for u in range(1, n + 1):
        for v in adj[u]:
            if room_assign[u] >= room_assign[v]:
                # Should not happen, but check
                print("NO")
                return

    print("YES")
    print(' '.join(str(room_assign[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()