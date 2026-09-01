# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

A factory employs $n$ workers, with $m$ synchronization links established among them. You must assign a shift code $s_i \in \{1, 2\}$ to each worker $i$. 

To maintain proper timing, the machines of connected workers must resonate at compatible frequencies. A synchronization link between two workers $u$ and $v$ is only stable if their shift codes satisfy the following resonance equation:
$$ 2(s_u^2 + s_v^2) = 5 \cdot s_u \cdot s_v $$

Determine if there is a valid assignment of shift codes for all workers such that every synchronization link in the factory is stable.

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