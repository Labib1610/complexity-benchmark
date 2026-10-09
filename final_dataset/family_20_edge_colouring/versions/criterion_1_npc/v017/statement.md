# Problem A — Rotating Maintenance Windows on the Trunk Grid

Time limit: 5 s   Memory limit: 256 MB

## Description
The utility's infrastructure upgrade pipeline operates in three sequential phases. 

**Phase 1: Topology Verification**
Ground-penetrating radar and historical blueprints are reconciled to produce a verified map of the trunk grid. This initial phase has already concluded, yielding a strict layout where every junction serves as a meeting point for exactly three cable conduits. 

**Phase 2: Schedule Generation (Your Task)**
The temporal distribution of maintenance work must be planned. There are exactly three rotating service windows available. Your module must assign each cable conduit to one of these three windows. Taking a conduit offline consumes a whole window. Safety rules mandate that a junction cannot maintain structural continuity if two of its three connected conduits are taken offline simultaneously. Consequently, at any given junction, all three incident conduits must be assigned to distinctly different service windows. 

**Phase 3: Logistics Dispatch**
Once a valid schedule is generated, an external logistics engine uses it to dispatch crews, allocate heavy machinery, and route traffic around work zones. If no valid schedule exists for the given topology, the pipeline halts and the grid must be redesigned.

Your program is responsible only for Phase 2. Given the verified topology from Phase 1, determine if a valid schedule exists. If it does, output the window assignments so Phase 3 can proceed.

## Input
The first line contains two integers `n` and `m` (`n` is even, `m = 3n/2`, `2 ≤ n ≤ 2000`), representing the number of junctions and cable conduits, respectively.
Each of the following `m` lines contains two integers `u` and `v` (`1 ≤ u < v ≤ n`), indicating a conduit connecting junction `u` and junction `v`.

## Output
If the schedule generation is successful, print `YES` on the first line. On the second line, print `m` integers, each either `1`, `2`, or `3`, representing the service window assigned to each conduit in the order they were provided in the input. If multiple valid schedules exist, any may be passed to Phase 3.
If the constraints make it impossible to schedule the maintenance within three windows, print `NO`.

## Example
### Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
### Output:
```
YES
1 2 3 3 2 1
```
