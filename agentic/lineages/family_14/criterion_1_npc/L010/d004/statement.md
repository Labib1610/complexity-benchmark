# Problem A — Algebraic Equivalence Verification

Time limit: 5 s   Memory limit: 256 MB

## Description

An automated theorem prover is analyzing **n** complex algebraic expressions, numbered 1 through **n**. To simplify the system, the prover can run specific verification subroutines to establish that certain pairs of expressions are mathematically equivalent. 

You are given a list of **m** available subroutines. Running a subroutine for expression **u** and expression **v** consumes **w** units of computing power. Once run, the equivalence **u** ≡ **v** is established permanently and operates bidirectionally. The total computing power consumed is the sum of the costs of all subroutines you choose to run.

By the properties of equality, equivalence is transitive: if **A** ≡ **B** and **B** ≡ **C** are established (either directly or via a longer chain of established equivalences), then **A** ≡ **C** is also implicitly established without consuming additional power.

The prover has identified a specific set of **t** target expressions. Your task is to select a set of subroutines to run such that all **t** target expressions are proven to be mutually equivalent to one another. You may run subroutines involving any of the **n** expressions, leveraging non-target expressions as intermediate transitive steps if it reduces the total computing power required.

Determine the absolute minimum total computing power needed to establish that all **t** target expressions are equivalent.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers representing the identities of the target expressions.
The next **m** lines each provide three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that a subroutine is available to directly establish the equivalence between expression **u** and expression **v** for a cost of **w** units of computing power.
It is guaranteed that it is possible to prove all **t** target expressions are equivalent using the available subroutines.

## Output

Output a single integer representing the minimum total computing power required to ensure all target expressions are mutually equivalent.

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

In Example 1, establishing the equivalences 1 ≡ 4, 2 ≡ 4, and 3 ≡ 4 costs 1 + 1 + 1 = 3. By transitivity, expressions 1, 2, and 3 are all proven equivalent. This is more efficient than establishing 1 ≡ 2 and 2 ≡ 3 directly, which would cost 2 + 2 = 4. 

In Example 3, there is only one target expression, which is vacuously equivalent to itself, so no subroutines need to be run.