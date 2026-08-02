# Problem A — Operational Shift Distribution

Time limit: 2 s   Memory limit: 256 MB

A facility operates across three distinct operational shifts labeled 1, 2, and 3. There are $n$ members, indexed from 1 to $n$. A list of conflict restrictions is given; two members listed together in a conflict pair cannot be scheduled during the same shift.

Every member must be assigned to exactly one shift. If no valid placement exists that satisfies all conflict restrictions, output `NO`. Otherwise, output `YES` and specify the valid assignment that produces the lexicographically smallest sequence of shift choices $s_1, s_2, \dots, s_n$ (comparing $s_1$ first, then $s_2$, and so on).

## Input
The first line contains two integers $n$ and $m$ — the number of members and the number of conflict pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a conflict pair between member $u$ and member $v$.

## Output
If no valid shift distribution exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line.
On the second line, print $n$ space-separated integers $s_1\ s_2\ \dots\ s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the shift assigned to member $i$ in the lexicographically smallest valid assignment.

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
