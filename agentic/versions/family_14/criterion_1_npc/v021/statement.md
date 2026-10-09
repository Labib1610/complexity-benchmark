# Market Stability

Time limit: 5 s
Memory limit: 256 MB

## Description

A market trades $n$ distinct commodities (numbered 1 to $n$). The regulatory authority wants to stabilize the market by locking the exchange rates between certain commodities. 

The regulator can purchase any subset of the $m$ available bilateral price-fixing contracts. Purchasing the available contract between commodity $u$ and commodity $v$ costs $w$ regulatory credits. Once this contract is purchased, the exchange rate between $u$ and $v$ becomes strictly fixed.

Exchange rate stability is transitive. The exchange rate between commodity $X$ and commodity $Y$ is considered strictly fixed if there exists a sequence of commodities $c_1, c_2, \dots, c_k$ (with $c_1 = X$ and $c_k = Y$) such that a contract has been purchased between $c_i$ and $c_{i+1}$ for every $1 \le i < k$.

The regulator has a mandate to guarantee that the exchange rates between all pairs of commodities in a specific portfolio of $t$ key commodities are strictly fixed. The regulator may purchase contracts involving commodities outside this key portfolio if doing so results in a lower total cost. 

Determine the minimum total regulatory credits that must be spent to fulfill the mandate.

## Input

The first line contains three integers $n$, $m$, and $t$ (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains $t$ distinct integers: the identifiers of the key commodities.
Each of the next $m$ lines contains three integers $u$, $v$, and $w$ (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), representing an available contract between commodity $u$ and commodity $v$ that costs $w$ credits.
The available contracts are sufficient to fulfill the mandate.

## Output

Print a single integer: the minimum total credits required to fix the exchange rates among all key commodities.

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

In Example 1, purchasing contracts that involve commodity 4 (costs 1+1+1 = 3) is cheaper than purchasing contracts directly between the three key commodities (which would cost 2+2 = 4 to fix the rates between all three). In Example 3, there is only one key commodity, so no contracts need to be purchased.
