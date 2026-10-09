# Problem C — Impossible Domains: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A digital signal processing system must synthesize $2j$ rectangular pulses over a continuous time domain. Let $P(t; k, W)$ denote a rectangular pulse of width $W$ starting at time $k$. Formally, $P(t; k, W) = 1$ for $t \in [k, k+W]$ and $P(t; k, W) = 0$ otherwise.

For each item $i \in \{1 \dots j\}$, the system must determine real-valued start times $k_{i,1}$ and $k_{i,2}$ to define two signal components:
- Component 1: $s_{i,1}(t) = P(t; k_{i,1}, p_{i,1})$
- Component 2: $s_{i,2}(t) = P(t; k_{i,2}, p_{i,2})$

The synthesized signals must strictly satisfy three constraints:
1. **Bounded Support:** For all $i \in \{1 \dots j\}$ and $c \in \{1, 2\}$, the signal $s_{i,c}(t)$ must be exactly zero for all $t < 0$ and all $t > T$.
2. **Non-negative Lag:** For every item $i$, the continuous cross-correlation between its two components must evaluate to zero for all strictly negative lags. That is, $R_i(\tau) = \int_{-\infty}^{\infty} s_{i,1}(t) s_{i,2}(t + \tau) dt = 0$ for all $\tau < 0$.
3. **Orthogonal Multiplexing:** For a fixed component $c$ (where $c \in \{1, 2\}$), the signals across all $j$ items must be pairwise orthogonal. That is, for any distinct items $i \neq m$, the inner product $\int_{-\infty}^{\infty} s_{i,c}(t) s_{m,c}(t) dt = 0$.

You are analyzing logs from failed systems where a valid complete assignment of start times is mathematically impossible. For every provided test case, exactly one of the following isolated conditions is inherently impossible to satisfy. Output the code for the one that applies:
- `JOB i` — It is mathematically impossible to find start times $k_{i,1}$ and $k_{i,2}$ such that the signals for item **i** (1-indexed) simultaneously satisfy Bounded Support and Non-negative Lag, even if we completely ignore Orthogonal Multiplexing and all other items.
- `LOAD c` — It is mathematically impossible to find start times $k_{1,c}, \dots, k_{j,c}$ such that the signals for component **c** (where **c** $\in \{1, 2\}$) simultaneously satisfy Bounded Support and Orthogonal Multiplexing, even if we completely ignore Non-negative Lag and the other component.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the following **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the required pulse widths $p_{i,1}$ and $p_{i,2}$ for component 1 and component 2 of the item, respectively.

## Output

Print a single line containing the applicable certificate: either `JOB i` or `LOAD c`.

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