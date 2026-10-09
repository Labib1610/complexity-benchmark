# SLA Rejection Certificate

Time limit: 2 s   Memory limit: 256 MB

## Description

A cloud computing platform processes a sequence of $j$ client requests. The system tracks its cumulative load $S$ and its processing backlog $D$. Initially, $S = 0$ and $D = 0$.

When a request with parameters $u$ and $v$ is processed, the system updates its state as follows:
- The cumulative load increases by $u$:
  $S_{new} = S + u$
- The backlog is reduced by $u$ (but cannot fall below zero), and then increases by $v$:
  $D_{new} = \max(0, D - u) + v$

The state is updated to $(S_{new}, D_{new})$. After all $j$ requests are processed in order, the final evaluation metric of the sequence is $S + D$. The client requires this final metric to be at most $T$.

For every input provided, it is impossible to meet this deadline. The input guarantees that exactly one of the two following limitation categories applies. You must print a short rejection certificate from the applicable category:

- **Isolated Job Obstruction:** There is a request $i$ ($1 \le i \le j$) such that if we were to construct a hypothetical sequence where the $i$-th request uses its actual parameters $u = p_{1, i}$ and $v = p_{2, i}$, but every other request $k \neq i$ is replaced by a dummy request with parameters $u = 0$ and $v = 0$, the final metric $S + D$ of this $j$-step sequence would strictly exceed $T$. If this category applies, print `JOB i`. (If multiple requests satisfy this, printing any one of them is acceptable).

- **Continuous Utilization Exhaustion:** There is a component $c \in \{1, 2\}$ such that if we were to construct a hypothetical sequence where the parameters for the *other* component are zeroed out across all requests, the final metric $S + D$ would strictly exceed $T$. Specifically:
  - If $c = 1$, we use $u = p_{1, k}$ and $v = 0$ for all $k$.
  - If $c = 2$, we use $u = 0$ and $v = p_{2, k}$ for all $k$.
  If this category applies, print `LOAD c`. (If both satisfy this, either is acceptable).

Output must be consistent with the unique applicable limitation category guaranteed by the input.

## Input

The first line contains two integers $j$ and $T$ ($1 \le j \le 200000$, $1 \le T \le 1000000000$).
Each of the next $j$ lines contains two integers $p_1$ and $p_2$ ($1 \le p_1, p_2 \le 1000000$): the parameters for component 1 and component 2 of a request, respectively.

## Output

Print a single line containing either `JOB i` or `LOAD c`. The output must be consistent with the unique applicable limitation category guaranteed by the input.

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

In Example 1, consider the hypothetical sequence for request 1 where requests 2 and 3 are dummy requests:
The modified sequence of parameters is $(70, 60)$, $(0, 0)$, $(0, 0)$.
Starting at $S = 0, D = 0$:
Step 1: $u=70, v=60$. $S = 0 + 70 = 70$. $D = \max(0, 0 - 70) + 60 = 60$.
Step 2: $u=0, v=0$. $S = 70 + 0 = 70$. $D = \max(0, 60 - 0) + 0 = 60$.
Step 3: $u=0, v=0$. $S = 70 + 0 = 70$. $D = \max(0, 60 - 0) + 0 = 60$.
The final metric is $S + D = 70 + 60 = 130$. Since $130 > 100$, `JOB 1` is a valid rejection certificate.

In Example 2, consider the hypothetical sequence for component 1 where all component 2 parameters are 0:
The modified sequence of parameters uses $u = p_{1, k}$ and $v = 0$ for all 4 steps.
Step 1: $u=50, v=0$. $S = 50$, $D = \max(0, 0 - 50) + 0 = 0$.
Step 2: $u=50, v=0$. $S = 100$, $D = \max(0, 0 - 50) + 0 = 0$.
Step 3: $u=50, v=0$. $S = 150$, $D = \max(0, 0 - 50) + 0 = 0$.
Step 4: $u=50, v=0$. $S = 200$, $D = \max(0, 0 - 50) + 0 = 0$.
The final metric is $S + D = 200 + 0 = 200$. Since $200 > 150$, `LOAD 1` is a valid rejection certificate.