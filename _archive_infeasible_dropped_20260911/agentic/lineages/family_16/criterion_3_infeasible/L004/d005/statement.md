# Problem C — Impossible Deadline: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A manufacturing facility processes **j** orders using two specialized workstations (workstation 1 and workstation 2). For each order $k$ (where $k$ is a 1-based index from 1 to **j**), you are given its required continuous processing time on workstation 1, denoted $p_{1,k}$, and on workstation 2, denoted $p_{2,k}$.

A valid schedule must assign a continuous time interval $I_{1,k}$ (of exact length $p_{1,k}$) and $I_{2,k}$ (of exact length $p_{2,k}$) for each order $k$, subject to three rules:

- **Rule 1 (Resource Isolation):** For a given workstation $c \in \{1, 2\}$, the intervals $I_{c,1}, I_{c,2}, \dots, I_{c,j}$ must be mutually disjoint (they cannot overlap in time, though they may share endpoints).
- **Rule 2 (Precedence):** For a given order $k$, the interval $I_{2,k}$ must begin no earlier than the end of interval $I_{1,k}$.
- **Rule 3 (Deadline):** Every interval $I_{1,k}$ and $I_{2,k}$ must be completely contained within the time window $[0, \mathbf{T}]$.

For all test cases provided in this problem, it is guaranteed that no schedule can satisfy all three rules simultaneously. Your task is to certify this impossibility by identifying a localized contradiction. Exactly one of the following two types of certificates will be valid for the given input. Print the one that applies:

- **Order-specific contradiction:** There is a single order **i** (1-based index) such that Rule 2 (for order **i**) and Rule 3 (for order **i** on both workstations) cannot be simultaneously satisfied, even if we completely ignore Rule 1 and all other orders. Print: `JOB i`.
- **Workstation-specific contradiction:** There is a single workstation **c** (where **c** is 1 or 2) such that Rule 1 (for workstation **c**) and Rule 3 (for workstation **c** across all orders) cannot be simultaneously satisfied, even if we completely ignore Rule 2 and the other workstation. Print: `LOAD c`.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the processing times of an order on workstation 1 and workstation 2.

## Output

Print a single line containing the certificate of impossibility: either `JOB i` (where i is the order index) or `LOAD c` (where c is the workstation number).

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

In Example 1, consider order 1. Rule 3 requires $I_{1,1}$ and $I_{2,1}$ to fit entirely within $[0, 100]$. Rule 2 requires $I_{2,1}$ to start after $I_{1,1}$ ends. Since their lengths are 70 and 60 respectively, they require at least 130 units of time in sequence, which contradicts Rule 3. Thus, `JOB 1` is the correct certificate. 

In Example 2, no single order violates the rules on its own. However, consider workstation 1. Rule 1 requires the four $I_{1,k}$ intervals (each of length 50) to be mutually disjoint. Rule 3 requires all of them to be completely contained within $[0, 150]$. Four disjoint intervals of length 50 require at least 200 units of time, which contradicts Rule 3. Thus, `LOAD 1` is the correct certificate.