# Problem A — Corporate Liquidity

Time limit: 5 s   Memory limit: 256 MB

## Description

A financial market has **n** currencies (numbered 1..n). There are **m** available exchange mechanisms. An exchange mechanism allows bidirectional conversion between currency **u** and currency **v**, and establishing this mechanism requires a one-time regulatory fee of **w**.

A multinational corporation holds reserves in a specific subset of **t** primary currencies. The corporation needs to ensure pure liquidity among these primary reserves.

Pure liquidity is achieved if the corporation can convert any primary currency into any other primary currency, possibly through a chain of established exchange mechanisms. The corporation is allowed to establish exchange mechanisms involving non-primary currencies if they serve as intermediaries in a conversion chain.

Determine the minimum total regulatory fee the corporation must pay to establish a set of exchange mechanisms that provides pure liquidity among all primary currencies.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ **t** ≤ 10, 1 ≤ **n** ≤ 100, 0 ≤ **m** ≤ **n**·(**n**−1)/2).
The second line contains **t** distinct integers: the ids of the primary currencies.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000): an exchange mechanism between currency **u** and currency **v** with a regulatory fee of **w**.
The available exchange mechanisms are sufficient to achieve pure liquidity.

## Output

Print a single integer: the minimum total regulatory fee to achieve pure liquidity among all primary currencies.

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

In Example 1, establishing exchange mechanisms through the non-primary currency 4 (fees 1+1+1 = 3) is cheaper than establishing mechanisms between the three primary currencies directly (which would cost 4). In Example 3 there is only one primary currency, so no exchange mechanisms need to be established.