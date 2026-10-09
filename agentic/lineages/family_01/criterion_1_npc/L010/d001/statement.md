# Problem A — Reactive Samples

Time limit: 2 s   Memory limit: 256 MB

An industrial laboratory needs to store $n$ chemical samples. The facility's maximum capacity is 40 samples, and it will always process at least one. Some pairs of samples are highly reactive and will degrade if placed in the same environment. The number of such reactive pairs $m$ can be zero, or it can be up to every possible pair, $n \cdot (n-1)/2$.

The laboratory provides exactly three distinct storage environments, labeled 1, 2, and 3. Every sample must be placed into exactly one of these three environments. If both samples from a reactive pair are placed in the same environment, safety protocols are violated.

You must determine an environment assignment for all samples that avoids any reactions, or state that no such assignment is possible.

## Input
The first line contains two integers $n$ and $m$ — the number of chemical samples and the number of reactive pairs ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a reactive pair of samples.

## Output
If no safe assignment exists, print a single line NO.
Otherwise print YES on the first line. On the second line print $n$ integers $s_1, s_2, \ldots, s_n$ (each in $\{1, 2, 3\}$), where $s_i$ is the environment of sample $i$. Any safe assignment is accepted.

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