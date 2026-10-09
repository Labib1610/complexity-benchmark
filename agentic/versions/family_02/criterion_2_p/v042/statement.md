# Problem B — Gallery Lighting Constraints

Time limit: 1 s
Memory limit: 256 MB

## Description

You are designing the lighting for a new gallery featuring $n$ display cases. Each case must be equipped with exactly one lighting filter: either an amber filter (represented by state 1) or a blue filter (represented by state 0).

The exhibition curator has specified $m$ aesthetic guidelines to ensure the gallery's visual flow. Every guideline links exactly two preferred filter states. For instance, a guideline might link "case 3 is amber" with "case 5 is blue". To maintain proper contrast, the final lighting configuration must satisfy at least one of the two preferred states in every guideline. If a configuration fails to meet both states of any guideline, the design is rejected.

Since each guideline contains exactly two options, failing to fulfill one option immediately forces the other to be fulfilled. These forced choices chain together across the gallery's display cases, propagating mandatory filter selections. You must trace these dependencies to find a single global assignment of filters that satisfies all $m$ guidelines simultaneously, or determine if the guidelines inherently contradict each other.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of display cases and the number of aesthetic guidelines.

Each of the following $m$ lines contains two non-zero integers $c_1$ and $c_2$ ($|c_i| \le n$). These represent the two preferred states for a guideline. A positive integer $c_i$ means case $c_i$ is preferred to have an amber filter. A negative integer $c_i$ means case $|c_i|$ is preferred to have a blue filter. The final configuration must satisfy at least one of the two states on each line.

## Output
If no valid filter assignment can satisfy all guidelines, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ integers $f_1, f_2, \dots, f_n$ (where each $f_i \in \{0, 1\}$), representing the filter assigned to each case from 1 to $n$. Output 1 for an amber filter and 0 for a blue filter. If multiple valid configurations exist, you may output any of them.

## Example 1
**Input:**
```
2 2
1 2
-1 -2
```
**Output:**
```
YES
1 0
```

## Example 2
**Input:**
```
1 2
1 1
-1 -1
```
**Output:**
```
NO
```

## Note
The same display case may appear in multiple guidelines.
