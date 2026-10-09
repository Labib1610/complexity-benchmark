# SLA Rejection Certificate

Time limit: 2 s   Memory limit: 256 MB

## Description
A data processing pipeline applies a sequence of $j$ transformations to a state vector. The state is represented as a pair of integers $(u, v)$. The initial state before any transformations is $(0, 0)$.

For each step $k$ (where $1 \le k \le j$), the pipeline applies a transformation $f_k$ to the current state. The transformation is parameterized by two integers $p_{1,k}$ and $p_{2,k}$, and is defined as follows:
$$f_k(u, v) = (u + p_{1,k}, \max(u + p_{1,k} + p_{2,k}, v + p_{2,k}))$$

The final state after all $j$ steps are applied sequentially is $(U, V) = f_j(f_{j-1}(\dots f_1(0, 0)\dots))$.
The system's service level agreement (SLA) requires that the final second coordinate satisfies $V \le T$.

For every input provided to your program, it is impossible to meet this SLA. The input guarantees that the failure is caused by exactly one of the two structural reasons below. You must print a short rejection certificate identifying a valid witness from the applicable category.

- **Type A (Isolated):** There is an index $i$ ($1 \le i \le j$) such that if we replace the transformation $f_k$ with the identity transformation $\text{id}(u, v) = (u, v)$ for every step $k \neq i$ (leaving $f_i$ unchanged), the final second coordinate strictly exceeds $T$.
  If this category applies, print `JOB i`.

- **Type B (Accumulated):** There is a component $c \in \{1, 2\}$ such that:
  - If $c = 1$, we replace the transformation $f_k$ at every step with $g_k(u, v) = (u + p_{1,k}, \max(u + p_{1,k}, v))$.
  - If $c = 2$, we replace the transformation $f_k$ at every step with $h_k(u, v) = (u, \max(u + p_{2,k}, v + p_{2,k}))$.
  If the final second coordinate under the $c$-th replacement strictly exceeds $T$, print `LOAD c`.

**Uniqueness and Multiplicity:** For every input, exactly one of the two categories is guaranteed to hold. However, within that category, there may be multiple valid witnesses (e.g., multiple indices $i$ that individually exceed $T$, or both $c=1$ and $c=2$ exceeding $T$). Outputting any one valid witness from the applicable category is strictly acceptable.

## Input
The first line contains two integers $j$ and $T$ ($1 \le j \le 200000$, $1 \le T \le 1000000000$).
Each of the next $j$ lines contains two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$): the parameters for the $k$-th transformation.

## Output
Print a single line containing either `JOB i` or `LOAD c`. The output must be a valid witness from the unique applicable category guaranteed by the input.

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
In Example 1, consider the Type A substitution for index 1:
The sequence of transformations is $f_1$, then $\text{id}$, then $\text{id}$.
Start at $(0, 0)$.
Step 1: $f_1(0, 0) = (0 + 70, \max(0 + 70 + 60, 0 + 60)) = (70, 130)$.
Step 2: $\text{id}(70, 130) = (70, 130)$.
Step 3: $\text{id}(70, 130) = (70, 130)$.
The final second coordinate is $130$. Since $130 > 100$, `JOB 1` is a valid rejection certificate.

In Example 2, consider the Type B substitution for $c = 1$:
The sequence of transformations uses $g_k(u, v) = (u + p_{1,k}, \max(u + p_{1,k}, v))$.
Start at $(0, 0)$.
Step 1: $g_1(0, 0) = (50, \max(50, 0)) = (50, 50)$.
Step 2: $g_2(50, 50) = (100, \max(100, 50)) = (100, 100)$.
Step 3: $g_3(100, 100) = (150, \max(150, 100)) = (150, 150)$.
Step 4: $g_4(150, 150) = (200, \max(200, 150)) = (200, 200)$.
The final second coordinate is $200$. Since $200 > 150$, `LOAD 1` is a valid rejection certificate.