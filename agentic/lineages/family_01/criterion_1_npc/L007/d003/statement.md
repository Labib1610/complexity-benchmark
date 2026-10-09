# Problem A — Trichrome Shifts

Time limit: 2 s   Memory limit: 256 MB

A manufacturing facility operates continuously across three distinct shifts, designated as 1, 2, and 3. The facility employs $n$ personnel.

Certain pairs of personnel have operational conflicts and cannot work at the same time. You are provided with $m$ conflict pairs, each specifying two individuals $u$ and $v$. 

To prevent critical workflow failures, the shift scheduling must ensure that for every recorded conflict pair $(u, v)$, the two individuals are assigned to strictly different shifts.

Your task is to allocate each person to exactly one of the three shifts such that every conflict pair satisfies this safety condition, or to determine that no such allocation exists.

## Input
The first line provides two integers $n$ and $m$ — the total number of personnel and the number of conflict pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the subsequent $m$ lines provides two integers $u$ and $v$, representing a pair of personnel who must be assigned to different shifts.

## Output
If there is no valid shift allocation, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2, 3\}$), with $s_i$ representing the shift assigned to person $i$. Any valid allocation is accepted.

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