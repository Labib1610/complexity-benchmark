# Problem A — Production Cycle Allocation

Time limit: 2 s   Memory limit: 256 MB

The factory operates continuously, dividing its workforce of $n$ personnel across 3 daily production cycles (labeled 1, 2, and 3). Having three distinct cycles provides significant scheduling flexibility—far more than a standard day-night rotation.

A preliminary collision detection system has already analyzed the localized work zones on the factory floor. It has identified $m$ pairs of personnel who require the same specialized machinery simultaneously. To maintain safety, these flagged pairs cannot be scheduled in the same cycle.

Many scheduling conflicts can be resolved by simply alternating workers between cycle 1 and cycle 2. The addition of cycle 3 is intended to provide a fallback to easily resolve any remaining overlaps. Your program must read the list of $m$ collisions and assign each worker a cycle $c_i \in \{1, 2, 3\}$ such that for every collision between worker $u$ and worker $v$, $c_u \neq c_v$.

You must evaluate whether the three available cycles provide enough flexibility to safely separate all colliding pairs. If a valid allocation exists, you must output it.

## Input
The first line contains two integers $n$ and $m$ — the number of personnel and the number of operational collisions ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the following $m$ lines contains two integers $u$ and $v$ — a pair of personnel with an operational collision.

## Output
If no valid allocation exists even with all three cycles, print a single line `NO`.
Otherwise print `YES` on the first line. On the second line print $n$ integers $c_1, c_2, \dots, c_n$ (each in $\{1, 2, 3\}$), where $c_i$ is the cycle assigned to person $i$. Any valid allocation is accepted.

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
