# Problem C — Impossible Set Selection: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

You are given **j** jobs. For each job $k$ (where $k$ is a 1-based index from 1 to **j**), you must construct two sets of consecutive integers: $S_{1,k}$ (belonging to collection 1) and $S_{2,k}$ (belonging to collection 2). 

The set $S_{1,k}$ must contain exactly $p_{1,k}$ integers, and the set $S_{2,k}$ must contain exactly $p_{2,k}$ integers.

A valid construction must satisfy three rules:

- **Rule 1 (Domain):** Every set $S_{1,k}$ and $S_{2,k}$ must be a subset of the integer universe $\{1, 2, \dots, \mathbf{T}\}$.
- **Rule 2 (Disjointness):** For a given collection $c \in \{1, 2\}$, the sets $S_{c,1}, S_{c,2}, \dots, S_{c,j}$ must be mutually disjoint (no two sets in the same collection can share any integers).
- **Rule 3 (Strict Precedence):** For a given job $k$, every integer in $S_{1,k}$ must be strictly less than every integer in $S_{2,k}$.

For all test cases provided in this problem, it is guaranteed that no valid construction can satisfy all three rules simultaneously. Your task is to certify this impossibility by identifying a localized contradiction. Exactly one of the following two types of certificates will be valid for the given input. Print the one that applies:

- **Job-specific contradiction:** There is a single job **i** (1-based index) such that Rule 1 (for job **i**) and Rule 3 (for job **i**) cannot be simultaneously satisfied, even if we completely ignore Rule 2 and all other jobs. Print: `JOB i`.
- **Collection-specific contradiction:** There is a single collection **c** (where **c** is 1 or 2) such that Rule 1 (for collection **c**) and Rule 2 (for collection **c**) cannot be simultaneously satisfied, even if we completely ignore Rule 3 and the other collection. Print: `LOAD c`.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the required sizes of $S_{1,k}$ and $S_{2,k}$ respectively.

## Output

Print a single line containing the certificate of impossibility: either `JOB i` (where i is the job index) or `LOAD c` (where c is the collection number).

## Examples

### Example 1

**Input**
```
3 100
70 60
2 2
3 4
```

**Output**
```
JOB 1
```

### Example 2

**Input**
```
4 150
50 1
50 1
50 1
50 1
```

**Output**
```
LOAD 1
```

## Note

In Example 1, consider job 1. Rule 1 requires $S_{1,1}$ and $S_{2,1}$ to be subsets of $\{1, 2, \dots, 100\}$. Rule 3 requires every element of $S_{1,1}$ to be strictly less than every element of $S_{2,1}$. Since $S_{1,1}$ must contain 70 consecutive integers and $S_{2,1}$ must contain 60 consecutive integers, satisfying Rule 3 would require at least 130 distinct integers in the universe, which contradicts Rule 1. Thus, `JOB 1` is the correct certificate. 

In Example 2, no single job violates the rules on its own. However, consider collection 1. Rule 2 requires the four $S_{1,k}$ sets (each of size 50) to be mutually disjoint. Rule 1 requires all of them to be subsets of $\{1, 2, \dots, 150\}$. Four disjoint sets of size 50 require at least 200 distinct integers, which contradicts Rule 1. Thus, `LOAD 1` is the correct certificate.