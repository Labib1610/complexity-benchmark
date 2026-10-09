# Problem B — Harmonic Resonance

Time limit: 1 s   Memory limit: 256 MB

A facility operates $n$ resonance generators. There are $m$ interference testing links, each connecting a specific pair of generators. You must configure the facility by assigning each generator $i$ a state $s_i \in \{1, 2\}$. 

Depending on its assigned state, a generator emits a complex phase signature:
- State 1 emits $c_1 = 1 + i$
- State 2 emits $c_2 = 1 - i$

(Here, $i$ represents the imaginary unit, where $i^2 = -1$.)

For any configuration, the system's overall reactive footprint is determined by the following procedure: for each of the $m$ linked pairs, compute the mathematical product of their two complex phase signatures, and extract the imaginary part of this product (for a complex number $a + bi$, the imaginary part is the real number $b$). The overall footprint is the sum of the squares of these $m$ imaginary parts. (If $m=0$, the footprint is exactly $0$).

To ensure system stability, a configuration is only valid if its overall reactive footprint is exactly $0$.

Determine if there is a valid configuration for all $n$ generators.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of generators connected by an interference testing link.

## Output
If no valid configuration exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \ldots, s_n$ (each in $\{1,2\}$) representing the valid configuration. If there are multiple valid configurations, output the one that minimizes the state $s_1$. If there is still a tie, minimize $s_2$, and so on sequentially up to $s_n$.

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