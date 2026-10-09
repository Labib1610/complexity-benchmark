# Problem B — Signal Pipeline Synchronization

Time limit: 1 s   Memory limit: 256 MB

You are configuring a data processing pipeline consisting of $n$ transformation filters. Each filter $i$ processes a dual-channel continuous signal by applying a $2 \times 2$ transformation matrix $M_i$.

You must configure each filter into exactly one of two operational modes:
* **Mode 1**: The filter passes the channels unchanged, applying the identity matrix $M_i = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$.
* **Mode 2**: The filter swaps the two channels, applying the exchange matrix $M_i = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.

The pipeline design includes $m$ synchronization pairs. Each pair specifies two filters $u$ and $v$. To maintain channel balance, any two filters in a synchronization pair must, when applied sequentially, result in a net channel swap. Specifically, their combined transformation must satisfy $M_u M_v = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$. Since these specific matrices commute, the order of application does not matter.

If a filter is not part of any synchronization pair, the condition is vacuously satisfied, but it must still be assigned exactly one mode.

You must determine if there is a valid configuration of modes for all $n$ filters. If there are multiple valid configurations, you must choose the one that yields the lexicographically smallest sequence of modes (where each mode is represented as $1$ or $2$) when listed in order from filter $1$ to filter $n$.

## Input
The first line of the input contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — indicating a synchronization pair between filter $u$ and filter $v$.

## Output
If there is no valid configuration, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers separated by spaces, where the $i$-th integer is the mode ($1$ or $2$) assigned to the $i$-th filter, representing the lexicographically smallest valid assignment.

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