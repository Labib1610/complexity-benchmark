# Problem A — Atmospheric Preservation

Time limit: 2 s   Memory limit: 256 MB

A collection of $n$ historical documents is being processed for long-term storage. Analysis has identified $m$ specific pairs of documents that possess incompatible material compositions; these pairs will degrade if kept in the same environment.

The facility is equipped with three distinct preservation vaults, which are identified by the codes 1, 2, and 3. The storage protocol mandates two rules:
- Any two documents identified as incompatible must be placed in different vaults.
- Every document must be assigned to exactly one of the three vaults.

Your task is to analyze the incompatibility data and decide whether it is possible to satisfy all storage protocols. If a valid arrangement exists, you must provide one.

## Input
The first line contains two integers $n$ and $m$ — the number of documents and the number of incompatible pairs ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of documents that are incompatible.

## Output
If no valid arrangement exists, print a single line NO.
Otherwise print YES on the first line. On the second line print $n$ integers $v_1 \ v_2 \dots v_n$ (each in $\{1, 2, 3\}$), where $v_i$ is the vault assigned to document $i$. Any valid arrangement is accepted.

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
