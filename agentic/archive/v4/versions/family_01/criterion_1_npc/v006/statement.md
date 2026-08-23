# Problem A — Division Assignment

Time limit: 2 s   Memory limit: 256 MB

A research institute must assign $n$ researchers to 3 distinct divisions labeled 1, 2, and 3. Due to overlapping equipment requirements, certain pairs of researchers cannot be placed in the same division. Assign every researcher to exactly one division so that no restricted pair shares a division, or determine that it is impossible.

## Input
The first line contains two integers $n$ and $m$ — the number of researchers and the number of restricted pairs ($1 \le n \le 40$, $0 \le m \le n \cdot (n - 1) / 2$).
Each of the next $m$ lines contains two integers $u$ $v$ — a restricted pair of researchers.

## Output
If no valid assignment exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1 \ s_2 \ \dots \ s_n$ (each in \{1, 2, 3\}), where $s_i$ is the division assigned to researcher $i$. Among all valid assignments, output the lexicographically smallest sequence (comparing $s_1$ first, then $s_2$, and so on).

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
