# Problem A — Calibration Matrices

Time limit: 5 s   Memory limit: 256 MB

## Description

A satellite communications array requires the setup of a stable transmission network. The system has a capacity limit of **k** channels (where **k** is at most 22).

The engineering team has certified exactly **t** approved configurations. Each approved configuration is given as a triplet `(x, y, z)`, representing a channel utilizing frequency band **x**, modulation scheme **y**, and encryption key **z**. All values are integers between 1 and **k**. All listed configurations are distinct.

To finalize the network setup, you must select and deploy exactly **k** configurations from the approved list.

A deployed network is considered fully operational only if its resonance levels match the baseline threshold across all three parameter types. The resonance is calculated using powers of 2. Specifically, if you select **k** configurations $(x_1, y_1, z_1), (x_2, y_2, z_2), \dots, (x_k, y_k, z_k)$, the system's resonance levels are evaluated as follows:
- The frequency resonance is $\sum_{i=1}^k 2^{x_i}$.
- The modulation resonance is $\sum_{i=1}^k 2^{y_i}$.
- The encryption resonance is $\sum_{i=1}^k 2^{z_i}$.

The baseline threshold for a system of capacity **k** is defined as $B_k = \sum_{j=1}^k 2^j$.

A valid deployment of **k** configurations must satisfy all three of the following conditions simultaneously:
1. Its frequency resonance exactly equals $B_k$.
2. Its modulation resonance exactly equals $B_k$.
3. Its encryption resonance exactly equals $B_k$.

Determine whether it is possible to deploy exactly **k** approved configurations that meet these criteria. If a valid set exists, provide it.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the capacity limit and the total number of approved configurations.
Each of the following **t** lines provides three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing an approved configuration utilizing frequency band **x**, modulation scheme **y**, and encryption key **z**. All listed configurations are distinct.

## Output

If a valid deployment of **k** configurations can be formed, print `YES` on the first line. Then, output **k** lines, each containing the three integers `x y z` of one selected configuration. Any valid deployment of **k** configurations is accepted; the chosen configurations may be printed in any order.

If no such deployment is possible, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 2 2
2 2 2
```

**Output**
```
YES
1 1 1
2 2 2
```

### Example 2

**Input**
```
2 2
1 1 1
2 1 2
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1
1 1 1
```

**Output**
```
YES
1 1 1
```

## Note

In Example 2, $B_2 = 2^1 + 2^2 = 6$. If we select the only two available configurations, the modulation resonance would be $2^1 + 2^1 = 4$. This does not equal the baseline threshold $B_2 = 6$. Thus, a valid deployment is impossible.