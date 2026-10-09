# Problem B — Factory Tuning

Time limit: 1 s   Memory limit: 256 MB

The factory requires each of its $n$ machines to be set to a power mode of either 1 or 2. There are $m$ interference links between specific pairs of machines. 

The factory calculates a link stress for each of the $m$ interference links. For a link between a machine with mode $x$ and a machine with mode $y$, the link stress is defined as the integer $x^2 + y^2$.

The factory's overall stability score is the mathematical product of the link stresses across all $m$ links. A legacy controller accepts the configuration if and only if this overall stability score is exactly equal to $5^m$. (If $m=0$, the score is $1 = 5^0$, which is accepted).

You must assign a power mode to every machine such that the configuration is accepted by the controller.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a linked pair of machines.

## Output
If no valid assignment of modes exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \dots s_n$ (each in $\{1,2\}$), representing the lexicographically smallest valid assignment. (An assignment $s$ is lexicographically smaller than $t$ if at the first index $i$ where they differ, $s_i < t_i$.)

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