# Problem A — Facility Fiber Integration

Time limit: 5 s   Memory limit: 256 MB

## Description

A campus consists of **n** facilities (numbered 1 through **n**). You have a list of potential bidirectional fiber links that can be installed between certain pairs of facilities, each with a specific installation expense.

A specific subset of **t** facilities are designated as *primary*. The goal is to establish a communication network so that every primary facility can transmit data to every other primary facility. Data can flow between any two facilities as long as there is a contiguous sequence of installed fiber links connecting them.

You may select any combination of the available fiber links to achieve this goal. Determine the minimum possible total expense required to ensure all primary facilities can communicate with one another.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the identifiers of the primary facilities.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), representing a potential fiber link between facility **u** and facility **v** with an installation expense of **w**.
It is guaranteed that the available potential links are sufficient to allow all primary facilities to communicate.

## Output

Print a single integer: the minimum total expense to install the links.

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

In Example 1, selecting the fiber links connecting facility 4 to facilities 1, 2, and 3 incurs a total expense of 1 + 1 + 1 = 3. This successfully allows the primary facilities (1, 2, and 3) to communicate and is more economical than linking them exclusively using direct connections between each other, which would require an expense of at least 4. In Example 3, there is only one primary facility, so no fiber links need to be installed.