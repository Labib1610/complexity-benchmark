# Problem B — Core Factions

Time limit: 2 s   Memory limit: 256 MB

## Description

You are configuring a system of $n$ modules (indexed 1 to $n$) and $m$ bidirectional channels. The channels are structured such that between any two modules, there is exactly one non-repeating sequence of channels linking them.

You must choose a subset of modules to activate. A specific set of $t$ primary modules is mandatory and must be included in your activated subset.

For any activated module $u$, let $c(u)$ be the number of channels that directly connect $u$ to another activated module. The *local stability* of an activated module $u$ is defined as $2 - c(u)$. 
Your chosen subset of activated modules is considered valid if and only if the sum of the local stabilities of all activated modules is exactly 2.

Each channel has a specific positive maintenance penalty $w$. A channel is considered *energized* if and only if both of its endpoint modules are activated. For every energized channel, its maintenance penalty is added to the total cost of the configuration. Channels that are not energized incur no cost.

You must determine the absolute minimum total cost required to yield a valid configuration of activated modules.

## Input

The first line contains three integers $n$, $m$, and $t$ ($1 \le t \le n$, $1 \le n \le 200000$, $m = n - 1$).
The second line contains $t$ distinct integers: the indices of the primary modules.
Each of the next $m$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$, $1 \le w \le 1000000$), representing a channel connecting module $u$ and module $v$ with a maintenance penalty of $w$.
These $m$ channels are guaranteed to form the structure described above (exactly one non-repeating sequence of channels linking any two modules).

## Output

Print a single integer: the minimum total cost required for a valid configuration.

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

In Example 1, the primary modules are 1 and 4, so they must be activated. If we only activate these two, $c(1) = 0$ and $c(4) = 0$, giving each a local stability of $2 - 0 = 2$. The sum of stabilities is 4, which is not equal to 2, so this configuration is invalid. If we activate modules 1, 2, 3, and 4, the connections between activated modules are (1,2), (2,3), and (3,4). The values of $c(u)$ are $c(1)=1$, $c(2)=2$, $c(3)=2$, and $c(4)=1$. The local stabilities are $1, 0, 0, 1$, which sum to exactly 2. The channels (1,2), (2,3), and (3,4) are energized, giving a total cost of 5 + 1 + 2 = 8.

In Example 2, there is only one primary module (3). By activating only module 3, $c(3) = 0$, and its local stability is 2. The sum of stabilities is 2, satisfying the condition. No channels are energized, so the minimum total penalty is 0.

In Example 3, primary modules 1, 2, and 3 must all be activated. The connections between them are (1,2) and (2,3). We have $c(1)=1$, $c(2)=2$, $c(3)=1$. The local stabilities are $1, 0, 1$, summing to 2. The energized channels are (1,2) and (2,3), yielding a total cost of 4 + 5 = 9.