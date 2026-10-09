# Genetic Resilience

Time limit: 2 s   Memory limit: 256 MB

## Description

You are engineering a synthetic organism containing **n** modified genes. Prior to deployment, each gene must be permanently set to either an expressed or suppressed state.

The organism will be exposed to **m** environmental stressors. Each stressor is neutralized if and only if the organism's configuration satisfies at least one of three specific gene requirements. A requirement dictates that a specific gene must be in a specific state. 

Your objective is to determine whether there exists a single configuration for all **n** genes that neutralizes every stressor simultaneously. If a valid configuration exists, you must provide it; otherwise, you must determine that no such configuration can exist.

## Input
The first line contains two integers **n** and **m** (1 ≤ n ≤ 90, 0 ≤ m ≤ 400).
Each of the following **m** lines describes the requirements to neutralize one stressor using three non-zero integers $l_1, l_2, l_3$ ($|l_i| \le n$).
A positive integer $x$ specifies a requirement that gene $x$ is expressed.
A negative integer $-x$ specifies a requirement that gene $x$ is suppressed.
The same gene may be referenced multiple times within the same stressor.

## Output
If no configuration can neutralize all stressors, print a single line containing `NO`.
If a valid configuration exists, print `YES` on the first line.
On the second line, print **n** integers $s_1, s_2, \dots, s_n$ separated by spaces, where $s_i \in \{0, 1\}$ represents the state of gene $i$ (1 for expressed, 0 for suppressed).
Any valid configuration will be accepted.

## Example 1
Input:
```
3 2
1 2 3
-1 2 -3
```
Output:
```
YES
0 0 1
```

## Example 2
Input:
```
1 2
1 1 1
-1 -1 -1
```
Output:
```
NO
```
