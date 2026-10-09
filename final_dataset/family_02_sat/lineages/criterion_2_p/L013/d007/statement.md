# Dual-Manifold Chemical Routing

Time limit: 1 s   Memory limit: 256 MB

## Description
A chemical processing plant contains $n$ flow distributors. Each distributor $i$ ($1 \le i \le n$) is controlled by a binary toggle $s_i \in \{0, 1\}$.

The plant's safety system includes $m$ reaction detectors. Each detector samples exactly two manifolds across the plant. A detector's connection is specified by two non-zero integers $l_1$ and $l_2$. For any sampled manifold $l$:
- The absolute value $|l|$ identifies the distributor index from which it samples.
- The sign of $l$ dictates its baseline resonance. Let $\delta(l) = 1$ if $l < 0$, and $\delta(l) = 0$ if $l > 0$.

For a given configuration of toggles, the *phase index* $P(l)$ of a sampled manifold $l$ is calculated using the toggle state of its distributor and its baseline resonance:
$$P(l) = (-1)^{s_{|l|} + \delta(l)}$$

A detector will trigger a catastrophic shutdown if and only if the sum of the phase indices of its two sampled manifolds is strictly positive (i.e., $P(l_1) + P(l_2) > 0$). As long as this sum is less than or equal to zero, the detector remains dormant.

Your task is to determine whether there is a configuration of toggles $s_1, s_2, \dots, s_n$ such that all $m$ detectors remain dormant. If it is possible, you must provide the configuration. If no such configuration exists, report that the plant is unconfigurable.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of distributors and the number of detectors, respectively.

Each of the following $m$ lines contains two non-zero integers $l_1$ and $l_2$ ($1 \le |l_i| \le n$), detailing the two manifolds sampled by a single detector. The two manifolds sampled by a detector may belong to the same distributor, and may even be the exact same manifold.

## Output
If no valid configuration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{0, 1\}$) representing a valid configuration.

## Example 1
Input:
```
2 2
1 2
-1 -2
```
Output:
```
YES
1 0
```

## Example 2
Input:
```
1 2
1 1
-1 -1
```
Output:
```
NO
```

## Note
Multiple valid configurations may exist; any one of them is accepted. The same distributor may be sampled by multiple detectors.