# Problem A — Streamlined Fiber Deployment

Time limit: 5 s
Memory limit: 256 MB

## Description
A regional energy provider is streamlining its grid communications. The grid consists of $n$ substations, and field engineers have identified $m$ viable corridors where fiber-optic cable can be laid. The exact installation expense for each corridor is known.

Initially, the goal was to link all substations into a single unified grid. However, a recent policy change dictates that only a small core of $t$ "primary" substations needs guaranteed connectivity. 

Your task is to design a streamlined network. You must select a subset of the available corridors to install such that all $t$ primary substations can exchange messages with one another (i.e., they are all in the same connected component). The remaining $n - t$ "secondary" substations do not require connectivity, but you are free to route fiber through any of them if using them as cheap passive relays reduces the total installation expense. 

Since $t$ is very small (at most 10), the primary substations form a compact core. Any valid streamlined network can be viewed as a grid-wide network from which all outer branches serving only secondary substations have been pruned. Because the network contains many redundant corridors, you can often rely on direct, low-cost routes between the primary substations. You must use these properties to find the absolute minimum total expense required to ensure the primary substations are fully connected.

## Input
The first line contains three integers $n$, $m$, and $t$ ($1 \le t \le 10$, $1 \le n \le 100$, $0 \le m \le n(n-1)/2$).
The second line contains $t$ distinct integers: the IDs of the primary substations (substations are numbered 1 to $n$).
Each of the next $m$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$, $1 \le w \le 1000000$), representing a viable corridor between substation $u$ and substation $v$ with an installation expense of $w$.
It is guaranteed that the surveyed corridors are sufficient to connect all primary substations.

## Output
Print a single integer: the minimum total expense to ensure all primary substations are connected.

## Examples

### Example 1

**Input**
```
4 6 3
1 2 3
1 4 1
2 4 1
3 4 1
1 2 2
2 3 2
1 3 2
```

**Output**
```
3
```

### Example 2

**Input**
```
4 4 3
1 2 3
1 2 1
2 3 1
1 4 10
3 4 10
```

**Output**
```
2
```

### Example 3

**Input**
```
3 2 1
1
1 2 5
2 3 5
```

**Output**
```
0
```

## Note
In Example 1, routing the fiber through the secondary substation 4 (which costs 1+1+1 = 3) is cheaper than linking the three primary substations directly to each other (which would cost 4). 
In Example 3, there is only one primary substation, so no fiber links need to be installed.
