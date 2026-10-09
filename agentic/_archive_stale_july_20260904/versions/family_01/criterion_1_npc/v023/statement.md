# Problem A — Vault Segregation

Time limit: 2 s   Memory limit: 256 MB

A research facility is organizing its inventory of chemical compounds. Every compound must be securely placed into exactly one of three climate-controlled vaults, designated as Vault 1, Vault 2, and Vault 3. 

Because of their volatile nature, certain pairs of compounds are strictly incompatible and will cause a dangerous reaction if placed in the same vault. Your task is to determine if it is possible to assign every compound to one of the three vaults such that no two incompatible compounds are placed together.

If a safe arrangement is possible, you must find a valid assignment for all compounds. To maintain standardized cataloging across the facility, if there are multiple safe arrangements, you must provide the one that is lexicographically smallest. That is, when the assigned vault numbers (1, 2, or 3) are listed as a sequence ordered by compound ID from 1 to $n$, the sequence should be as small as possible.

## Input
The first line of the manifest contains two integers, $n$ and $m$.
The number of compounds, $n$, is at least 1 and at most the total number of cells in an 8-by-5 grid.
The number of incompatible pairs, $m$, is non-negative and will not exceed the total number of unique two-compound combinations possible from $n$ items.
Each of the next $m$ lines contains two integers $u$ and $v$ — the IDs of two compounds that are incompatible. Compounds are identified by integers from 1 to $n$.

## Output
If there is no way to safely distribute the compounds across the three vaults, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $v_1, v_2, \dots, v_n$ (each being 1, 2, or 3), where $v_i$ represents the vault assigned to compound $i$. Among all valid assignments, output the one that produces the lexicographically smallest sequence of vault numbers.

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
