# Problem A — Infrastructure Integration

Time limit: 5 s   Memory limit: 256 MB

## Description

A facility consists of **n** locations (numbered 1 to **n**). You have the option to install communication links between specific pairs of locations, each requiring a known budget.

A specific subset of **t** locations are designated as *mandatory*. Your task is to select and fund a set of links such that every mandatory location can exchange data with every other mandatory location. Data can pass through any number of funded links in sequence, and you may freely establish links through any of the other non-mandatory locations if doing so reduces your total budget.

Determine the smallest total budget required to ensure all mandatory locations are integrated into the same continuous structure of funded links.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the ids of the mandatory locations.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that a link can be installed between location **u** and location **v** for a budget of **w**.
It is guaranteed that sufficient links exist to integrate all mandatory locations.

## Output

Print a single integer: the minimum total budget required to integrate all mandatory locations.

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

In Example 1, establishing a structure through the non-mandatory location 4 (budget 1+1+1 = 3) is cheaper than linking the three mandatory locations directly (which would require a budget of 4). In Example 3 there is only one mandatory location, so no links are needed.
