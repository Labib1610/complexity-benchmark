# Problem C — Impossible Deadline: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

You are given a system of temporal constraints over a set of **j** signals. The system features exactly 2 sequential processing stages, numbered 1 and 2. 
Each signal $i$ (for $1 \le i \le j$) has a required duration defined by a matrix $D$, where $D_{i,1}$ is the duration in stage 1 and $D_{i,2}$ is the duration in stage 2.

We define the activation and deactivation times for each signal $i$ in each stage $c \in \{1, 2\}$ as non-negative real numbers $S_{i,c}$ and $E_{i,c}$.
A valid configuration must satisfy all of the following rules:
- **Duration constraint:** $E_{i,c} \ge S_{i,c} + D_{i,c}$ for all $i$ and all $c$.
- **Sequential stage constraint:** $S_{i,2} \ge E_{i,1}$ for all $i$.
- **Exclusivity constraint:** For a given stage $c$, no two signals can be processed concurrently. For any $i \neq k$, either $S_{i,c} \ge E_{k,c}$ or $S_{k,c} \ge E_{i,c}$.
- **Global deadline:** $E_{i,c} \le T$ for all $i$ and all $c$.

For every test input, it is guaranteed that no valid configuration exists. Your task is to output a short certificate that proves the system is contradictory. For every test input, exactly one of these certificate types is guaranteed to apply. Print the one that holds:

* `JOB i` (where **i** is a 1-based index): The constraints restricted only to signal **i** across both stages (Duration, Sequential, Non-negative activations, and Global deadline) are already contradictory. This certificate is valid exactly when the row sum $\sum_{c=1}^{2} D_{i,c} > T$.
* `LOAD c` (where **c** is either 1 or 2): The constraints restricted only to stage **c** across all signals (Duration, Exclusivity, Non-negative activations, and Global deadline) are already contradictory. This certificate is valid exactly when the column sum $\sum_{k=1}^{j} D_{k,c} > T$.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): representing $D_{i,1}$ and $D_{i,2}$ respectively for signal $i$.

## Output

Print a single line containing either `JOB i` (where the isolated constraints for signal **i** prove the deadline is impossible, meaning exactly $\sum_{c=1}^{2} D_{i,c} > T$) or `LOAD c` (where **c** is either 1 or 2, and the isolated constraints for stage **c** prove the deadline is impossible, meaning exactly $\sum_{k=1}^{j} D_{k,c} > T$).

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

In Example 1, `JOB 1` is the certificate because for signal 1, the duration and sequential constraints require $E_{1,2} \ge S_{1,2} + 60 \ge E_{1,1} + 60 \ge S_{1,1} + 70 + 60 \ge 130$. Since $S_{1,1} \ge 0$, $E_{1,2} \ge 130$, which contradicts the global deadline $E_{1,2} \le 100$. This matches the row sum condition $70 + 60 > 100$.
In Example 2, `LOAD 1` is the certificate because stage 1 has 4 signals each with duration 50. The exclusivity and duration constraints require the maximum $E_{i,1}$ to be at least $4 \times 50 = 200$, which contradicts the global deadline $E_{i,1} \le 150$. This matches the column sum condition for stage 1: $200 > 150$.