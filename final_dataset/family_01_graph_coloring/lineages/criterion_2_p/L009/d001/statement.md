# Problem B — Factory Tuning

Time limit: 1 s   Memory limit: 256 MB

The factory requires each of its $n$ machines to be set to a power mode, which can be either 1 or 2. With $n$ machines, there are $2^n$ possible mode configurations to consider. Given $m$ interference links, search this space to assign each machine a power mode such that for every linked pair of machines, the bitwise XOR of their power modes evaluates to exactly 3. If no valid assignment exists in the configuration space, report impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a linked pair of machines.

## Output
If no valid assignment exists in the configuration space, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \dots s_n$ (each in $\{1,2\}$), representing the lexicographically smallest valid assignment.

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