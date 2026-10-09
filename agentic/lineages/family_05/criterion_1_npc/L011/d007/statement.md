# Problem A — Calibration Matrices

Time limit: 5 s   Memory limit: 256 MB

## Description

A satellite communications array requires the setup of a stable transmission network. The system has a capacity limit of **k** channels (where **k** is at most 22).

The engineering team has certified exactly **t** approved configurations. Each approved configuration is given as a triplet `(x, y, z)`, representing a channel utilizing frequency band **x**, modulation scheme **y**, and encryption key **z**. All values are integers between 1 and **k**. All listed configurations are distinct.

To finalize the network setup, you must select and deploy exactly **k** configurations from the approved list.

A deployed network is considered fully operational only if its interference signature equals the ideal harmonic across all three parameter types. The signature is calculated using powers of 10. Specifically, if you select **k** configurations $(x_1, y_1, z_1), (x_2, y_2, z_2), \dots, (x_k, y_k, z_k)$, the system's signatures are evaluated as follows:
- The frequency signature is $\sum_{i=1}^k 10^{x_i}$.
- The modulation signature is $\sum_{i=1}^k 10^{y_i}$.
- The encryption signature is $\sum_{i=1}^k 10^{z_i}$.

The ideal harmonic for a system of capacity **k** is defined as $H_k = \sum_{j=1}^k 10^j$.

A valid deployment of **k** configurations must satisfy all three of the following conditions simultaneously:
1. Its frequency signature exactly equals $H_k$.
2. Its modulation signature exactly equals $H_k$.
3. Its encryption signature exactly equals $H_k$.

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

In Example 2, $H_2 = 10^1 + 10^2 = 110$. If we select the only two available configurations, the modulation signature would be $10^1 + 10^1 = 20$. This does not equal the ideal harmonic $H_2 = 110$. Thus, a valid deployment is impossible.