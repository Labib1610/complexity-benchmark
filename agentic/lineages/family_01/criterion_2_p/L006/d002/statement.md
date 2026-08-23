# Fragrance Formulation

Time limit: 1 s   Memory limit: 256 MB

A master perfumer is creating two distinct signature fragrances, Formulation 1 and Formulation 2. The laboratory contains $n$ essential extracts, labeled from 1 to $n$. Every extract must be utilized in exactly one of the two formulations.

Because of chemical volatility, certain extracts will neutralize each other if they are combined in the same fragrance. The perfumer has documented $m$ such volatile pairs that cannot be placed in the same formulation.

You must determine whether it is possible to separate the extracts into the two formulations without combining any volatile pair. In cases where more than one valid separation exists, the laboratory evaluates the assignment by concatenating the sequence of choices $f_1, f_2, \dots, f_n$ to form a single $n$-digit integer (where each digit $f_i$ is either 1 or 2). Your objective is to find the valid assignment that minimizes the value of this integer. If it is impossible to separate the extracts safely, the entire batch must be discarded.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
The next $m$ lines each contain two integers $u$ and $v$ — a volatile pair of extracts that must be kept in separate formulations.

## Output
If no valid separation exists, output a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $f_1, f_2, \dots, f_n$ (where each $f_i \in \{1, 2\}$) representing the formulation assigned to each extract in the separation that minimizes the $n$-digit integer described above.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```