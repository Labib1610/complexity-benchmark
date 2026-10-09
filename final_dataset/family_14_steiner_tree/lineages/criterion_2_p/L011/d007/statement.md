# Problem B — Controlled Demolition of a Framework

Time limit: 2 s   Memory limit: 256 MB

## Description

You are tasked with the controlled demolition of a temporary framework. The framework consists of **n** joints, numbered 1 to **n**, and **m** load-bearing struts. Each strut connects two distinct joints and has a known structural mass.

The initial framework is fully *cohesive*. A set of joints is considered *cohesive* if it is impossible to partition it into two non-empty groups such that no strut connects a joint in the first group to a joint in the second group. (A set consisting of a single joint cannot be partitioned and is inherently cohesive).

You may perform a sequence of joint extractions to reduce the framework. In a single extraction step, you permanently remove exactly one joint, which safely destroys any struts attached to it. However, your extraction sequence must satisfy two strict safety regulations:
1. You may never extract any of the **t** *anchor joints*, as they are required for the final operation.
2. After every individual extraction step, the set of remaining joints must still be *cohesive*. If removing a joint would cause the remaining joints to lose cohesiveness (i.e., they could then be partitioned into two unlinked groups), that joint cannot be extracted at that time.

You can stop the extraction process at any point, including making no extractions at all. Your objective is to determine the minimum possible total structural mass of the struts that remain in the framework when you finish.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line provides **t** distinct integers representing the labels of the anchor joints.
Each of the subsequent **m** lines provides three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating a strut between joint **u** and joint **v** with a structural mass of **w**.

## Output

Output a single integer representing the minimum possible total structural mass of the remaining struts after a valid sequence of extractions.

## Examples

### Example 1

**Input**
```
4 3 2
1 4
1 2 5
2 3 1
3 4 2
```

**Output**
```
8
```

### Example 2

**Input**
```
5 4 1
3
1 2 4
2 3 6
3 4 2
4 5 9
```

**Output**
```
0
```

### Example 3

**Input**
```
3 2 3
1 2 3
1 2 4
2 3 5
```

**Output**
```
9
```