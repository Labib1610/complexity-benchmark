# Problem A — Factory Rotation Assignments

Time limit: 2 s
Memory limit: 256 MB

A manufacturing plant operates around the clock using three distinct daily rotations, designated as rotation 1, rotation 2, and rotation 3. The plant employs $n$ technicians. Due to past interpersonal disputes, certain pairs of technicians are deemed incompatible and cannot be assigned to the same rotation.

You must allocate each of the $n$ technicians to exactly one of the three rotations such that no two incompatible technicians share a rotation. If there is no way to achieve this, you must determine that it is impossible.

To comply with the plant's organizational invariants, the input data is guaranteed to satisfy the following structural properties:
* No single technician is incompatible with 40 or more distinct colleagues.
* There is no subset of 41 or more technicians who are all mutually incompatible with one another.

## Input
The first line provides $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$) — the number of technicians and the number of incompatible pairs.
Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a pair of technicians who cannot share a rotation. It is guaranteed that each unordered pair is listed at most once.

## Output
If a valid allocation cannot be formed, output NO on a single line.
Otherwise, output YES on the first line. On the second line, output $n$ integers $s_1, s_2, \ldots, s_n$ separated by spaces, where $s_i \in \{1, 2, 3\}$ is the rotation assigned to technician $i$. Any allocation that satisfies all requirements is acceptable.

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
