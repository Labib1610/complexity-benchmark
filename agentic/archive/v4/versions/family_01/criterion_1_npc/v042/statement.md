# Museum Vault Assignment

Time limit: 2 s   Memory limit: 256 MB

A museum curator is organizing an exhibit featuring $n$ delicate historical artifacts, numbered $1$ to $n$. The museum has three climate-controlled vaults available for storage, designated as Vault $1$, Vault $2$, and Vault $3$.

Due to chemical reactions and environmental sensitivities, certain pairs of artifacts are mutually incompatible and cannot be stored in the same vault. Every such incompatible pair must be placed in different vaults.

Assign every artifact to exactly one of the three vaults so that no incompatible pair shares a vault, or determine that no such assignment exists. If multiple valid vault assignments exist, select the one that yields the lexicographically smallest sequence of vault numbers $c_1, c_2, \dots, c_n$, where $c_i$ is the vault assigned to artifact $i$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$) — the number of artifacts and the number of incompatible pairs.
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of mutually incompatible artifacts.

## Output
If no valid vault assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $c_1, c_2, \dots, c_n$ (each in \{1, 2, 3\}), where $c_i$ is the vault number assigned to artifact $i$. Output the lexicographically smallest valid assignment (comparing $c_1$ first, then $c_2$, and so on).

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
