# Problem B — Market-Linked Portfolio Selection

Time limit: 2 s   Memory limit: 256 MB

## Description

You are designing a financial fund from a market of **n** available assets, numbered 1 to **n**. There are **m** bilateral hedging contracts currently established in the market. Each contract links two distinct assets and carries a positive maintenance fee.

The market is structured such that the entire system of **n** assets is fully *market-linked*. A subset of assets $F$ is defined as *market-linked* if it is impossible to partition $F$ into two non-empty sub-portfolios such that no hedging contract links an asset in the first sub-portfolio to an asset in the second. (A subset consisting of a single asset cannot be partitioned and is inherently market-linked).

You must select a subset of assets to form your fund, satisfying the following regulatory criteria:
1. The fund must include a specific list of **t** *mandatory assets*.
2. The fund itself must be *market-linked*.

When you select your fund, any hedging contract that has BOTH of its linked assets included in your fund becomes active, and you must pay its maintenance fee. Contracts where one or both linked assets are excluded from your fund remain dormant and cost nothing.

Your objective is to determine the minimum total maintenance fee required to form a valid fund.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line provides **t** distinct integers representing the labels of the mandatory assets.
Each of the subsequent **m** lines provides three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating a hedging contract between asset **u** and asset **v** with a maintenance fee of **w**.

## Output

Output a single integer representing the minimum total maintenance fee of the active hedging contracts.

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