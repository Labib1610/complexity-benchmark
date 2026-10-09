# Flow Regulator Configuration

Time limit: 2 s   Memory limit: 256 MB

## Description
A chemical plant features $n$ flow regulators. Each regulator must be locked into one of two modes: active (1) or standby (0). No intermediate states are possible.

During safety inspections, $m$ potential hazard scenarios were identified. A hazard scenario is defined by a combination of three specific regulator states. For example, a scenario's list might specify regulator 2 as active, regulator 5 as standby, and regulator 7 as active.

A hazard scenario materializes—triggering a plant shutdown—if and only if the plant's actual configuration does not match any of the three states listed for that scenario. As long as the plant's configuration matches at least one of the listed states, the scenario is safely averted.

Your task is to determine whether there is a global configuration for all $n$ regulators that averts every single hazard scenario simultaneously.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$).
Each of the next $m$ lines contains three non-zero signed integers $l_1, l_2, l_3$, with $|l_i| \le n$.
A positive integer $x$ indicates that the scenario lists regulator $x$ as active. A negative integer $x$ indicates that the scenario lists regulator $|x|$ as standby.

## Output
If no safe configuration exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line print $n$ integers $s_1, s_2, \dots, s_n$ (each in $\{0, 1\}$), where $s_i$ is the state of regulator $i$ (1 for active, 0 for standby). Any safe configuration is accepted.

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
Each hazard scenario lists exactly three states. The same regulator may be listed more than once in a single scenario.
