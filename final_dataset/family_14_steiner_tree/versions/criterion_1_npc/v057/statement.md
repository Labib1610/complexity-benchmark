# Strategic Risk Mitigation

Time limit: 5 s
Memory limit: 256 MB

## Description

A multinational firm manages risk across a catalog of $n$ distinct commodities (identified by integers 1 through $n$). The firm's automated risk management pipeline operates in three sequential phases.

In Phase 1, the market analysis engine monitors market volatility and flags a specific portfolio of $t$ core commodities that are highly vulnerable to sudden price divergence. 

In Phase 2, the risk mitigation module receives this portfolio along with a list of $m$ available bilateral hedge agreements. Purchasing an agreement between commodity $u$ and commodity $v$ requires an upfront capital allocation of $w$. Once purchased, the price movements of $u$ and $v$ become perfectly coupled. This coupling is transitive: if commodity $X$ and commodity $Y$ are connected through any sequence of purchased hedge agreements, their price movements are also perfectly coupled. The mitigation module's objective is to compute the exact minimum capital required to purchase a set of agreements such that all $t$ core commodities are perfectly coupled with each other. The module is permitted to purchase agreements involving non-core commodities if utilizing them as intermediaries results in a lower overall capital requirement.

In Phase 3, the execution layer takes the single minimum capital figure computed in Phase 2, drafts a budget requisition, and submits it to the board for immediate approval.

You are tasked with implementing the Phase 2 risk mitigation module. Given the output of Phase 1 and the available hedge agreements, determine the minimum capital requisition required to couple all core commodities.

## Input

The first line provides three integers $n$, $m$, and $t$ (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains $t$ distinct integers representing the identifiers of the core commodities flagged in Phase 1.
Each of the subsequent $m$ lines contains three integers $u$, $v$, and $w$ (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), detailing an available hedge agreement between commodity $u$ and commodity $v$ that requires $w$ capital.
It is guaranteed that the available agreements are sufficient to couple the core commodities.

## Output

Print a single integer: the minimum total capital required to ensure all core commodities are perfectly coupled.

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

In Example 1, purchasing the agreements that couple commodities 1, 2, and 3 via the non-core commodity 4 requires 1+1+1 = 3 capital. This is more efficient than purchasing direct agreements among the core commodities, which would require 2+2 = 4 capital to couple all three. 
In Example 3, Phase 1 only flagged a single core commodity, meaning it is inherently coupled with itself and requires 0 capital.
