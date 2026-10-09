# Problem A — Memory Synchronization

Time limit: 5 s   Memory limit: 256 MB

## Description

You are configuring a system with **n** memory banks (numbered 1 to **n**). You can install two-way state-links between specific pairs of banks. Installing a link between two banks incurs a known hardware cost. Once installed, a link can carry synchronization signals between its endpoints in either direction.

The system relies on a sequence of **t** core banks, provided in a specific order: $c_1, c_2, \dots, c_t$. To guarantee system stability, you must satisfy a chain of synchronization requirements: for every index $i$ from 1 to $t-1$, there must exist a path of installed state-links connecting core bank $c_i$ to core bank $c_{i+1}$. 

You may install any subset of the available links. Once a link is installed and paid for, it can be used in any number of these paths at no extra cost. The installed links do not need to form a single continuous line; they can form any network structure as long as the required paths exist within it. Your task is to select a single overall set of links to install such that all $t-1$ connectivity requirements are simultaneously met.

Determine the minimum total cost of the installed links required to satisfy these conditions. (If $t=1$, no paths are required and the minimum cost is 0).

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2), representing the total number of memory banks, the number of available state-links, and the number of core banks.
The second line contains **t** distinct integers $c_1, c_2, \dots, c_t$: the identifiers of the core banks in their specified sequence.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): indicating that a state-link can be installed between bank u and bank v at a cost of w.
It is guaranteed that the available links are sufficient to satisfy all requirements.

## Output

Print a single integer: the minimum total cost of a set of installed links that satisfies the chain of requirements.

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

In Example 1, the core banks are 1, 2, and 3. The requirements are to establish a path from 1 to 2, and a path from 2 to 3. This can be met by installing links between (1,4), (2,4), and (3,4) for a total cost of 1+1+1 = 3. The path for 1 to 2 routes via bank 4, and the path for 2 to 3 also routes via bank 4. Alternatively, installing links (1,2) and (2,3) directly would cost 2+2 = 4. The minimum cost is 3. 

In Example 3, there is only one core bank ($t=1$), so there are no routing requirements and no links are needed.