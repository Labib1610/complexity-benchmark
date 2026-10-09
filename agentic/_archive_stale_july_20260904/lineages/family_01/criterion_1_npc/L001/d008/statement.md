# Problem A — Orbital Network Frequency Coordination

Time limit: 2 s   Memory limit: 256 MB

A telecommunications agency is configuring a network of $n$ satellite transmitters, numbered $1$ through $n$. Each transmitter must be assigned an operating band from the set $\{1, 2, 3\}$.

Geospatial analysis has identified $m$ pairs of transmitters with overlapping coverage areas. To prevent signal collision, any two transmitters in a listed pair must be assigned different operating bands.

A configuration is a sequence of $n$ band assignments, where the $i$-th value is the band assigned to transmitter $i$. The agency will only consider configurations that are completely free of signal collisions. If no such configuration exists, the setup is aborted.

If valid configurations do exist, the agency must deploy the single configuration that minimizes the network's total interference metric. 

The interference metric $M$ for a configuration is evaluated by simulating a noise cascade across the network. The agency uses $n$ noise accumulators, $A_1, A_2, \dots, A_n$, corresponding to the $n$ transmitters. The simulation proceeds as follows:

1. Initially, each accumulator $A_j$ is set to the band assigned to transmitter $j$ (so $A_j = b_j$).
2. The cascade occurs in $n-1$ sequential steps. For each step $k$ from $1$ to $n-1$:
   The current noise in accumulator $A_k$ propagates to all subsequent accumulators. Specifically, for every $j$ strictly greater than $k$, the value of $A_j$ is increased by $3 \times A_k$.
3. After all $n-1$ steps are completed, the final interference metric $M$ is the sum of all $n$ accumulators ($M = A_1 + A_2 + \dots + A_n$).

## Input
The first line contains two integers $n$ and $m$ — the number of satellite transmitters and the number of overlapping coverage pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — representing a pair of transmitters that have overlapping coverage and must use different bands.

## Output
If no collision-free configuration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $b_1, b_2, \dots, b_n$ (where each $b_i \in \{1, 2, 3\}$), representing the band allocated to transmitter $i$. Output the configuration that minimizes the total interference metric.

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