# Operational Workflow Optimization: Shift Distribution Stage

Time limit: 2 s   Memory limit: 256 MB

In a multi-stage operational management workflow, an enterprise pipeline processes data through three sequential phases: Data Ingestion, Shift Distribution, and Resource Audit. You are tasked with implementing the computational module for Phase 2 (Shift Distribution).

In Phase 2, the system receives $n$ personnel IDs, numbered $1$ through $n$, along with $m$ conflict rules specifying pairs of personnel who cannot be active during the same operational period. The facility operates three distinct operational periods per cycle, represented by the integer tags $1$, $2$, and $3$.

Your task is to assign each personnel member $i$ ($1 \le i \le n$) an operational period tag $s_i \in \{1, 2, 3\}$ such that no two personnel bound by a conflict rule share the same tag. To prepare the output for the deterministic verification algorithm in Phase 3 (Resource Audit), if several valid tag assignments exist, you must output the assignment that yields the lexicographically smallest sequence $(s_1, s_2, \dots, s_n)$. If no valid tag assignment satisfies all conflict rules, report that the workflow cannot proceed.

## Input
The first line contains two space-separated integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$), representing the number of personnel members and the number of conflict rules, respectively.
The following $m$ lines each contain two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that personnel $u$ and personnel $v$ share a conflict rule and cannot receive the same operational period tag.

## Output
If no valid tag assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2, 3\}$), representing the assigned operational period tag for each personnel member from $1$ to $n$. Output the lexicographically smallest sequence among all valid assignments.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
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
NO
```
