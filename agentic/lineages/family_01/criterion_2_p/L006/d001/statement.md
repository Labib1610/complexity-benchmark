# Problem B — System Equilibrium

Time limit: 1 s   Memory limit: 256 MB

A facility configures $n$ automated valves, numbered 1 to $n$. Each valve must be assigned an operational state of either 1 or 2.

The facility relies on $m$ pressure monitors. Each monitor evaluates a specific pair of valves. To maintain equilibrium, every monitor requires that exactly one of the two valves it evaluates is set to state 1. Because the only available states are 1 and 2, this strictly dictates that the other valve in the evaluated pair must be set to state 2.

Determine if there is a valid arrangement of states for all $n$ valves. If multiple valid arrangements exist, you must find the one that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the indices of the two valves evaluated by a monitor.

## Output
If no valid arrangement exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \dots s_n$ (each in {1,2}), representing the lexicographically smallest valid arrangement.

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