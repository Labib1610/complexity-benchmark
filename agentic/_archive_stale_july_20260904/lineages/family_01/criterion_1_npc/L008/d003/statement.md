# Problem A — Assembly Tolerances

Time limit: 2 s   Memory limit: 256 MB

A high-tech manufacturing plant is preparing $n$ precision-machined elements for final integration into a single mechanism. Before they can be integrated, each element requires exactly one of three available chemical barrier coatings, labeled 1, 2, and 3.

Within the mechanism, certain pairs of elements are designed to be in direct physical contact. If any two contacting elements are treated with the identical barrier coating, their shared chemical makeup will induce a catastrophic polymer fusion. This fusion locks the mechanism and renders the entire unit defective. Consequently, no two contacting elements can ever be treated with the same coating.

The plant's automated verification suite intentionally evaluates your logic against adversarial testing configurations on the full 40 elements. These include closely constrained and fundamentally incompatible layouts, engineered specifically to cause fixed-order, coating-by-coating trial-and-error approaches to exceed the time limit.

You must determine whether a non-reactive coating configuration exists for the given mechanism.

## Input
The first line provides two integers $n$ and $m$ — the total number of elements and the number of contact pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), signifying that element $u$ and element $v$ are in direct physical contact.

## Output
If there is no way to coat the elements without inducing polymer fusion, output a single line containing `NO`.
If a non-reactive configuration is achievable, output `YES` on the first line. On the second line, provide $n$ integers $s_1 s_2 \dots s_n$ ($s_i \in \{1, 2, 3\}$), where $s_i$ represents the coating applied to element $i$. If multiple non-reactive configurations exist, you must output the one that is lexicographically smallest (comparing the coating of element 1 first, then element 2, and so on).

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```