# Problem B — Economic Integration

Time limit: 2 s   Memory limit: 256 MB

## Description

A global trade alliance involves **n** distinct regional currencies, identified by integers from 1 to **n**. You are analyzing a list of proposed bilateral peg agreements. Each agreement would permanently lock the exchange rate between a specific pair of currencies. The list of proposed agreements is comprehensive enough that, if all were enacted, it would be possible to convert any currency to any other currency at a fixed, unchanging rate.

Within this alliance, a specific subset of **t** currencies are designated as **reserve currencies**. Your objective is to enact a subset of the proposed peg agreements such that all reserve currencies are locked into a single fixed-exchange network. They may be locked together directly by an agreement, or transitively through other currencies (which may or may not be reserve currencies themselves). 

Each proposed peg agreement requires a specific annual subsidy to maintain. Determine the minimum total subsidy required to enact a valid set of agreements that locks all reserve currencies together.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line provides **t** distinct integers representing the identifiers of the reserve currencies.
Each of the subsequent **m** lines provides three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that a peg agreement can be enacted between currency **u** and currency **v** with an annual subsidy of **w**.

## Output

Output a single integer representing the minimum total subsidy needed to ensure all reserve currencies are locked together.

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