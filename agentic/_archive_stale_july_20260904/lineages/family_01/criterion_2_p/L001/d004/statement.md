# Problem B — Polymer Resonance Tuning

Time limit: 1 s
Memory limit: 256 MB

A synthetic polymer consists of $n$ monomers, indexed from 1 to $n$. A tuning configuration assigns each monomer a resonance level, which must be chosen as either 1 or 2.

The laboratory maintains a record of $m$ covalent bonds between these monomers. To ensure molecular stability, a strict structural rule applies to any pair of monomers connected by a documented bond. For every recorded bonded pair of monomers $u$ and $v$, the configuration must satisfy two conditions simultaneously:
- Monomers $u$ and $v$ cannot both be assigned resonance level 1.
- Monomers $u$ and $v$ cannot both be assigned resonance level 2.

Your task is to determine a valid tuning configuration for all $n$ monomers. If multiple valid configurations exist, you must output the sequence of resonance levels that is lexicographically smallest. This means the configuration must prioritize assigning level 1 to monomer 1 if any valid configuration allows it; then, among those valid configurations, prioritize assigning level 1 to monomer 2, and so on sequentially up to monomer $n$. If no configuration can satisfy the structural rule for all recorded bonds simultaneously, you must report the failure.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$, identifying a bonded pair of monomers in the record. Both monomer identifiers $u$ and $v$ are at least 1 and at most $n$.

## Output
If no valid tuning configuration exists, output `NO` on a single line.
Otherwise, output `YES` on the first line. On the second line, output $n$ space-separated integers $r_1, r_2, \dots, r_n$ (where each $r_i \in \{1, 2\}$) representing the resonance level assigned to each respective monomer from 1 to $n$. This sequence must be the lexicographically smallest possible valid sequence.

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