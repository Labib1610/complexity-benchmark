# Problem A — Component Commissioning

Time limit: 2 s   Memory limit: 256 MB

## Description

Engineers have compiled a set of $m$ acceptance criteria for a control system. Each criterion consists of exactly three conditions. A single condition specifies a target component and a required polarity for that component (either active or inactive). A criterion is satisfied provided that at least one of its three conditions is met. A criterion with none of its conditions met fails the acceptance check.

The control system itself consists of $n$ individual components. Prior to operation, every component must be locked into exactly one of two states: active (represented by 1) or inactive (represented by 0). A component cannot be left in a neutral state. Because the same component can appear across multiple criteria—sometimes required to be active by one condition and inactive by another—the criteria often overlap and restrict each other.

Given the $m$ acceptance criteria and the $n$ components, you must determine whether there exists a single, global configuration of all $n$ components that satisfies all $m$ criteria simultaneously. If such a configuration is possible, you must output one valid state for each component. If the criteria are over-constrained and no such configuration exists, you must report this.

## Input

The first line contains two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$).
Each of the next $m$ lines contains three non-zero signed integers $l_1, l_2, l_3$, with $|l_i| \le n$. 
The absolute value $|l_i|$ identifies the component. A positive value means the condition requires the component to be active. A negative value means the condition requires the component to be inactive.

## Output

If no valid configuration exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each in \{0, 1\}), where $s_i$ is the state of component $i$. Any valid configuration is accepted.

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

Each criterion has exactly three conditions. The same component index may appear more than once within a single criterion.
