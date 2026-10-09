# Problem A — Constraint System Optimization

Time limit: 5 s   Memory limit: 256 MB

## Description

You are analyzing a system of **n** abstract variables, indexed from 1 to n. You have the option to enforce various bidirectional equality constraints between pairs of variables. Enforcing a specific constraint between two variables requires a known computational overhead.

In this system, equality is fully deductive: if the enforced constraints logically imply that two variables must be equal, the system treats them as identical.

Among all the variables, a specific subset of **t** variables are designated as focal variables. 

Your objective is to select a set of constraints to enforce such that the system is logically forced to evaluate all **t** focal variables as equal to one another. You are free to enforce constraints involving non-focal variables; they follow the exact same deductive rules and can be used as intermediate steps to bridge equalities between focal variables.

Calculate the minimum possible total overhead required to enforce a valid set of constraints that achieves this condition among the focal variables.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the identifiers of the focal variables.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a potential equality constraint between variables u and v that requires w overhead to enforce.
The potential constraints are sufficient to allow all focal variables to be forced equal.

## Output

Print a single integer: the minimum total overhead of the enforced constraints required to ensure all **t** focal variables are equal.

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

In Example 1, enforcing the constraints between variable 4 and each of the three focal variables (overheads 1+1+1 = 3) successfully forces variables 1, 2, and 3 to be equal (since they all equal variable 4). This is more efficient than only enforcing constraints directly among the focal variables (which would cost 4). In Example 3, with only one focal variable, the requirement is already satisfied, so the minimum overhead is 0.