# Problem C — Registry Resonance

Time limit: 2 s
Memory limit: 256 MB

You are analyzing a system of $n$ independent memory registries, numbered $1$ to $n$.
The system receives a sequence of $m$ synchronization pulses. Each pulse is assigned a sequential index $k$ from $1$ to $m$ in the order it is received.

Each registry $i$ maintains a state vector $V_i$ of length $m$. Initially, all elements of every vector are set to $0$.

The $k$-th pulse is defined by a pair of registry IDs $(u, v)$. Upon receiving this pulse, registry $u$ sets the $k$-th element of its vector to $1$ ($V_u[k] = 1$), and registry $v$ sets the $k$-th element of its vector to $1$ ($V_v[k] = 1$). All other elements of their vectors remain unchanged.

Let $V_a \cdot V_b$ denote the standard dot product of two state vectors, defined as $\sum_{k=1}^m V_a[k] \times V_b[k]$.

A critical resonance anomaly occurs if there exist three registry IDs $x_1, x_2$, and $x_3$ strictly increasing in value ($x_1 < x_2 < x_3$) such that:
$$ (V_{x_1} \cdot V_{x_2}) \cdot (V_{x_1} \cdot V_{x_3}) \cdot (V_{x_2} \cdot V_{x_3}) > 0 $$

You must find the IDs involved in this anomaly. It is guaranteed that the sequence of pulses produces at least one such configuration.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 200000)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the two registries involved in the $k$-th synchronization pulse. The first of these lines corresponds to $k=1$, the next to $k=2$, and so on.
It is guaranteed that at least one resonance anomaly exists.

## Output
Print three integers $x_1$, $x_2$, and $x_3$ on one line with $x_1 < x_2 < x_3$. Output the lexicographically smallest such combination (smallest $x_1$; ties broken by smallest $x_2$; then smallest $x_3$).

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