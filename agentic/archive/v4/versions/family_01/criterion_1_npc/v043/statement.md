# Facility Shift Allocation

**Time limit:** 2 s  
**Memory limit:** 256 MB

A research facility operates in three distinct operational shifts numbered 1, 2, and 3. There are $n$ members of personnel, identified by integers from 1 to $n$. Certain pairs of personnel are declared mutually exclusive, meaning they cannot be assigned to work in the same operational shift.

You must assign every individual to exactly one shift such that no mutually exclusive pair shares a shift. If multiple such valid allocations exist, you must select the one that yields the lexicographically smallest sequence of assigned shift numbers $(s_1, s_2, \dots, s_n)$. If no valid allocation exists at all, you must report this outcome.

## Input
The first line contains two space-separated integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$) — the total number of personnel and the number of mutually exclusive pairs, respectively.

Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that person $u$ and person $v$ cannot share a shift.

## Output
If it is impossible to satisfy all mutual exclusivity conditions, print a single line containing `NO`.

Otherwise, print two lines:
- The first line must contain `YES`.
- The second line must contain $n$ space-separated integers $s_1\ s_2\ \dots\ s_n$, where $s_i \in \{1, 2, 3\}$ is the shift assigned to person $i$. This sequence must be the lexicographically smallest among all valid shift allocations.

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
