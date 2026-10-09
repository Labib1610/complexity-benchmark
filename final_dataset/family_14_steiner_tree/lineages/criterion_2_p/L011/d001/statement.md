# Problem B — Campus Network Infrastructure

Time limit: 2 s   Memory limit: 256 MB

## Description

A campus consists of **n** facilities, identified by integers from 1 to **n**. You have a list of potential bidirectional communication links that can be established between specific pairs of facilities, each requiring a certain investment. The infrastructure of potential links is comprehensive enough that it is possible to connect any facility to any other facility.

A specific subset of **t** facilities are designated as **core facilities**. Your objective is to select a subset of the potential links to establish such that all core facilities are able to communicate with one another. They may communicate directly or relay information through other intermediate facilities (which may or may not be core facilities themselves). 

Determine the minimum total investment required to establish a valid network that connects all core facilities.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line provides **t** distinct integers representing the identifiers of the core facilities.
Each of the subsequent **m** lines provides three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that a link can be established between facility **u** and facility **v** with an investment of **w**.

## Output

Output a single integer representing the minimum total investment needed to ensure all core facilities are connected.

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