# Facility Operations Workflow: Operational Slot Allocation

Time limit: 2 s   Memory limit: 256 MB

In the facility's quarterly planning pipeline, the automated scheduler processes operational data across three sequential stages: audit, allocation, and dispatch. The preliminary audit stage has generated a database of $n$ active personnel (indexed from $1$ to $n$) along with $m$ identified pairwise incompatibility restrictions between certain workers.

In the current allocation stage, every individual worker must be assigned to exactly one of three active work shifts, designated as $1$, $2$, and $3$. To prevent operational disruption, any two personnel who share an incompatibility restriction cannot be assigned to the same shift.

To ensure consistency before passing the layout to the final dispatch stage, if multiple valid shift assignments exist for the workforce, the system must select the configuration that is lexicographically smallest when represented as a sequence of assigned shift labels $(s_1, s_2, \dots, s_n)$. If no assignment exists that respects all incompatibility restrictions, the process halts.

## Input
The first line contains two integers $n$ and $m$ — the number of personnel and the number of pairwise incompatibility restrictions ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that worker $u$ and worker $v$ are incompatible.

## Output
If no valid assignment satisfying all incompatibility constraints exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1\ s_2\ \dots\ s_n$ where $s_i \in \{1, 2, 3\}$ denotes the shift assigned to worker $i$. If multiple valid sequences exist, output the lexicographically smallest sequence (comparing $s_1$ first, then $s_2$, and so on).

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
