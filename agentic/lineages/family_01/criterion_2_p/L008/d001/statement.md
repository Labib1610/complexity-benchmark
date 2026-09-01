# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

There are $n$ workers in a factory, and $m$ synchronization links between them. Each worker must be assigned a shift code, which is either 1 or 2. For every synchronization link between a pair of workers, the sum of their assigned shift codes must be exactly 3. 

Given these conditions, assign each worker a shift code, or report impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of workers connected by a synchronization link.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \ldots s_n$ (each in $\{1,2\}$), the lexicographically smallest valid assignment.

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