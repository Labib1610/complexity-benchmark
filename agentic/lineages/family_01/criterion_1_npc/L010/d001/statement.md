# Sequential Execution Tier Assignment

Time limit: 2 s   Memory limit: 256 MB

A facility manages $n$ tasks, indexed sequentially from 1 to $n$. Each task must be allocated to one of three available operational tiers, labeled 1, 2, and 3. There are $m$ pairwise interference rules between specific tasks. An interference rule between task $u$ and task $v$ means that task $u$ and task $v$ contend for exclusive system resources and cannot be allocated to the same operational tier.

Find an allocation of operational tiers for all $n$ tasks that satisfies every interference rule. Among all valid allocations, choose the one that yields the lexicographically smallest sequence of tier numbers $s_1, s_2, \dots, s_n$ (i.e., prioritizing smaller tier numbers for lower task indices). If no valid allocation exists, report that it is impossible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$) — the number of tasks and the number of interference rules.
Each of the next $m$ lines contains two integers $u$ $v$ ($1 \le u, v \le n$, $u \ne v$), specifying an interference rule between task $u$ and task $v$.

## Output
If no valid allocation exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line print $n$ integers $s_1, s_2, \dots, s_n$ (each in \{1, 2, 3\}), where $s_i$ denotes the operational tier assigned to task $i$. Output the lexicographically smallest sequence among all valid allocations.

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