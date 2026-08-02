# Problem A — Roster Distribution

Time limit: 2 s   Memory limit: 256 MB

A facility assigns each of its $n$ personnel members to one of three designated operational slots, numbered 1, 2, and 3. Certain pairs of personnel are incompatible and cannot be assigned to the same operational slot. Determine if every personnel member can be assigned a slot such that no incompatible pair shares a slot. If valid assignments exist, output the one that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$) — the number of personnel members and the number of incompatible pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ — an incompatible pair of personnel.

## Output
If no valid assignment exists, print a single line `NO`.
Otherwise print `YES` on the first line. On the second line print $n$ integers $s_1\ s_2\ \dots\ s_n$ (each in $\{1, 2, 3\}$), where $s_i$ is the slot assigned to personnel member $i$. Among all valid assignments output the lexicographically smallest sequence (compare $s_1$ first, then $s_2$, and so on).

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
