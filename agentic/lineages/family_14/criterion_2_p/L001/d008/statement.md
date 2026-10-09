# Problem B — Network Activation

Time limit: 2 s   Memory limit: 256 MB

## Description

You are managing a communication network consisting of $n$ stations and $m$ bidirectional channels. The network is constructed incrementally: starting with a single initial station, each subsequent station was added by connecting it to exactly one previously existing station via a single channel.

You must assign an operational state to each station $i$ (for $1 \le i \le n$): either active ($x_i = 1$) or inactive ($x_i = 0$).
A specific set of $t$ mandatory stations must be active; that is, $x_i = 1$ for every mandatory station $i$.

For any active station $i$, let $k_i$ be the number of its directly connected neighbors that are also active.
The *network balance* of an assignment $x$ is calculated by summing a local score over all active stations:
$$ B(x) = \sum_{i : x_i = 1} (2 - k_i) $$
An assignment is considered **valid** if and only if its network balance evaluates to exactly $B(x) = 2$.

Each channel $j$ has a positive maintenance penalty $w_j$. The *activation cost* of an assignment is the sum of the maintenance penalties for all channels where both endpoint stations are active.

Your task is to determine the absolute minimum activation cost among all valid assignments.

## Input

The first line contains three integers $n$, $m$, and $t$ ($1 \le t \le n$, $1 \le n \le 200000$, $m = n - 1$).
The second line contains $t$ distinct integers: the IDs of the mandatory stations.
Each of the next $m$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$, $1 \le w \le 1000000$), representing a bidirectional channel between station $u$ and station $v$ with a maintenance penalty of $w$.
The channels are guaranteed to form the incrementally constructed structure described above.

## Output

Print a single integer: the minimum activation cost of a valid assignment.

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

In Example 1, the mandatory stations are 1 and 4, so $x_1 = 1$ and $x_4 = 1$. 
If we only activate these two stations ($x = [1, 0, 0, 1]$):
- Station 1 has $k_1 = 0$ active neighbors.
- Station 4 has $k_4 = 0$ active neighbors.
The network balance is $B(x) = (2 - 0) + (2 - 0) = 4$.
Since $B(x) \neq 2$, this assignment is invalid.
If we activate all four stations ($x = [1, 1, 1, 1]$):
- Station 1 has $k_1 = 1$ (station 2).
- Station 2 has $k_2 = 2$ (stations 1 and 3).
- Station 3 has $k_3 = 2$ (stations 2 and 4).
- Station 4 has $k_4 = 1$ (station 3).
The network balance is $B(x) = (2 - 1) + (2 - 2) + (2 - 2) + (2 - 1) = 1 + 0 + 0 + 1 = 2$.
This assignment is valid. The activation cost is $5 + 1 + 2 = 8$.

In Example 2, there is only one mandatory station (3). By activating only station 3 ($x = [0, 0, 1, 0, 0]$):
- Station 3 has $k_3 = 0$ active neighbors.
The network balance is $B(x) = 2 - 0 = 2$.
This assignment is valid, and the activation cost is 0.

In Example 3, mandatory stations 1, 2, and 3 must all be active ($x = [1, 1, 1]$).
- Station 1 has $k_1 = 1$ (station 2).
- Station 2 has $k_2 = 2$ (stations 1 and 3).
- Station 3 has $k_3 = 1$ (station 2).
$B(x) = (2 - 1) + (2 - 2) + (2 - 1) = 1 + 0 + 1 = 2$.
This assignment is valid, and the activation cost is $4 + 5 = 9$.