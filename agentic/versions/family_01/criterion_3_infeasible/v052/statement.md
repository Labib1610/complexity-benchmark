# Problem C — Layer Assignment Violation

Time limit: 2 s
Memory limit: 256 MB

A printed circuit board (PCB) is being designed with exactly two copper layers. The board layout contains several signal traces. Because of the geometry of the design, certain pairs of traces cross each other. To avoid electrical shorts, any two traces that cross must be assigned to different layers.

The automated routing software has determined that a valid two-layer assignment is impossible for the given layout. Your task is to extract a minimal proof of this failure to show the hardware engineer.

Specifically, the layout is guaranteed to contain a group of exactly three traces that all mutually cross one another. Within this trio, each trace intersects with both of the other two. Because there are only two layers available, it is physically impossible to isolate all three traces from each other. 

You must identify such a trio of traces.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2\cdot 10^5)$), the number of signal traces and the number of crossing pairs, respectively. Traces are identified by integers from $1$ to $n$.

Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that trace $u$ and trace $v$ cross each other. No crossing pair is listed more than once.

It is guaranteed that at least one such trio of mutually crossing traces exists in the input.

## Output
Output a single line containing three integers $a$, $b$, and $c$, representing the identifiers of the three traces in the trio, sorted in ascending order ($a < b < c$).

If multiple such trios exist, output the one that is lexicographically smallest. This means you should first minimize $a$; if there is a tie, minimize $b$; and if still tied, minimize $c$.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
