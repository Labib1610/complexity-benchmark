# Problem B — Machine Modes

Time limit: 1 s   Memory limit: 256 MB

A manufacturing process involves $n$ machines. Each machine must be set to either mode 1 or mode 2. There are $m$ interference warnings. Each warning specifies a pair of machines that will fail if they operate in identical modes. 

Determine a mode for each machine so that no warning is triggered, or report if this cannot be done.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of machines in an interference warning.

## Output
If no safe configuration exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \dots s_n$ (each in {1,2}), representing the lexicographically smallest safe configuration.

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
