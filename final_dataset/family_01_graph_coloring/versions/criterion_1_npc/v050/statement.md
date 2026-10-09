# Problem A — Torsional Stress

Time limit: 2 s   Memory limit: 256 MB

You are designing a support framework consisting of $n$ structural modules. Each module must be aligned with exactly one of the three primary spatial axes (X, Y, or Z). For the control software, these axes are designated by the integer codes 1, 2, and 3, respectively. By definition, any two distinct axes from this set are perpendicular to each other, whereas an axis is parallel (not perpendicular) to itself.

The framework is reinforced by $m$ rigid struts, where each strut connects a specific pair of modules. To prevent torsional failure under load, the design mandates that any two modules joined by a strut must be aligned to perpendicular axes.

Determine a valid axis alignment for all $n$ modules that satisfies this structural requirement. If no such alignment is possible, you must report that it is impossible.

## Input
The first line provides two integers $n$ and $m$ — the total number of modules and the number of struts ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the subsequent $m$ lines contains two integers $u$ and $v$, indicating that a strut connects module $u$ and module $v$.

## Output
If there is no valid way to align all modules safely, print a single line containing the word NO.
If a valid configuration exists, print YES on the first line. On the second line, print $n$ integers $s_1, s_2, \ldots, s_n$ separated by spaces, where $s_i \in \{1, 2, 3\}$ is the axis code assigned to the $i$-th module. Any valid configuration is accepted.

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
