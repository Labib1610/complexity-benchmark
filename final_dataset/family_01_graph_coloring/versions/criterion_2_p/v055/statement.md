# Problem B — Security Patch Scheduling

Time limit: 1 s   Memory limit: 256 MB

An infrastructure team is planning a rolling restart for $n$ database instances. The restart procedure is divided into exactly two phases: Phase 1 and Phase 2. Every instance must be assigned to exactly one of these phases.

To prevent I/O contention from concurrent pre-restart snapshots, any two instances that are co-located on the same underlying block storage cannot be assigned to the same phase. You are provided a list of all co-located instance pairs.

Your task is to find a phase assignment for all $n$ instances that satisfies this isolation requirement, or determine that no such assignment exists. The deployment controller requires a deterministic output: if there are multiple safe assignments, you must supply the one where the sequence of phase choices (represented as 1s and 2s for instances 1 through $n$) is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of database instances and the number of co-located pairs.
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that instances $u$ and $v$ are co-located on the same block storage.

## Output
If no safe phase assignment exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1 \dots s_n$ (each being 1 or 2), representing the lexicographically smallest valid phase assignment.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
