# Personnel Deployment Tiers

Time limit: 2 s   Memory limit: 256 MB

A corporation is restructuring its workforce of $n$ personnel, who are assigned numerical identifiers from 1 to $n$. The daily operational protocol mandates that each individual is assigned to exactly one deployment tier. The available tier designations are 1, 2, and 3.

During field tests, it was discovered that certain pairs of personnel interfere with each other if operating in the same tier. You are given a compatibility registry. Each entry in the registry specifies two personnel who must not share a tier.

A valid deployment must satisfy the following condition: for every entry in the compatibility registry, the tier designation assigned to the first person and the tier designation assigned to the second person must be strictly unequal.

To ensure computational predictability, the registry is guaranteed to exhibit the following administrative bounds:
- For any single entry in the registry, the absolute difference between the numerical identifiers of the two personnel is strictly less than $n$.
- The total sum of all personnel numerical identifiers evaluated across every entry in the entire registry is strictly less than $n^3 + 1$.

You must determine whether a valid deployment exists for all $n$ personnel. If multiple valid deployments are possible, you must resolve the ambiguity using a sequential prioritization process:
1. From the set of all valid deployments, filter down to those that assign the smallest possible tier designation to person 1.
2. If multiple deployments remain, filter those to minimize the tier designation for person 2.
3. Continue this sequential filtering for person 3, person 4, and so on, until exactly one deployment remains.

## Input
The first line contains two integers $n$ and $m$ — the number of personnel and the number of registry entries ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the numerical identifiers of the personnel in a registry entry.

## Output
If no deployment can satisfy all conditions, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the tier designation assigned to person $i$. If there are multiple valid deployments, output the single deployment determined by the sequential prioritization process.

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
