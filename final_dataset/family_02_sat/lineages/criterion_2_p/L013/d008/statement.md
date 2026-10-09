# Dual-Manifold Chemical Routing

Time limit: 1 s   Memory limit: 256 MB

## Description
A chemical processing plant contains $n$ flow distributors. Each distributor $i$ ($1 \le i \le n$) is controlled by a binary toggle $s_i \in \{0, 1\}$.

The toggle determines the specific isotope produced by the distributor:
- Setting $s_i = 1$ causes it to produce Isotope-1.
- Setting $s_i = 0$ causes it to produce Isotope-0.

The plant's safety system includes $m$ reaction detectors. Each detector samples exactly two manifolds across the plant. A detector's connection is specified by two non-zero integers $l_1$ and $l_2$. For any sampled manifold $l$:
- The absolute value $|l|$ identifies the distributor index from which it draws fluid.
- The sign of $l$ dictates its filtration process before reaching the detector:
  - If $l > 0$, the manifold is a direct line. The isotope produced by the distributor flows unchanged.
  - If $l < 0$, the manifold is a transmuting line. It converts Isotope-1 into Isotope-0, and Isotope-0 into Isotope-1.

Inside each detector, the fluids from its two sampled manifolds are combined in a mixing chamber. The mixing chamber will therefore hold a mixture comprising the isotope delivered by the first manifold and the isotope delivered by the second manifold.

A detector will trigger a catastrophic shutdown if and only if the resulting mixture in its chamber contains Isotope-0 and is completely devoid of Isotope-1. If this specific condition is not met, the detector remains dormant.

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