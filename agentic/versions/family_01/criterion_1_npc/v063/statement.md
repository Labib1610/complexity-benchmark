# Problem A — Phase Assignments

Time limit: 2 s   Memory limit: 256 MB

A tactical command center oversees a roster of active field agents. The facility's communication infrastructure requires a minimum of one active agent to remain operational, and its hardware can support a maximum capacity of 40 agents simultaneously.

To execute a complex operation, each agent must be assigned exactly one of three operational phases, designated by the codes 1, 2, and 3. However, certain pairs of agents have conflicting operational profiles. If two agents with conflicting profiles are assigned to the exact same operational phase, their operation will be compromised.

You will be provided with the roster size and the list of all conflicting agent pairs. The number of such conflicting pairs can range anywhere from none at all, up to the theoretical maximum where every single agent conflicts with every other agent. Determine if it is possible to assign every agent a phase code such that no two conflicting agents operate in the same phase. If it is possible, provide one such valid assignment.

## Input
The first line provides two integers, $n$ and $m$, representing the number of active agents and the total count of conflicting pairs, respectively. The constraints on these values are dictated by the facility's physical limits and the maximum possible number of pairs described above.
Each of the next $m$ lines contains two integers $u$ and $v$. These represent the ID numbers (from 1 to $n$) of two distinct agents whose profiles conflict. No pair of agents is listed more than once.

## Output
If there is no way to assign the phases safely, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $s_1, s_2, \dots, s_n$ separated by spaces. Each integer $s_i$ must be 1, 2, or 3, representing the operational phase assigned to agent $i$. Any valid assignment is accepted.

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
