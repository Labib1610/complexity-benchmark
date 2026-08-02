# Tri-Duty Allocation

Time limit: 2 s   Memory limit: 256 MB

A facility operates across three distinct operational time slots, identified by the integers 1, 2, and 3. There are $n$ personnel members, indexed from 1 to $n$. Certain pairs of personnel experience workplace friction and cannot be assigned to the same time slot.

Your task is to assign every personnel member to exactly one time slot (1, 2, or 3) such that no two individuals with workplace friction share the same slot. Among all valid assignments, select the one that yields the lexicographically smallest sequence of time slot choices $s_1, s_2, \dots, s_n$ (comparing $s_1$ first, then $s_2$, and so forth). If no valid assignment exists, report that it is impossible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$) — the number of personnel members and the number of friction pairs, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating a pair of personnel members who cannot share a time slot.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2, 3\}$), where $s_i$ is the time slot assigned to personnel member $i$. Output the lexicographically smallest valid assignment sequence.

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
