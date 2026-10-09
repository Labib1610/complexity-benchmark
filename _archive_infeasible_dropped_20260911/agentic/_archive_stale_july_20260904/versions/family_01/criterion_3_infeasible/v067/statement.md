# Problem C — Warranty Claim

Time limit: 2 s
Memory limit: 256 MB

A facility's perimeter is monitored by $n$ security cameras. Because of power grid limitations, certain pairs of cameras are connected by power-sharing cables. When two cameras are connected by a cable, they cannot draw power simultaneously, meaning they must operate on alternating power shifts.

The facility manager discovered that the current wiring layout prevents a valid two-shift configuration. To file a warranty claim, the manager must identify a specific wiring defect: a set of three distinct cameras that are mutually connected to each other. Specifically, the first camera is wired to the second, the second is wired to the third, and the third is wired to the first. Because there are only two power shifts available, this arrangement makes a safe power schedule impossible. 

It is guaranteed that the provided wiring layout contains at least one such defect. Your task is to find and report one.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of cameras and the number of power-sharing cables, respectively. Cameras are numbered from $1$ to $n$.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that camera $u$ and camera $v$ are connected by a cable. Cables operate in both directions. It is guaranteed that no pair of cameras is listed more than once, and that at least one wiring defect of three mutually connected cameras exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, representing the identifiers of the three cameras that form the wiring defect. 

The identifiers must be printed in ascending order ($a < b < c$). If there are multiple valid sets of three cameras, you must output the one that is lexicographically smallest. This means you should first minimize $a$; if there are ties, minimize $b$ among those ties; and if there are still ties, minimize $c$.

## Example 1
**Input:**
```
4 5
1 2
1 3
2 3
2 4
3 4
```
**Output:**
```
1 2 3
```

## Example 2
**Input:**
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
**Output:**
```
1 2 4
```
