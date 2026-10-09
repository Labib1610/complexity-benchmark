# Infeasible Coordinate Assignments

Time limit: 2 s   Memory limit: 256 MB

## Description

You are given a target threshold $T$ and a set of $j$ elements. Each element $i$ (from $1$ to $j$) is associated with two positive integers, $q_{1,i}$ and $q_{2,i}$.

Consider the problem of assigning a real-valued coordinate $w_{c,i}$ to each element $i$ for each stage $c \in \{1, 2\}$. The assignment must satisfy the following three conditions:
1. **Separation:** For every element $i$, $w_{2,i} - w_{1,i} \ge q_{1,i} + q_{2,i}$.
2. **Dispersion:** For each stage $c \in \{1, 2\}$ and every pair of distinct elements $i$ and $k$, $|w_{c,i} - w_{c,k}| \ge q_{c,i} + q_{c,k}$.
3. **Boundary:** For every element $i$, $w_{1,i} \ge q_{1,i}$ and $w_{2,i} \le 2T - q_{2,i}$.

For every test case, it is guaranteed that no such full assignment of $w_{c,i}$ exists. Your task is to provide a directly checkable certificate of unsatisfiability by identifying a specific relaxed subsystem of these constraints that is already impossible to satisfy on its own. 

To formalize the certificates, we define the symmetric margin function for a coordinate $w$ and parameter $q$ as:
$$S(w, q) = \min(w - q, (2T - q) - w)$$

You must output a valid certificate of unsatisfiability from one of the two allowed forms below. It is mathematically guaranteed that at least one such certificate is valid for every test case.

- `JOB i` : For the element at 1-based index $i$, the subsystem consisting only of the Separation constraint for $i$ and the Boundary constraints for $i$ cannot be simultaneously satisfied (ignoring all other elements and conditions).
- `LOAD c` : where $c \in \{1, 2\}$. This certifies that the subsystem consisting only of the Dispersion constraints for stage $c$, along with the requirement that $S(w_{c,i}, q_{c,i}) \ge 0$ for all $i$, cannot be simultaneously satisfied (ignoring the other stage and all other conditions).

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **q1** and **q2** (1 ≤ q1, q2 ≤ 1000000): the values of $q_{1,i}$ and $q_{2,i}$ for the $i$-th element.

## Output

Print a single line containing a valid certificate: `JOB i` or `LOAD c` as described above.

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

In Example 1, for element 1, the `JOB` subsystem requires $w_{1,1} \ge 70$, $w_{2,1} - w_{1,1} \ge 130$, and $w_{2,1} \le 140$. Combining the first two inequalities gives $w_{2,1} \ge 200$, which contradicts $w_{2,1} \le 140$. Thus, this subsystem is unsatisfiable for element 1, making `JOB 1` a valid certificate.

In Example 2, no single element violates the `JOB` subsystem. However, for `LOAD 1`, the subsystem requires four real numbers $w_{1,i}$ to simultaneously satisfy $S(w_{1,i}, 50) \ge 0$. Evaluating the symmetric margin function, this means $\min(w_{1,i} - 50, 250 - w_{1,i}) \ge 0$, which simplifies to $50 \le w_{1,i} \le 250$. This confines all four coordinates to an interval of length 200. The Dispersion condition requires $|w_{1,i} - w_{1,k}| \ge 100$ for all distinct pairs. It is mathematically impossible to place four points mutually separated by at least 100 within an interval of length 200. Thus, this subsystem is unsatisfiable, making `LOAD 1` a valid certificate.