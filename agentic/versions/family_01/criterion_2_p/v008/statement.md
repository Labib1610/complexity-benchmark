# Phase 2: Shift Assignment

Time limit: 1 s   Memory limit: 256 MB

As part of the workforce optimization pipeline, employee scheduling is executed across three distinct phases: Phase 1 (Conflict Extraction), Phase 2 (Shift Assignment), and Phase 3 (Schedule Publishing).

You are tasked with implementing Phase 2. Given $n$ workers and $m$ conflict pairs identified during Phase 1, each worker must be assigned to either shift 1 or shift 2 such that no two conflicting workers share the same shift. If multiple valid assignments are possible, select the lexicographically smallest assignment (when comparing the sequence $s_1, s_2, \dots, s_n$). If no valid shift assignment can satisfy all conflict constraints, Phase 2 fails and no roster can be generated.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$) representing a conflicting pair of workers.

## Output
If no valid assignment exists, print a single line `NO`.
Otherwise, print `YES` on the first line, and on the second line print $n$ integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2\}$), the lexicographically smallest valid assignment.

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
