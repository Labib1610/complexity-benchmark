# Problem C — Automated Audit Evidence Extraction

Time limit: 2 s   Memory limit: 256 MB

Our logistics platform processes shipments of industrial chemicals. Because some chemicals are highly reactive when stored in the same environment, they must be separated. Currently, our fleet consists of exactly two transport vessels. 

The daily scheduling pipeline consists of four sequential execution phases:
1. **Ingestion:** The system parses the manifest of $n$ chemicals and a list of $m$ known reactive pairs.
2. **Allocation:** A scheduler attempts to safely distribute all chemicals between the two vessels. 
3. **Evidence Extraction:** If the scheduler fails, it triggers a diagnostic routine to isolate the root cause.
4. **Reporting:** The isolated cause is formatted into a regulatory rejection ticket.

You are responsible for implementing Phase 3. The scheduler (Phase 2) has already aborted and determined that a safe two-vessel distribution is impossible for the given manifest. To satisfy the reporting requirements of Phase 4, you must extract a minimal proof of this impossibility. 

Specifically, you must find a group of exactly three chemicals that are mutually incompatible—meaning each chemical in the group reacts dangerously with the other two. Because they all conflict with each other, they would require at least three vessels, which serves as a formal proof that the two-vessel limit cannot be met.

You do not need to parse the original manifest formats or generate the final PDF report; your module will receive the raw conflict data directly from Phase 1. Your program must simply locate the three mutually reactive chemicals. 

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the number of chemicals and the number of reactive pairs. Chemicals are assigned integer IDs from $1$ to $n$.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that chemical $u$ and chemical $v$ react dangerously. 
The input data is guaranteed to represent a failed manifest containing at least one such group of three mutually reactive chemicals.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, with $a < b < c$. These are the IDs of the three chemicals forming the proof.
To ensure the Reporting phase behaves deterministically, if multiple valid groups of three exist, you must output the group that is lexicographically smallest. (This means selecting the group with the smallest value for $a$; if tied, the smallest value for $b$; and if still tied, the smallest value for $c$).

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
