# Problem B — Core Factions

Time limit: 2 s   Memory limit: 256 MB

## Description

You are optimizing the configuration of a network consisting of $n$ nodes and $m$ bidirectional links. The links are arranged such that between any two nodes, there is exactly one non-repeating sequence of links connecting them.

You must assign a state $x_i \in \{0, 1\}$ to each node $i$ (for $1 \le i \le n$). A state of $1$ means the node is active, and $0$ means it is inactive. 
A specific set of $t$ critical nodes must be active; that is, $x_i = 1$ for every critical node $i$.

The *structural index* of a configuration $x$ is defined by the formula:
$$ I(x) = \sum_{i=1}^n x_i - \sum_{j=1}^m x_{u_j} x_{v_j} $$
where $(u_j, v_j)$ are the endpoints of the $j$-th link. A configuration is considered **valid** if and only if its structural index evaluates to exactly $I(x) = 1$.

Each link $j$ has a positive maintenance penalty $w_j$. The *operational cost* of a configuration is the sum of the penalties for the links where both endpoints are active:
$$ C(x) = \sum_{j=1}^m w_j x_{u_j} x_{v_j} $$

Your task is to determine the absolute minimum operational cost $C(x)$ among all valid configurations.

## Input

The first line contains three integers $n$, $m$, and $t$ ($1 \le t \le n$, $1 \le n \le 200000$, $m = n - 1$).
The second line contains $t$ distinct integers: the indices of the critical nodes.
Each of the next $m$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$, $1 \le w \le 1000000$), representing a link connecting node $u$ and node $v$ with a maintenance penalty of $w$.
These $m$ links are guaranteed to form the structure described above (exactly one non-repeating sequence of links connecting any two nodes).

## Output

Print a single integer: the minimum operational cost $C(x)$ of a valid configuration.

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

In Example 1, the critical nodes are 1 and 4, so $x_1 = 1$ and $x_4 = 1$. 
If we only activate these two ($x = [1, 0, 0, 1]$), the structural index is:
$I(x) = (1 + 0 + 0 + 1) - (0 + 0 + 0) = 2$.
Since $I(x) \neq 1$, this configuration is invalid.
If we activate all four nodes ($x = [1, 1, 1, 1]$), the structural index is:
$I(x) = (1 + 1 + 1 + 1) - (1 \cdot 1 + 1 \cdot 1 + 1 \cdot 1) = 4 - 3 = 1$.
This configuration is valid. The operational cost is $C(x) = 5(1) + 1(1) + 2(1) = 8$.

In Example 2, there is only one critical node (3). By setting $x_3 = 1$ and all other $x_i = 0$, we get:
$I(x) = 1 - 0 = 1$.
This configuration is valid, and the operational cost is $C(x) = 0$.

In Example 3, critical nodes 1, 2, and 3 must all be active ($x = [1, 1, 1]$).
$I(x) = (1 + 1 + 1) - (1 \cdot 1 + 1 \cdot 1) = 3 - 2 = 1$.
The operational cost is $C(x) = 4(1) + 5(1) = 9$.