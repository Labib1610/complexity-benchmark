# Problem A — Cluster Unification

Time limit: 5 s   Memory limit: 256 MB

## Description

You are managing a system of **n** initially isolated data clusters, numbered 1 through **n**. 
Your specific objective is to ensure that a critical subset of **t** clusters, identified as $c_1, c_2, \dots, c_t$, are fully integrated.

To integrate the system, you can execute merge procedures. You are provided with a list of **m** available merge procedures. Each procedure specifies two clusters, $u$ and $v$, and a one-time execution cost of $w$. When a procedure is executed, it permanently combines the entire group containing cluster $u$ and the entire group containing cluster $v$ into a single, unified group. 

You must choose a subset of these merge procedures to execute such that all **t** critical clusters end up in the exact same unified group. You may freely involve non-critical clusters in the merges if doing so results in a lower total cost. 

Determine the minimum total execution cost required to bring all **t** critical clusters into the same group. (If $t=1$, no procedures are needed, so the minimum cost is 0).

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2), representing the total number of clusters, the number of available merge procedures, and the number of critical clusters.
The second line contains **t** distinct integers $c_1, c_2, \dots, c_t$: the identifiers of the critical clusters.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that a merge procedure between cluster u and cluster v can be executed for a cost of w.
It is guaranteed that the available merge procedures are sufficient to bring all critical clusters into the same group.

## Output

Print a single integer: the minimum total execution cost.

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

In Example 1, the critical clusters are 1, 2, and 3. You can execute the merge procedures between (1,4), (2,4), and (3,4) for a total cost of 1+1+1 = 3. 
Executing (1,4) merges cluster 1 and 4. Executing (2,4) merges cluster 2 into the same group. Executing (3,4) merges cluster 3 into that group. All critical clusters are now in the same group. 
Alternatively, you could execute procedures (1,2) and (2,3) for a total cost of 2+2 = 4 to put clusters 1, 2, and 3 in the same group. The minimum cost is 3.

In Example 3, there is only one critical cluster ($t=1$), so no procedures are needed. The minimum cost is 0.