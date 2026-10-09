# Problem B — Paired Window Constraints

Time limit: 1 s
Memory limit: 256 MB

## Description
A facility's main control board consists of $n$ mechanical toggles, each of which must be locked into either position 1 or position 0 prior to operation. During the safety review, inspectors define $m$ operational requirements.

Every requirement specifies exactly two target conditions. A target condition is simply a toggle and its desired position (represented by a positive index if position 1 is desired, and a negative index if position 0 is desired). For a requirement to be satisfied, at least one of its two target conditions must be met by the board's configuration. This creates a chain of dependencies: if a configuration fails to meet one side of a requirement, the other side's condition becomes absolutely mandatory.

Your task is to evaluate whether a single, stable configuration of all $n$ toggles can simultaneously satisfy all $m$ requirements. If such a configuration exists, you must provide one. If the requirements inherently contradict each other, you must report this failure.

## Input
The first line contains two integers $n$ and $m$. The facility requires at least one toggle, but the board's physical chassis limits the maximum number of toggles to exactly one hundred thousand. The number of requirements $m$ can be as low as zero, and is permitted to grow up to exactly double the chassis's maximum toggle capacity.

Each of the following $m$ lines describes a requirement using two non-zero signed integers $l_1$ and $l_2$. The absolute value of any given $l_i$ identifies the toggle, and will never exceed the actual $n$ used for that test. A positive sign indicates the toggle must be in position 1, while a negative sign indicates position 0.

## Output
If it is impossible to satisfy all requirements, print a single line containing `NO`.
If a valid configuration exists, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{0, 1\}$) representing the position of each toggle from 1 to $n$.

## Example 1
Input:
```
2 2
1 2
-1 -2
```
Output:
```
YES
1 0
```

## Example 2
Input:
```
1 2
1 1
-1 -1
```
Output:
```
NO
```

## Note
Multiple valid configurations may exist; any one is accepted. The same toggle index may appear in multiple requirements.
