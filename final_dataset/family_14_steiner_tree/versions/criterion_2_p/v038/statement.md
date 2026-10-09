# Problem B — Priority Campus Network

Time limit: 2 s   Memory limit: 256 MB

## Description

A university campus consists of **n** facilities, numbered 1 through **n**. The administration plans to establish a private communication network that connects a specific group of **t** priority facilities.

They will achieve this by activating a subset of the currently dormant fiber-optic connections on campus. Each dormant connection links two facilities and requires a specific activation cost. The layout of these dormant connections guarantees that for any pair of facilities, there is exactly one sequence of connections linking them without reusing any connection. Exactly **n** − 1 dormant connections exist across the campus.

You must select a subset of these connections to activate such that all **t** priority facilities can communicate with one another, either directly or by routing signals through intermediate facilities. Your goal is to find the minimum possible total activation cost.

Additionally, the following conditions hold for all layouts:
- The total activation cost of all **m** dormant connections combined is strictly less than 200,000,000,000.
- The number of priority facilities **t** is at most **m** + 1.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ **t** ≤ **n**, 1 ≤ **n** ≤ 200000, **m** = **n** − 1).
The second line contains **t** distinct integers: the identifiers of the priority facilities.
Each of the subsequent **m** lines contains three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000), representing a dormant connection between facility **u** and facility **v** with an activation cost of **w**. It is guaranteed that the connections form the layout described above.

## Output

Print a single integer representing the minimum total activation cost required to link all priority facilities.

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
