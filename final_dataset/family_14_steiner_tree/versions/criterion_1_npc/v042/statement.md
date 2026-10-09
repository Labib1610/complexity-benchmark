# Problem A — Deep-Rock Excavation

Time limit: 5 s   Memory limit: 256 MB

## Description

A mining corporation has mapped out **n** underground chambers (numbered 1..n). Within this network, **t** specific chambers contain rare mineral deposits. The corporation wants to select a set of tunnels to excavate so that all **t** deposit chambers end up connected to each other (either directly or through intermediate chambers). 

The geological survey provides a list of potential tunnels that can be excavated, each with a given cost. The remaining chambers without deposits are optional intermediaries: you may route your excavated network through them if it reduces the overall cost, or ignore them entirely.

Determine the minimum total excavation cost of a set of tunnels that successfully connects all deposit chambers.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the IDs of the deposit chambers.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a potential tunnel between chamber **u** and chamber **v** that costs **w** to excavate.
The available potential tunnels are enough to connect all deposit chambers.

## Output

Print a single integer: the minimum total excavation cost to connect all deposit chambers.

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

In Example 1, routing the network through the optional intermediary chamber 4 (excavating tunnels at costs 1+1+1 = 3) is cheaper than connecting the three deposit chambers directly (which would cost 4). In Example 3 there is only one deposit chamber, so no tunnels need to be excavated.
