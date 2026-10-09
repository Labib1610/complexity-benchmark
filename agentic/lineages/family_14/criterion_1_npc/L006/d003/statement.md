# Problem A — Corporate Liquidity

Time limit: 5 s   Memory limit: 256 MB

## Description

A multinational corporation manages operations across $n$ distinct currencies (identified by integers 1 through $n$). The corporation holds its primary reserves in a strategic subset of $t$ currencies. 

The treasury department has a mandate to establish *consolidated liquidity* for these primary reserves. 

Initially, each currency operates in complete isolation. However, the treasury can access a market of $m$ bilateral swap agreements. Activating a swap agreement between currency $u$ and currency $v$ permanently merges their respective liquidity pools. When pools merge, all currencies that were previously part of either pool become mutually fungible within the new, unified pool. This merging is transitive: if currency $A$ is fungible with $B$, and $B$ is fungible with $C$, then $A$ and $C$ are fungible.

The corporation is free to activate agreements that involve non-primary currencies, provided these activations ultimately help consolidate the primary reserves. 

Each swap agreement carries a fixed regulatory capital lockup, denoted by $w$. The total regulatory burden incurred by the treasury is the sum of the capital lockups of the distinct agreements chosen for activation. 

Determine the minimum total regulatory burden required to select and activate a combination of swap agreements such that all $t$ primary currencies are consolidated into the exact same liquidity pool.

## Input

The first line provides three integers $n$, $m$, and $t$ (1 ≤ $t$ ≤ 10, 1 ≤ $n$ ≤ 100, 0 ≤ $m$ ≤ $n$·($n$−1)/2).
The second line lists $t$ distinct integers representing the identifiers of the primary currencies.
Each of the subsequent $m$ lines specifies an available swap agreement using three integers $u$, $v$, and $w$ (1 ≤ $u$, $v$ ≤ $n$, $u$ ≠ $v$, 1 ≤ $w$ ≤ 1000000). This indicates an agreement that merges the pools of currency $u$ and currency $v$ with a regulatory lockup of $w$.
It is guaranteed that the available agreements are sufficient to consolidate all primary currencies.

## Output

Print a single integer: the minimum total regulatory burden required to ensure all primary currencies share the same liquidity pool.

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

In Example 1, activating the swap agreements that connect to the non-primary currency 4 (which require capital lockups of 1, 1, and 1; total burden = 3) is more efficient than activating the agreements directly between the three primary currencies (which would result in a total burden of 4). 
In Example 3, there is only a single primary currency, so it already constitutes its own liquidity pool. No swap agreements need to be activated, resulting in a total burden of 0.