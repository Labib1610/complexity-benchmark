# Problem C — Cargo Prohibition Protocol

Time limit: 2 s   Memory limit: 256 MB

A logistics firm operates a shipping route for hazardous materials. Certain pairs of these materials are highly reactive and are strictly prohibited from sharing a vessel.

The proposed loading schedule is structurally impossible to fulfill. You must produce a definitive proof of this impossibility to trigger an automatic schedule rejection.

To establish this proof, you are required to isolate a "deadlock" configuration consisting of exactly three distinct materials. A configuration of three materials is deemed a deadlock if and only if they cannot be safely transported by a standard dual-hold cargo ship. Specifically, if you were to consider just those three materials, it must be impossible to assign each of them to either Hold A or Hold B such that neither hold ends up containing a prohibited pair.

Because the automated auditing system requires deterministic reporting, it will not accept an arbitrary deadlock configuration. The system demands the canonical proof, meaning you must systematically ensure no earlier configuration could have been reported.

## Input
The first line provides two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), indicating the number of hazardous materials and the number of prohibited pairs. The materials are identified by integers from $1$ to $n$.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$) — a pair of materials that are prohibited from sharing a vessel. 
It is guaranteed that the input contains at least one deadlock configuration of three materials.

## Output
Output a single line containing three integers $a$, $b$, and $c$ ($a < b < c$), representing the identifiers of the materials in the deadlock configuration.
To satisfy the deterministic auditing system, if more than one such configuration exists, you must output the lexicographically earliest one among all valid configurations. This means you must minimize $a$; if there is a tie, minimize $b$; and if still tied, minimize $c$.

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