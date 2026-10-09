# Problem A — Memory Synchronization

Time limit: 5 s   Memory limit: 256 MB

## Description

You are configuring a system with **n** memory banks (numbered 1 to n). You can install two-way state-links between specific pairs of banks. Installing a link between two banks incurs a known hardware cost and permanently binds their contents, ensuring they always hold the exact same value. Because this binding propagates, any sequence of links connecting two banks forces them to hold identical values.

The system relies on **t** core banks. Your task is to select a set of links to install such that all **t** core banks are guaranteed to hold the identical value. You may install any subset of the available links. 

Determine the minimum total cost of the installed links required to satisfy this condition.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2), representing the total number of memory banks, the number of available state-links, and the number of core banks.
The second line contains **t** distinct integers: the identifiers of the core banks.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): indicating that a state-link can be installed between bank u and bank v at a cost of w.
It is guaranteed that the available links are sufficient to bind all core banks.

## Output

Print a single integer: the minimum total cost to ensure all core banks share the same value.

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

In Example 1, the condition can be met by installing links between (1,4), (2,4), and (3,4) for a total cost of 1+1+1 = 3. This forces banks 1, 2, and 3 to share the same value (along with bank 4). Alternatively, linking (1,2) and (2,3) costs 4. The minimum cost is 3. In Example 3, there is only one core bank, so no links are needed.