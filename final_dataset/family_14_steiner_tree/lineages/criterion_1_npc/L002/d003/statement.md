# Problem A — Database Synchronization

Time limit: 5 s
Memory limit: 256 MB

## Description
You are configuring a distributed database cluster consisting of $n$ nodes. 

There are $m$ bilateral synchronization agreements available for activation. Activating an agreement between two nodes incurs a one-time licensing cost. When an agreement is active, the two nodes maintain identical state. This state sharing is transitive: if node X shares state with node Y, and node Y shares state with node Z, then node X and node Z also share identical state.

A specific subset of $t$ nodes have been designated as primary ledgers. Your objective is to select a set of agreements to activate such that all $t$ primary ledgers share identical state. You are permitted to activate agreements that involve non-primary nodes; if utilizing them as transitive conduits reduces the overall licensing cost, it is a valid strategy.

Write a program to calculate the minimum total licensing cost necessary to ensure all $t$ primary ledgers share identical state.

## Input
The first line contains three integers $n$, $m$, and $t$.
The cluster size $n$ is limited to a maximum of 100 nodes by the hardware controller, with a minimum of 1 node. The number of available agreements $m$ ranges from a minimum of 0 up to a fully connected mesh of $n(n-1)/2$. The number of primary ledgers $t$ is constrained by the 10 available master keys (so at most 10), and there is always at least 1.

The second line contains $t$ distinct integers: the IDs of the primary ledgers.

Each of the next $m$ lines contains three integers $u$, $v$, and $w$, representing an available agreement between node $u$ and node $v$ that requires a licensing cost of $w$. Each agreement connects two distinct nodes (identified by integers from 1 to $n$, where $u \neq v$). The licensing cost $w$ is at least 1 and is capped at an enterprise limit of 1000000.

It is guaranteed that the available agreements are sufficient to ensure all primary ledgers can share identical state.

## Output
Print a single integer: the minimum total licensing cost to ensure all primary ledgers share identical state.

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
In Example 1, configuring the state sharing through the non-primary node 4 (which requires a cost of 1+1+1 = 3) is more cost-effective than activating the agreements that directly involve only the three primary ledgers (which would require a cost of 4). 
In Example 3, there is only one primary ledger, so no agreements need to be activated.