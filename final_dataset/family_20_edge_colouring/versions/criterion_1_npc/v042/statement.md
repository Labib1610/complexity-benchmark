# Problem A — High-Pressure Flushing Schedule

Time limit: 5 s   Memory limit: 256 MB

## Description
A municipal water authority is certifying a newly built distribution grid. The grid consists of intersections connected by pipelines. The network was designed with a strict uniform topology: every intersection is the meeting point of exactly three pipelines.

To certify the grid, every pipeline must undergo a high-pressure flush. The certification process is divided into exactly three distinct flushing cycles: 1, 2, and 3. Each pipeline must be assigned to exactly one of these cycles.

The intersections are equipped with safety valves that can only manage the flow of one high-pressure flush at a time. If two or more pipelines connected to the same intersection are flushed during the same cycle, the conflicting pressures will rupture the intersection's valves. Therefore, the three pipelines meeting at any given intersection must each be assigned to a different flushing cycle.

Determine if it is possible to schedule the flushes under these strict conditions, and if so, provide a valid cycle assignment for each pipeline.

## Input
The first line contains two integers **n** and **m** (n even, m = 3n/2, 2 ≤ n ≤ 2000), representing the number of intersections and pipelines, respectively.
Each of the next **m** lines contains two integers u and v (1 ≤ u < v ≤ n), indicating a pipeline connecting intersection u and intersection v.

## Output
If a safe flushing schedule exists, print `YES` on the first line. On the second line, print **m** space-separated integers from the set {1, 2, 3} — the flushing cycle assigned to each pipeline in input order (pipelines meeting at the same intersection must have different cycles). Otherwise, print `NO`.

## Example
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
YES
1 2 3 3 2 1
```
