# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

A factory employs $n$ workers, with $m$ synchronization links established among them. You must assign a shift code $s_i \in \{1, 2\}$ to each worker $i$. 

To maintain proper timing, the machines operated by any two workers $u$ and $v$ connected by a synchronization link must emit a joint frequency pulse. The frequency of this pulse is defined by concatenating their shift codes to form a two-digit integer ($10 s_u + s_v$). The link is only stable if this joint frequency is exactly divisible by 3.

Determine if there is a valid assignment of shift codes for all workers.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of workers connected by a synchronization link.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \ldots s_n$ (each in $\{1,2\}$), representing the lexicographically smallest valid assignment.

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