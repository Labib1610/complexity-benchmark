# Sequence Configuration

Time limit: 2 s   Memory limit: 256 MB

You are tasked with generating an integer sequence $C$ of length $n$. Each element in the sequence must be chosen from the set $\{1, 2, 3\}$.

The sequence must satisfy $m$ conditions. Each condition is defined by a pair of 1-based indices $u$ and $v$. For the sequence to be valid under a given condition, the quadratic equation 
$z^2 - (C[u] + C[v])z + C[u]C[v] = 0$
must have exactly two distinct real roots.

Your objective is to determine if at least one such sequence $C$ can be constructed that satisfies all $m$ conditions simultaneously.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$). 
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating a condition applied to the elements at index $u$ and index $v$. 

## Output
If no such sequence can be constructed, output `NO` on a single line.
If a valid sequence exists, output `YES` on the first line. On the second line, output $n$ integers representing the valid sequence $C[1], C[2], \dots, C[n]$. If there are multiple valid sequences, any of them will be accepted.

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