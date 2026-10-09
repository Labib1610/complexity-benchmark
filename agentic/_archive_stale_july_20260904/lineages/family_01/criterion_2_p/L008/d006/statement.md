# Problem B — Harmonic Resonance

Time limit: 1 s   Memory limit: 256 MB

A factory employs $n$ workers, with $m$ synchronization links established among them. You must assign a shift code $s_i \in \{1, 2\}$ to each worker $i$. 

To maintain proper timing, the machines of connected workers must resonate at compatible frequencies. We define two resonance matrices:
$$A_1 = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \quad \text{and} \quad A_2 = \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix}$$

A synchronization link between two workers $u$ and $v$ is stable if and only if the trace of the matrix product $A_{s_u} A_{s_v}$ is exactly $6$. 

Additionally, to prevent harmonic buildup, any valid assignment must ensure that in every simple cycle within the factory's synchronization network, the number of workers assigned shift code 1 is exactly equal to the number of workers assigned shift code 2.

Determine if there is a valid assignment of shift codes for all workers such that every synchronization link is stable and the harmonic buildup condition is satisfied.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of workers connected by a synchronization link.

## Output
If no valid assignment exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \ldots, s_n$ (each in $\{1,2\}$) representing the valid assignment. If there are multiple valid assignments, output the one that minimizes the structural weight of the sequence, defined as $\sum_{i=1}^n s_i \cdot 3^{n-i}$. Print this assignment as a full sequence of $n$ integers.

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