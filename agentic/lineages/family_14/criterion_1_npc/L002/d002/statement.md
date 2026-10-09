# Problem A — Monetary Stabilization

Time limit: 5 s
Memory limit: 256 MB

## Description
A global financial institution is stabilizing a network of $n$ distinct regional currencies (numbered 1 to $n$).

Due to market fluctuations, the institution can establish fixed exchange pegs between certain pairs of currencies. There are $m$ proposed bilateral pegs available. Each peg allows direct, two-way value equivalence between a specific pair of currencies and requires a one-time capital reserve allocation to establish.

The institution's board has designated $t$ specific currencies as anchor currencies. Your objective is to determine the minimum total capital reserve allocation required to establish a set of pegs such that equivalent value can flow between any anchor currency and any other anchor currency. You may chain multiple pegs together to link anchor currencies. Furthermore, you are permitted to establish pegs involving non-anchor currencies if using them as intermediate steps reduces the overall reserve allocation required.

Write a program to calculate the minimum total capital reserve necessary to ensure all $t$ anchor currencies are linked in a single stabilized network.

## Input
The first line contains three integers $n$, $m$, and $t$ ($1 \le t \le 10$, $1 \le n \le 100$, $0 \le m \le n(n-1)/2$).
The second line contains $t$ distinct integers: the IDs of the anchor currencies.
Each of the next $m$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$, $1 \le w \le 1000000$), representing an available bilateral peg between currency $u$ and currency $v$ that requires a capital reserve allocation of $w$.
The available pegs are sufficient to ensure all anchor currencies can be linked.

## Output
Print a single integer: the minimum total capital reserve allocation to ensure all anchor currencies are linked.

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
In Example 1, routing the equivalence through the non-anchor currency 4 (which requires a reserve of 1+1+1 = 3) is more cost-effective than establishing the pegs that directly link the three anchor currencies (which would require a reserve of 4). 
In Example 3, there is only one anchor currency, so no pegs are needed.