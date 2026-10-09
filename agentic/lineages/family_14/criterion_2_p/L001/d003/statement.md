# Problem B — Core Factions

Time limit: 2 s   Memory limit: 256 MB

## Description

You are analyzing a political landscape of **n** factions (numbered 1 to n) and **m** bilateral treaties. The treaties link all **n** factions into a single diplomatic network. The network is structured such that there is exactly one simple sequence of treaties connecting any two factions.

A specific group of **t** factions are designated as **core**. Your objective is to form a coalition that includes all **t** core factions. To do this, you must select a subset of the treaties to uphold, ensuring that every core faction is connected to every other core faction through the upheld treaties. Non-core factions can be part of the coalition if they serve as intermediaries.

Each treaty has a maintenance cost. You must determine the absolute minimum total maintenance cost required to uphold a set of treaties that fully connects all core factions.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the ids of the core factions.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000) representing a bilateral treaty between faction u and faction v with a maintenance cost of w.

## Output

Print a single integer: the minimum total maintenance cost to fully connect all core factions.

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

## Note

In Example 1, the core factions 1 and 4 can only be connected if the treaties (1,2), (2,3), and (3,4) are all upheld. The total cost is 5 + 1 + 2 = 8.
In Example 2, there is only one core faction, so no treaties need to be upheld. The minimum total cost is 0.
In Example 3, core factions 1, 2, and 3 must all be connected. Upholding the treaty (1,2) with cost 4 and the treaty (2,3) with cost 5 achieves this for a total cost of 9.