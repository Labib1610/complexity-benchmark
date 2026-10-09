# Problem A — Atmospheric Preservation

Time limit: 2 s   Memory limit: 256 MB

You are tasked with organizing $n$ historical documents for long-term storage. Extensive testing has uncovered $m$ pairs of documents with incompatible material compositions, meaning they will suffer degradation if stored in the same environment.

The storage facility provides three separate preservation vaults, labeled 1, 2, and 3. To prevent damage, the following protocols apply:
- Each document must be securely assigned to exactly one of the three vaults.
- No two documents that are incompatible can be assigned to the same vault.

Determine whether there is a storage assignment that strictly follows these protocols. If such an assignment is possible, provide one.

## Input
The first line contains two integers $n$ and $m$ — the number of documents and the number of incompatible pairs ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the following $m$ lines contains two integers $u$ and $v$, representing a pair of incompatible documents.

## Output
If no valid assignment exists, print a single line NO.
Otherwise, print YES on the first line. On the second line, print $n$ integers $c_1 \ c_2 \dots c_n$ (each in $\{1, 2, 3\}$), where $c_i$ is the vault assigned to document $i$. Providing one valid assignment is sufficient if several exist.

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