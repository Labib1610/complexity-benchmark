# Production Line Diagnostics

Time limit: 2 s   Memory limit: 256 MB

A manufacturing facility operates continuously. Certain pairs of manufacturing steps require a shared specialized calibration tool. 

Your diagnostic software must isolate a root cause of an allocation failure by identifying a group of exactly three steps that form an unresolvable bottleneck. 

Consider any group of exactly three distinct steps. Imagine assigning each of these three steps a configuration setting chosen from the values 1, 2, or 3. There are exactly $3^3 = 27$ possible configuration states for the group.

For any given state, we define its *tension* as the sum of the absolute differences in configuration settings across all shared calibration tool requirements strictly within the group. That is, for every pair of steps in the group that requires a shared calibration tool, compute the absolute difference between their assigned configuration settings, and sum these differences together. 

A configuration state is classified as *relaxed* if its tension is exactly 2. 

A group of three distinct steps is classified as an unresolvable bottleneck if exactly 12 out of its 27 possible configuration states are relaxed.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the total number of manufacturing steps and the number of tool collision pairs. Steps are numbered from $1$ to $n$.

Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that step $u$ and step $v$ require a shared calibration tool.

It is guaranteed that at least one unresolvable bottleneck exists in the provided data.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, with $a < b < c$, representing the identifiers of the three steps. Output the combination that is sequentially lowest (the smallest possible value for $a$; in case of a tie, the smallest possible value for $b$; and finally the smallest possible value for $c$).

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