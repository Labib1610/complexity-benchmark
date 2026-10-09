# Problem C — Signal Transmission Scheduling

Time limit: 2 s   Memory limit: 256 MB

## Description

A signal processing system must schedule a set of $j$ independent processes within a continuous transmission window of duration $T$, extending from time $0$ to time $T$.

Each process $k \in \{1 \dots j\}$ consists of an alpha burst of duration $p1_k$ and a beta burst of duration $p2_k$. 

To place these bursts on the timeline, the scheduler must assign a real-valued central timestamp $x_k$ for the alpha burst and a real-valued central timestamp $y_k$ for the beta burst. Consequently, the alpha burst occupies the continuous interval $[x_k - p1_k/2, x_k + p1_k/2]$, and the beta burst occupies the continuous interval $[y_k - p2_k/2, y_k + p2_k/2]$.

A schedule is valid if and only if it satisfies all of the following spatial and temporal constraints:

1. **Alpha Confinement:** For all $k \in \{1 \dots j\}$, the alpha burst must be positioned entirely within the transmission window. Thus, $x_k - p1_k/2 \ge 0$ and $x_k + p1_k/2 \le T$.
2. **Beta Confinement:** For all $k \in \{1 \dots j\}$, the beta burst must be positioned entirely within the transmission window. Thus, $y_k - p2_k/2 \ge 0$ and $y_k + p2_k/2 \le T$.
3. **Phase Sequence:** For all $k \in \{1 \dots j\}$, the alpha burst must conclude before the beta burst begins. Thus, $x_k + p1_k/2 \le y_k - p2_k/2$.
4. **Alpha Exclusivity:** For any two distinct processes $u$ and $v$ in $\{1 \dots j\}$, their alpha bursts must not overlap. Thus, $|x_u - x_v| \ge \frac{p1_u + p1_v}{2}$.
5. **Beta Exclusivity:** For any two distinct processes $u$ and $v$ in $\{1 \dots j\}$, their beta bursts must not overlap. Thus, $|y_u - y_v| \ge \frac{p2_u + p2_v}{2}$.

The system has determined that no valid schedule exists for the current batch of processes. You must output a diagnostic code identifying the isolated source of this impossibility. 

The input data is guaranteed to trigger exactly one of the following isolated contradictions. Print the corresponding code:
- `JOB i` (where $i$ is the 1-based index of the process): It is mathematically impossible to assign timestamps $x_i$ and $y_i$ for process $i$ to simultaneously satisfy Constraints 1, 2, and 3 (assuming all other processes are ignored and Constraints 4 and 5 are lifted). If multiple processes satisfy this, you may output the code for any such process.
- `LOAD 1`: It is mathematically impossible to assign timestamps $x_1 \dots x_j$ for all $j$ processes to simultaneously satisfy Constraints 1 and 4 (assuming Constraints 2, 3, and 5 are lifted).
- `LOAD 2`: It is mathematically impossible to assign timestamps $y_1 \dots y_j$ for all $j$ processes to simultaneously satisfy Constraints 2 and 5 (assuming Constraints 1, 3, and 4 are lifted).

## Input

The first line contains two integers $j$ and $T$ ($1 \le j \le 200000$, $1 \le T \le 1000000000$).
Each of the next $j$ lines contains two integers $p1$ and $p2$ ($1 \le p1, p2 \le 1000000$): the durations of the alpha and beta bursts for that process.

## Output

Print a single line containing the valid diagnostic code (`JOB i`, `LOAD 1`, or `LOAD 2`).

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

In Example 1, `JOB 1` is triggered because process 1 requires an alpha burst of duration 70 and a beta burst of duration 60. Constraint 3 requires $x_1 + 35 \le y_1 - 30$. Rearranging gives $y_1 - x_1 \ge 65$. Constraints 1 and 2 require $x_1 \ge 35$ and $y_1 \le 100 - 30 = 70$. This implies the maximum possible difference $y_1 - x_1$ is $70 - 35 = 35$, which contradicts the requirement of $65$. Thus, it is impossible to satisfy Constraints 1, 2, and 3 for process 1.

In Example 2, `LOAD 1` is triggered because there are four alpha bursts, each of duration 50. Constraint 4 requires that the distance between any two alpha central timestamps $x_u$ and $x_v$ is at least 50. This means the four timestamps must span a distance of at least $3 \times 50 = 150$ between the first and last center. However, Constraint 1 restricts all $x_k$ to the range $[25, 125]$, which has a maximum span of $100$. This forms a direct contradiction, making it impossible to satisfy Constraints 1 and 4 simultaneously.