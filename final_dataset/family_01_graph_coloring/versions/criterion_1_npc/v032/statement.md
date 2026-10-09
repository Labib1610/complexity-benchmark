# Problem A — Bounded Difference System

Time limit: 2 s   Memory limit: 256 MB

You are analyzing a system of $n$ integer variables $x_1, x_2, \dots, x_n$. 
These variables represent configuration parameters for a highly regular production pipeline. Because the pipeline relies on alternating states, the system is designed to be largely two-phase, where most variables can simply oscillate between the values 1 and 2. A third state, 3, is permitted strictly to resolve localized structural anomalies (such as odd-length dependency cycles) that occasionally arise from redundant fail-safes.

Every variable must be assigned an integer value such that $1 \le x_i \le 3$.
You are given $m$ dependency conditions. Each condition specifies two variables $u$ and $v$ that must not hold the same state, which is expressed mathematically as the requirement $|x_u - x_v| \ge 1$.

Determine if there exists an assignment for all $n$ variables that satisfies all $m$ conditions, or report that the system is overconstrained.

## Input
The first line contains two integers $n$ and $m$ — the number of variables and the number of conditions ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that the condition $|x_u - x_v| \ge 1$ must hold. Each unordered pair $\{u, v\}$ appears at most once.

## Output
If no valid assignment exists, print a single line containing NO.
Otherwise, print YES on the first line. On the second line, print $n$ integers $x_1, x_2, \dots, x_n$ (each in $\{1, 2, 3\}$), where $x_i$ is the value assigned to variable $i$. Any valid assignment is accepted.

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
