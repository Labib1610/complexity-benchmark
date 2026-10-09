# Problem A — Variable Equivalences

Time limit: 5 s   Memory limit: 256 MB

## Description

You are analyzing a system of **n** variables, numbered 1 through **n**. You have the option to establish direct equivalences between specific pairs of variables. Establishing a direct equivalence between a specific pair incurs a known computational cost. 

Equivalence in this system is symmetric and transitive. If you establish a direct equivalence between variable $u$ and variable $v$, they become equivalent. Furthermore, if $u$ is equivalent to $v$, and $v$ is equivalent to $x$, then $u$ is equivalent to $x$ through transitivity. 

You are given a subset of **t** critical variables: $c_1, c_2, \dots, c_t$. Your objective is to select a single set of direct equivalences to establish such that all **t** critical variables become mutually equivalent to each other. 

You may establish equivalences involving non-critical variables; these can act as intermediaries to make critical variables equivalent via transitivity. Once a set of direct equivalences is paid for and established, all resulting transitive equivalences apply simultaneously at no additional cost. 

Determine the minimum total cost of direct equivalences you must establish to ensure that all **t** critical variables are equivalent. (If $t=1$, no equivalences are needed and the minimum cost is 0).

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2), representing the total number of variables, the number of available direct equivalences, and the number of critical variables.
The second line contains **t** distinct integers $c_1, c_2, \dots, c_t$: the identifiers of the critical variables. The order of these identifiers does not matter.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that a direct equivalence can be established between variable u and variable v at a cost of w.
It is guaranteed that the available direct equivalences are sufficient to make all critical variables equivalent.

## Output

Print a single integer: the minimum total cost to establish a set of direct equivalences that satisfies the requirement.

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

In Example 1, the critical variables are 1, 2, and 3. You can establish direct equivalences between (1,4), (2,4), and (3,4) for a total cost of 1+1+1 = 3. Because 1 is equivalent to 4 and 2 is equivalent to 4, 1 is equivalent to 2. Similarly, 3 is equivalent to 4, so all three critical variables become mutually equivalent. Alternatively, establishing direct equivalences (1,2) and (2,3) directly would cost 2+2 = 4. The minimum cost is 3. 

In Example 3, there is only one critical variable ($t=1$), so no equivalences are needed and the minimum cost is 0.