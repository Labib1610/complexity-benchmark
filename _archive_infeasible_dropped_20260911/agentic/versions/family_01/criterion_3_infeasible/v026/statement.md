# Problem C — Manifest Impossibility

Time limit: 2 s   Memory limit: 256 MB

The shipping company transports $n$ distinct types of cargo, numbered 1 through $n$. Certain pairs of cargo types are incompatible and will react dangerously if placed on the same vessel. The company only operates two vessels, but the current shipping manifest is known to be impossible to fulfill safely.

Your task is not to attempt to safely divide the cargo—it is to certify the impossibility of doing so. It is guaranteed that the manifest contains at least one set of three cargo types that are all mutually incompatible with one another. Any such trio proves that two vessels cannot suffice, as at least two of the three would inevitably have to share a vessel. You must output one such trio.

The number of cargo types $n$ is at least 3 (the minimum needed to form a trio). The maximum number of cargo types the company's database can register is exactly equal to the number of kilograms in two metric tonnes.

The number of incompatible pairs $m$ is at least 3. The system can record up to a maximum of one-fifth of a million incompatible pairs, or the total number of distinct possible pairs among the $n$ cargo types, whichever is smaller.

## Input
The first line contains two integers $n$ and $m$.
Each of the next $m$ lines contains two integers $u$ and $v$, representing an incompatible pair of cargo types.
It is guaranteed that at least one mutually incompatible trio exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ such that all three pairs ($a$ and $b$, $a$ and $c$, $b$ and $c$) are incompatible. Output the lexicographically smallest such trio (the one with the smallest $a$; in case of a tie, the smallest $b$; and finally the smallest $c$).

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
