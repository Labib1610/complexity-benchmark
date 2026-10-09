# Problem A — Corporate Consolidation

Time limit: 5 s   Memory limit: 256 MB

## Description

A venture capital firm is looking to consolidate a fragmented market consisting of **n** independent companies (numbered 1 to **n**). 

Through market research, the firm has identified **m** possible bilateral merger deals. Each potential deal allows two specific companies to merge, requiring a known, one-time capital investment to execute. 

When a deal is executed, the two companies—along with any other companies they are already joined with—become part of the exact same unified corporate entity. This consolidation is transitive: if company $X$ is merged into the same entity as $Y$, and $Y$ is merged into the same entity as $Z$, then $X$, $Y$, and $Z$ all belong to a single unified corporate entity.

Within this market, there are **t** key companies that each own a crucial segment of a highly lucrative technology patent. The venture capital firm's ultimate goal is to ensure that all **t** of these key companies end up belonging to the *same* single corporate entity, allowing the patent to be fully assembled.

The remaining **n** − **t** companies do not own any part of the patent. However, they can still be involved in mergers if using them as intermediaries creates a cheaper overall sequence of deals to unite the key companies.

Determine the absolute minimum total capital investment required to execute a subset of merger deals such that every one of the **t** key companies shares the exact same unified corporate entity.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the identification numbers of the key companies holding the patent segments.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that a merger deal can be executed between company **u** and company **v** for a cost of **w** million dollars.
It is guaranteed that it is possible to unite all key companies into a single entity using the available deals.

## Output

Print a single integer: the minimum total capital investment (in millions of dollars) required to ensure all key companies belong to the same corporate entity.

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

In Example 1, executing mergers between the key companies (1, 2, and 3) and company 4 requires three deals (costing 1+1+1 = 3). Because company 4 merges with 1, 2, and 3, all four companies become a single entity, which unites the key companies more cheaply than merging the key companies directly with one another (which would cost 4). 

In Example 3, there is only one key company, so it already constitutes a single entity holding the required patent segments, requiring 0 capital investment.
