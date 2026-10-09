# Problem B — Isotope Stabilization Process

Time limit: 2 s
Memory limit: 256 MB

## Description
An industrial processing plant needs to stabilize a batch of volatile isotopes. The batch contains $q$ Alpha-type isotopes and $q$ Beta-type isotopes. Alpha-type isotopes are assigned unique integer identifiers from $1$ to $q$. Beta-type isotopes are assigned unique integer identifiers from $q+1$ to $2q$.

To achieve stabilization, the plant must pair one Alpha-type isotope with one Beta-type isotope. However, not all pairings are stable. The plant's researchers have compiled a registry of $t$ stable pairs. Any pair not in this registry will result in a failure. The registry might list the same stable pair multiple times; such duplicates do not affect stability.

You must determine if it is possible to select exactly $q$ pairs from the registry to achieve a total stabilization. A valid stabilization plan must simultaneously satisfy all of the following conditions:
- Every Alpha-type isotope is used in exactly one selected pair.
- Every Beta-type isotope is used in exactly one selected pair.
- For every selected pair $(a, b)$ where $a$ is the Alpha-type and $b$ is the Beta-type, the difference in their identifiers must be strictly positive ($b - a > 0$).
- The sum of the Alpha-type identifiers across all $q$ selected pairs must equal exactly $\frac{q(q+1)}{2}$.
- The sum of the Beta-type identifiers across all $q$ selected pairs must equal exactly $\frac{q(3q+1)}{2}$.

Determine if the registry allows for such a total stabilization. If it does, output one valid configuration of $q$ pairs; otherwise, report that it is impossible.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of Alpha-type isotopes (which is also the number of Beta-type isotopes) and the total number of stable pairs in the registry.
The next $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating that Alpha-type isotope $a$ can be safely paired with Beta-type isotope $b$.

## Output
If a valid stabilization plan is possible, print `YES` followed by $q$ lines, each containing the two identifiers of a chosen pair. If it is impossible, print `NO`.

## Example 1

### Input
3 4
1 4
1 5
2 6
3 5

### Output
YES
1 4
3 5
2 6

## Example 2

### Input
2 2
1 3
2 3

### Output
NO
