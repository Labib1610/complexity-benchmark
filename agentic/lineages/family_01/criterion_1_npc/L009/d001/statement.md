# Operational Window Partitioning

Time limit: 2 s   Memory limit: 256 MB

A facility operates across three distinct time slots labeled 1, 2, and 3. There are $n$ personnel, numbered 1 through $n$. The facility maintains $m$ shift collision rules. Each rule specifies two distinct personnel who are forbidden from working during the same time slot.

Your task is to assign every person to exactly one time slot such that all shift collision rules are respected, or report that no valid schedule exists.

## Input
The first line contains two integers $n$ and $m$ — the number of personnel and the number of shift collision rules ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that person $u$ and person $v$ cannot share a time slot.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line.
On the second line, print $n$ integers $s_1\ s_2\ \dots\ s_n$ (where each $s_i \in \{1, 2, 3\}$), where $s_i$ is the time slot assigned to person $i$.
Among all valid assignments, output the lexicographically smallest sequence (comparing $s_1$ first, then $s_2$, and so on).

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