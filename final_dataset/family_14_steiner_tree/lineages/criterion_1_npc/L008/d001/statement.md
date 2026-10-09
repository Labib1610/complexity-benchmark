# Problem A — Grid Integration

Time limit: 5 s   Memory limit: 256 MB

## Description

An offshore wind farm has **n** platforms (numbered 1..n). Certain pairs of platforms can be joined by a submarine cable at a given material cost.

Among the platforms, **t** contain **primary turbines**. You must select a set of submarine cables to install so that every primary turbine platform can exchange energy with every other primary turbine platform, either directly or via a sequence of installed cables. 

Determine the minimum total material cost of a set of cables that satisfies this requirement.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the ids of the primary turbine platforms.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a submarine cable option joining platforms u and v at cost w.
The available cable options are sufficient to allow all primary turbine platforms to exchange energy.

## Output

Print a single integer: the minimum total material cost of the installed cables.

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

In Example 1, purchasing the cables joining platform 4 to platforms 1, 2, and 3 (total cost 1+1+1 = 3) allows the three primary turbine platforms to exchange energy, which is cheaper than installing cables strictly between the primary turbine platforms themselves (which would cost 4). In Example 3 there is only one primary turbine platform, so no cabling is needed.