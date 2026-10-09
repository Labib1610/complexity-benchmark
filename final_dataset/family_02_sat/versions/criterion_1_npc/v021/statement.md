# Problem A — Master Key Design

Time limit: 2 s   Memory limit: 256 MB

## Description

A security company is designing a mechanical lock consisting of $n$ tumblers. To open the lock, a key must push each tumbler into one of two distinct positions: "high" (represented by 1) or "low" (represented by 0). There are no intermediate positions, and no tumbler can be left unconfigured.

The lock's internal mechanism contains $m$ locking pins. Each locking pin is held in place by three sensory prongs that detect the positions of three specific tumblers. A single prong's configuration is expressed as a non-zero integer $x$:
- If $x > 0$, the prong rests on the upper catch of tumbler $x$. This prong will release the pin if tumbler $x$ is pushed to the high position (1).
- If $x < 0$, the prong rests on the lower catch of tumbler $|x|$. This prong will release the pin if tumbler $|x|$ is pushed to the low position (0).

A locking pin will successfully disengage if **at least one** of its three sensory prongs is triggered to release it. If a pin has none of its three prongs triggered, it remains engaged and the lock will not open. The same tumbler may be monitored by many prongs across different pins, and the physical constraints often force a tumbler to be pushed high for one pin but low for another.

Your task is to determine whether there exists a single global key configuration of the $n$ tumblers that disengages all $m$ locking pins simultaneously.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$).
Each of the next $m$ lines contains three non-zero integers $l_1, l_2, l_3$, with $|l_i| \le n$. These represent the configurations of the three sensory prongs for a single locking pin. At least one of the three stated prongs must release the pin for the lock to open.

## Output
If no such tumbler configuration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each either 0 or 1), where $s_i$ is the required position of tumbler $i$. Any valid configuration is accepted.

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

## Note
Each locking pin always has exactly three sensory prongs. The same tumbler index may appear more than once within the prongs of a single pin.
