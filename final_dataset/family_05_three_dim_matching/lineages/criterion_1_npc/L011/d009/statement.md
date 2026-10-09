# Problem A — Calibration Matrices

Time limit: 5 s   Memory limit: 256 MB

## Description

A satellite communications array requires the setup of a stable transmission network. The system has a capacity limit of **k** channels (where **k** is at most 22).

The engineering team has certified exactly **t** approved configurations. Each approved configuration is given as a triplet `(x, y, z)`, representing a channel utilizing frequency band **x**, modulation scheme **y**, and encryption key **z**. All values are integers between 1 and **k**. All listed configurations are distinct.

To finalize the network setup, you must select and deploy exactly **k** configurations from the approved list.

A deployed network is considered fully operational only if its parameter matrices are non-singular. Specifically, if you select **k** configurations, let $x_1, x_2, \dots, x_k$ be their frequency bands. You must construct a $k \times k$ matrix $F$ where the entry in the $i$-th row and $j$-th column is $(x_i)^{j-1}$ (using 1-based indexing for rows and columns, and defining $x^0 = 1$ for all $x$). The frequency bands are considered stable if and only if the determinant of $F$ is non-zero.

The exact same stability requirement applies independently to the modulation schemes and the encryption keys. You must construct a $k \times k$ matrix $M$ from the modulation schemes $y_1, y_2, \dots, y_k$ (where $M_{i,j} = (y_i)^{j-1}$) and a $k \times k$ matrix $E$ from the encryption keys $z_1, z_2, \dots, z_k$ (where $E_{i,j} = (z_i)^{j-1}$). The determinants of $M$ and $E$ must also be non-zero.

Determine whether it is possible to deploy exactly **k** approved configurations such that the matrices $F$, $M$, and $E$ all have non-zero determinants. If a valid set exists, provide it.

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

In Example 2, if we select the only two available configurations, their modulation schemes are $y_1 = 1$ and $y_2 = 1$. The corresponding $2 \times 2$ matrix $M$ will have two identical rows, `[1, 1]` and `[1, 1]`. The determinant of this matrix is 0. Because a valid deployment requires the determinant to be non-zero, this deployment is impossible.