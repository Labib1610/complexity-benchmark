# Problem B — Network Configurations

Time limit: 1 s
Memory limit: 256 MB

A communication grid consists of $n$ radio towers. You need to assign each tower $i$ a configuration value $f_i$, which must be chosen from the set $\{1, 2\}$. 

There are $m$ critical links between specific pairs of towers. To prevent signal degradation, the two towers connected by any critical link must satisfy the Signal Interleaving stability predicate.

When a critical link is active, both towers continuously transmit a repeating two-step signal pattern determined by their configuration:
- A tower assigned configuration 1 transmits a 'high' signal in step one and a 'low' signal in step two.
- A tower assigned configuration 2 transmits a 'low' signal in step one and a 'high' signal in step two.

The link is stable if and only if the signals from the two connected towers perfectly interleave: at each step, exactly one tower must transmit a 'high' signal while the other transmits a 'low' signal. If both transmit the same signal type simultaneously, a collision or silence occurs and the link fails.

Determine if a valid assignment exists for all towers such that all critical links are stable. If no such assignment is possible, report impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of towers connected by a critical link.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $f_1 \dots f_n$ (each in $\{1,2\}$), representing the lexicographically smallest valid assignment.

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