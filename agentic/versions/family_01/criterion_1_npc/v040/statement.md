# Operational Phase Assignment Protocol

Time limit: 2 s   Memory limit: 256 MB

As part of an automated workforce deployment pipeline, a site coordinator must execute a duty assignment stage for $n$ registered operators. There are three designated operational time windows, identified by integer codes 1, 2, and 3. Each operator must be assigned to exactly one of these three windows.

A automated compliance audit has generated $m$ incompatibility rules between pairs of operators. Each rule specifies two operators who are prohibited from working within the same time window.

Determine whether a valid schedule exists that assigns every operator $i$ ($1 \le i \le n$) a time window $s_i \in \{1, 2, 3\}$ without violating any incompatibility rule. If valid assignments exist, output the lexicographically smallest sequence $s_1, s_2, \dots, s_n$ (comparing $s_1$ first, then $s_2$, and so forth). Otherwise, report that no valid configuration exists.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$) — the number of operators and the number of incompatibility rules.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that operator $u$ and operator $v$ cannot share the same operational time window.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2, 3\}$), representing the assigned time window for each operator $1$ through $n$. If multiple valid schedules exist, output the lexicographically smallest one.

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
