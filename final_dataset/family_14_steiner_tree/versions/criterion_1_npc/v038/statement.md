# Problem A — Module Synchronization

Time limit: 5 s
Memory limit: 256 MB

## Description

You are configuring a synchronization protocol for $n$ distinct processing modules (numbered 1 to $n$). 
You can implement a bilateral data bridge between certain pairs of modules. Implementing a bridge between module $u$ and module $v$ adds $w$ milliseconds of latency overhead to the system. 

There are $t$ *core* modules. Your task is to select a subset of available bridges to implement so that the core modules are perfectly synchronized. Synchronization is achieved if, for every pair of core modules, information can propagate between them through a sequence of implemented bridges. You may implement bridges that involve non-core modules if doing so lowers the overall latency overhead.

Determine the minimum total latency overhead required to synchronize all core modules.

## Input

The first line contains three integers $n$, $m$, and $t$ ($1 \le t \le 10$, $1 \le n \le 100$, $0 \le m \le n(n-1)/2$).
The second line contains $t$ distinct integers: the identifiers of the core modules.
Each of the next $m$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \ne v$, $1 \le w \le 1000000$): an available bilateral bridge between modules $u$ and $v$ with a latency overhead of $w$.

It is guaranteed that:
- The available bridges are sufficient to synchronize all core modules.
- The number of core modules $t$ is never greater than the total number of modules $n$.
- The sum of the latency overheads of all available bridges in the input does not exceed $4,950,000,000$.

## Output

Print a single integer: the minimum total latency overhead required to synchronize all core modules.

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

In Example 1, utilizing the non-core module 4 (which incurs an overhead of 1+1+1 = 3) is more efficient than bridging the three core modules directly (which would incur an overhead of 4). In Example 3, there is only one core module, so no bridges need to be implemented.
