# Problem A — Register Synchronization

Time limit: 5 s   Memory limit: 256 MB

## Description

You are configuring a system with **n** hardware registers (numbered 1 to n). You can install bidirectional synchronizers between specific pairs of registers. Installing a synchronizer between two registers incurs a known hardware cost and permanently binds their contents, ensuring they always hold the exact same value. Because this binding is transitive, if register A is synchronized with register B, and B is synchronized with C, then A and C are also forced to hold the identical value.

The system relies on **t** critical registers. Your task is to install a set of synchronizers such that all **t** critical registers are guaranteed to hold the identical value. The remaining registers are auxiliary; you are not required to synchronize them, but you may choose to install synchronizers involving them if it provides a cheaper way to indirectly bind the critical registers together.

Determine the minimum total cost of the installed synchronizers required to ensure all critical registers are mutually synchronized.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2), representing the total number of registers, the number of available synchronizer connections, and the number of critical registers.
The second line contains **t** distinct integers: the identifiers of the critical registers.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): indicating that a synchronizer can be installed between register u and register v at a cost of w.
It is guaranteed that the available synchronizers are sufficient to bind all critical registers.

## Output

Print a single integer: the minimum total cost to synchronize all critical registers.

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

In Example 1, binding the three critical registers by installing synchronizers through the auxiliary register 4 (costs 1+1+1 = 3) is cheaper than installing synchronizers directly between the critical registers (which would cost 4). In Example 3, there is only one critical register, so no synchronizers are needed.