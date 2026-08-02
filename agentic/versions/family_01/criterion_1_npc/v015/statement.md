# Operational Shift Coordination

**Time limit:** 2 s  
**Memory limit:** 256 MB

A industrial facility operates continuously using three distinct work windows labeled 1, 2, and 3. There are $n$ technicians, numbered 1 through $n$, who must each be assigned to perform their duties in exactly one of these three windows.

Due to safety regulations and spatial restrictions, certain pairs of technicians cannot be present during the same work window. You are given a list of all $m$ incompatible technician pairs.

Determine whether it is possible to assign every technician to a work window such that no two incompatible technicians work during the same window. If a valid assignment exists, find the one that minimizes the resulting sequence of assignments $s_1, s_2, \dots, s_n$ lexicographically (that is, preferring smaller window numbers for technician 1, then technician 2, and so on).

## Input

The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$) — the total number of technicians and the number of incompatible pairs.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that technician $u$ and technician $v$ cannot be assigned to the same work window.

## Output

If no valid assignment exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the work window assigned to technician $i$, such that the sequence $s_1, s_2, \dots, s_n$ is lexicographically as small as possible.

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
