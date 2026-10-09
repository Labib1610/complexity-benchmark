# Problem A — Universal Interpretation

Time limit: 5 s   Memory limit: 256 MB

## Description

A galactic council contains representatives speaking **n** different dialects (numbered 1 through **n**). A specific mandate requires that a designated group of **t** core dialects must be mutually intelligible.

You can hire bilingual interpreters from a pool of candidates. Each candidate is proficient in exactly two dialects and requires a specific salary to be retained. 

Communication between dialects works as follows: if an interpreter is hired for a pair of dialects, speakers of those two dialects can freely exchange information. Furthermore, this exchange can chain together: if dialect A can exchange information with dialect B, and dialect B with dialect C, then dialect A can exchange information with dialect C.

Your task is to select a group of interpreters to hire such that information can be exchanged between any two of the **t** core dialects. You are allowed to hire interpreters for dialects outside the core group if using them as intermediaries reduces the total salary required.

Determine the minimum total salary needed to hire a valid group of interpreters.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the identifiers of the core dialects.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), representing a candidate interpreter who bridges dialect **u** and dialect **v** for a salary of **w**.
It is guaranteed that there exists at least one hiring arrangement that allows all core dialects to exchange information.

## Output

Print a single integer: the minimum total salary required to hire interpreters such that all core dialects can exchange information with each other.

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

In Example 1, hiring interpreters who bridge the core dialects to the non-core dialect 4 (requiring 1+1+1 = 3 salary) is cheaper than hiring interpreters to bridge the three core dialects directly (which would require 2+2 = 4 salary). In Example 3, there is only one core dialect, so no interpreters need to be hired (0 salary).
