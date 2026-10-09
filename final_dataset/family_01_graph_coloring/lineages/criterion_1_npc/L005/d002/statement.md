# Problem A — Atmospheric Preservation

Time limit: 2 s   Memory limit: 256 MB

You are responsible for archiving $n$ historical artifacts in a secure facility. Through chemical analysis, you have identified $m$ pairs of artifacts that react poorly with each other; if placed in the same climate zone, they will degrade.

The facility has exactly three climate-controlled zones, designated as Zone 1, Zone 2, and Zone 3. To ensure complete preservation:
- Every artifact must be allocated to exactly one of these three zones.
- Artifacts that react poorly together must never share the same zone.

Please note that the test data deliberately includes adversarial reaction networks designed to trap simplistic trial-and-error allocation methods in an astronomical number of dead ends. You must determine if a safe allocation exists under these conditions. If it does, output a valid configuration.

## Input
The first line contains two integers $n$ and $m$ — the number of artifacts and the number of reactive pairs ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the subsequent $m$ lines contains two integers $u$ and $v$, identifying a pair of artifacts that cannot be stored together.

## Output
If no safe allocation is possible, output NO on a single line.
Otherwise, output YES on the first line. On the second line, output $n$ integers $c_1 \ c_2 \dots c_n$ (each being 1, 2, or 3), where $c_i$ is the zone allocated to artifact $i$. If multiple safe allocations exist, providing any one of them is acceptable.

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