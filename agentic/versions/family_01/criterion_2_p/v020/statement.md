# Problem B — Laser Grid Polarization

Time limit: 1 s   Memory limit: 256 MB

You are designing a security system composed of $n$ laser emitters, numbered 1 through $n$. Each emitter must be fitted with exactly one of two types of polarization filters: type 1 or type 2.

The physical layout of the facility causes the beams from certain emitters to intersect. There are $m$ such intersection points. At each intersection point, the beams from two specific emitters cross paths. If both intersecting beams have the exact same polarization type, they will cause destructive interference and trigger a false alarm. To prevent this, any two emitters whose beams cross must be equipped with different types of polarization filters.

Your task is to determine if it is possible to assign a polarization filter to every emitter such that no false alarms are triggered. If it is possible, you must output a valid assignment. Due to inventory preferences, if there are multiple valid assignments, you must provide the lexicographically smallest one (i.e., assignment $A$ is lexicographically smaller than assignment $B$ if, at the first emitter $i$ where their filter types differ, assignment $A$ uses type 1 and assignment $B$ uses type 2).

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that the beams from emitter $u$ and emitter $v$ intersect.

## Output
If there is no way to assign the filters without causing interference, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $f_1, f_2, \ldots, f_n$ (where each $f_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment of filters to the $n$ emitters.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
