# Problem B — Polymer Frequency Tuning

Time limit: 1 s
Memory limit: 256 MB

A synthetic polymer consists of $n$ monomers, indexed from 1 to $n$. A tuning configuration assigns each monomer a specific frequency band, which is a continuous real interval. For each monomer, you must choose its frequency band to be either the interval $[0, 1]$ or the interval $[1, 2]$.

The laboratory maintains a record of $m$ covalent bonds between these monomers. To avoid destructive interference, the polymer must satisfy a local stability condition for every bond: for any recorded bond connecting monomer $u$ and monomer $v$, the frequency band assigned to $u$ and the frequency band assigned to $v$ must intersect at exactly one point. If their assigned bands overlap over a range of positive length, the polymer will destabilize. (Note that multiple records of the same bond, or a bond connecting a monomer to itself, must still strictly satisfy this condition without exception).

Your task is to determine a valid tuning configuration for all $n$ monomers. If multiple valid configurations exist, you must output the one that is lexicographically smallest when represented as a sequence of choices. Specifically, represent the choice of interval $[0, 1]$ as the integer 1, and the choice of interval $[1, 2]$ as the integer 2. The configuration is valid if it produces a sequence of $n$ integers $r_1, r_2, \dots, r_n$ (where each $r_i \in \{1, 2\}$) such that the sequence is lexicographically smaller than any other valid sequence. This means it must prioritize assigning 1 to monomer 1 if possible; then prioritize assigning 1 to monomer 2, and so on sequentially. 

If no configuration can satisfy the stability constraint for all $m$ recorded bonds, you must report the failure.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$, identifying a bonded pair of monomers in the record. Both monomer identifiers $u$ and $v$ are at least 1 and at most $n$.

## Output
If no tuning configuration can satisfy the stability constraint, output `NO` on a single line.
Otherwise, output `YES` on the first line. On the second line, output $n$ space-separated integers $r_1, r_2, \dots, r_n$ (where each $r_i \in \{1, 2\}$) representing the interval assigned to each respective monomer from 1 to $n$. This sequence must be the lexicographically smallest possible valid sequence.

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