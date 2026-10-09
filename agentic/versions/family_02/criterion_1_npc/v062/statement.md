# Problem A — Redundant Control Calibration

Time limit: 2 s   Memory limit: 256 MB

## Description

A control system is governed by **n** binary dials, each firmly set to either position 1 or position 0. The system's stability is verified through **m** redundancy audits. Each audit observes exactly three dial requirements (a requirement specifies a dial and its desired position, 1 or 0). 

Because the system is designed for high fault tolerance, an audit is considered successful if **at least one** of its three requirements is met. This means that out of the 8 possible local states for the three dials involved in an audit, 7 are perfectly valid. With 87.5% of local configurations passing any given check, the system exhibits massive local flexibility. 

Furthermore, whenever two requirements of an audit are known to be unmet, the third requirement becomes strictly forced. This often leads to rapid, deterministic cascading updates across the system. Given this high degree of redundancy and the potential for deterministic propagation, your task is to find a single, global configuration for all **n** dials that satisfies all **m** audits simultaneously, or report if the audits are mutually over-constrained.

## Input
The first line contains two integers **n** and **m** (1 ≤ **n** ≤ 90, 0 ≤ **m** ≤ 400).
Each of the next **m** lines contains three non-zero signed integers **l₁ l₂ l₃**, with |**lᵢ**| ≤ **n**. The absolute value of **lᵢ** identifies the dial (from 1 to **n**). A positive sign indicates the audit requires that dial to be in position 1; a negative sign indicates it requires position 0. An audit passes if at least one of its three requirements is satisfied.

## Output
If no valid configuration exists, print a single line `NO`.
Otherwise print `YES` on the first line. On the second line print **n** integers **s₁ s₂ … sₙ** (each in {0, 1}), where **sᵢ** is the state of dial **i**. Any valid configuration is accepted.

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
Each audit lists exactly three requirements. The same dial index may appear more than once in a single audit.
