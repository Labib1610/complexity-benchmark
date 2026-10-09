# Problem B — Core Factions

Time limit: 2 s   Memory limit: 256 MB

## Description

You are configuring a system of $n$ modules (indexed 1 to $n$) and $m$ bidirectional channels. The channels are structured such that between any two modules, there is exactly one non-repeating sequence of channels linking them.

You must choose a configuration vector $X \in \{0, 1\}^n$, where $X_i$ represents the state of module $i$. A specific set of $t$ primary modules must be activated, meaning you must set $X_c = 1$ for every primary module $c$.

Let $A$ be an $n \times n$ symmetric matrix where $A_{u,v} = 1$ if there is a channel connecting module $u$ and module $v$, and $A_{u,v} = 0$ otherwise. 
Your configuration vector $X$ must satisfy the following algebraic condition:
$$ X^T A X = 2 X^T X - 2 $$
where $X^T$ is the transpose of $X$.

Each channel between a pair of modules has a specific positive maintenance penalty $w$. A channel connecting module $u$ and module $v$ is considered energized if and only if both modules are activated ($X_u = 1$ and $X_v = 1$). For every energized channel, you must pay its maintenance penalty exactly once. Channels that are not energized incur no penalty.

You must determine the absolute minimum total maintenance penalty required to yield a valid configuration vector $X$.

## Input

The first line contains three integers $n$, $m$, and $t$ ($1 \le t \le n$, $1 \le n \le 200000$, $m = n - 1$).
The second line contains $t$ distinct integers: the indices of the primary modules.
Each of the next $m$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$, $1 \le w \le 1000000$), representing a channel connecting module $u$ and module $v$ with a maintenance penalty of $w$.
These $m$ channels are guaranteed to form the structure described above (exactly one non-repeating sequence of channels linking any two modules).

## Output

Print a single integer: the minimum total maintenance penalty required for a valid configuration.

## Examples

### Example 1

**Input**
```
4 3 2
1 4
1 2 5
2 3 1
3 4 2
```

**Output**
```
8
```

### Example 2

**Input**
```
5 4 1
3
1 2 4
2 3 6
3 4 2
4 5 9
```

**Output**
```
0
```

### Example 3

**Input**
```
3 2 3
1 2 3
1 2 4
2 3 5
```

**Output**
```
9
```

## Note

In Example 1, the primary modules are 1 and 4, so $X_1 = 1$ and $X_4 = 1$. If we only assign 1 to these two, we have $X^T X = 2$. Since $A_{1,4} = 0$, there are no energized channels and $X^T A X = 0$. This violates the condition $0 = 2(2) - 2$. To satisfy the equation, we must also set $X_2 = 1$ and $X_3 = 1$. This yields $X^T X = 4$. The channels (1,2), (2,3), and (3,4) are energized, giving $X^T A X = 2(1) + 2(1) + 2(1) = 6$. Since $6 = 2(4) - 2$, the configuration is valid. The total penalty is 5 + 1 + 2 = 8.

In Example 2, there is only one primary module ($X_3 = 1$). By setting all other components of $X$ to 0, we have $X^T X = 1$ and $X^T A X = 0$. The equation $0 = 2(1) - 2$ is satisfied. The minimum total penalty is 0.

In Example 3, primary modules 1, 2, and 3 must all be assigned 1. Thus $X^T X = 3$. The channels (1,2) and (2,3) are energized, yielding $X^T A X = 4$. The equation $4 = 2(3) - 2$ is satisfied. The total penalty is 4 + 5 = 9.