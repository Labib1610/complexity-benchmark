# Problem A — Grid Frequency Unification

Time limit: 5 s   Memory limit: 256 MB

## Description

A disaster recovery team manages a regional power grid consisting of $n$ substations. Certain pairs of substations can be linked by restoring a transmission line, which requires a specific number of labor hours.

Among the grid's facilities, $t$ substations serve critical hospitals. The recovery protocol dictates that all hospital substations must share a unified grid frequency. The mechanics of frequency sharing operate according to the following rules:
- Any two substations directly linked by a restored transmission line share the same frequency.
- Frequency sharing propagates transitively: if substation X shares a frequency with Y, and Y shares it with Z, then X and Z share the same frequency.
- Substations that do not serve hospitals are not required to share this frequency, but they can be used to propagate it if restoring lines to them reduces the overall effort.

You must select a set of transmission lines to restore. Your objective is to ensure that every critical substation shares the same frequency with every other critical substation, while minimizing the total labor hours (the sum of the labor hours of the restored lines).

## Input

The first line contains three integers $n$, $m$, and $t$ (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains $t$ distinct integers representing the identifiers of the critical substations.
Each of the following $m$ lines contains three integers $u$, $v$, and $w$ (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that a transmission line can be restored between substation $u$ and substation $v$ at the cost of $w$ labor hours.
The provided lines are always sufficient to successfully unify the frequency of all critical substations.

## Output

Print a single integer: the minimum total labor hours required to ensure all critical substations share the same frequency.

## Examples

### Example 1

**Input**
```
4 6 3
1 2 3
1 4 1
2 4 1
3 4 1
1 2 2
2 3 2
1 3 2
```

**Output**
```
3
```

### Example 2

**Input**
```
4 4 3
1 2 3
1 2 1
2 3 1
1 4 10
3 4 10
```

**Output**
```
2
```

### Example 3

**Input**
```
3 2 1
1
1 2 5
2 3 5
```

**Output**
```
0
```

## Note

In Example 1, propagating the frequency through the non-critical substation 4 requires restoring three lines (costs 1+1+1 = 3), which requires fewer labor hours than linking the three critical substations exclusively among themselves (which would cost 4). In Example 3, there is only one critical substation, so it trivially meets the requirement without restoring any lines.
