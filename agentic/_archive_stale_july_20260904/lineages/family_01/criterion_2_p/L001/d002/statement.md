# Problem B — Monomer Spin States

Time limit: 1 s   Memory limit: 256 MB

A synthetic polymer consists of $n$ monomers, identified by integers from 1 up to $n$. A synthesis configuration assigns each monomer a spin state, which is an integer value of either 1 or 2.

The laboratory maintains a record of $m$ covalent bonds. To ensure molecular stability, the protocol enforces a strict parity rule for any pair of monomers listed in the record: when the assigned spin states of the two monomers in a bonded pair are added together, the resulting sum must be exactly 3.

Your task is to determine a valid synthesis configuration for all $n$ monomers. If multiple valid configurations exist, you must provide the one that is lexicographically smallest. If it is impossible to satisfy the parity rule for all bonded pairs simultaneously, you must report the failure.

## Input
The first line provides two integers $n$ and $m$. The polymer requires a minimum of $1$ monomer and has a maximum capacity of $2 \cdot 10^5$ monomers. The bond record can contain as few as $0$ entries or up to a maximum of $2 \cdot 10^5$ entries, represented by $m$.
Each of the following $m$ lines contains two integers $u$ and $v$, identifying a pair of monomers in the record. Both monomer identifiers $u$ and $v$ are at least $1$ and at most $n$.

## Output
If no valid synthesis configuration exists, output `NO` on a single line.
Otherwise, output `YES` on the first line. On the second line, output $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$) representing the spin state assigned to each respective monomer from 1 to $n$. This sequence must be the lexicographically smallest possible valid sequence.

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