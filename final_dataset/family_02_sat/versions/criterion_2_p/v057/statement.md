# Problem B — Reactor Boot Sequence

Time limit: 1 s   Memory limit: 256 MB

## Description

The startup sequence for the newly constructed hyper-reactor consists of three distinct phases. You are responsible for programming the software module for Phase II.

**Phase I: Topological Profiling**
Before any reaction begins, diagnostic probes map the reactor's internal plumbing. They identify $n$ flow regulators, numbered 1 to $n$. Each regulator can be set to either an active mode (1) or a dormant mode (0). The probes also map $m$ pressure relief channels. Each channel is mechanically coupled to exactly two specific regulator conditions. A condition is encoded as a non-zero integer $X$:
- A positive $X$ means regulator $X$ is active.
- A negative $X$ means regulator $|X|$ is dormant.
The output of this phase is a complete list of all relief channels and the two conditions they depend on. 

**Phase II: Configuration Synthesis (Your Task)**
Your module receives the diagnostic profile from Phase I. To ensure structural integrity, every single relief channel must be operational. The mechanics of a channel dictate a strict dependency: because it is coupled to exactly two conditions, failing to satisfy the first condition physically forces the second to become mandatory, and vice versa. Consequently, a channel is operational if and only if at least one of its two coupled conditions is fulfilled by the overall regulator settings. Your software must process the profile and either output a static assignment of modes for all $n$ regulators that makes all $m$ channels operational, or detect that the mechanical dependencies are self-contradictory. 

**Phase III: Hardware Actuation**
If your module outputs a valid assignment, the central control system physically locks the regulators into those modes and ignites the reactor. If your module reports a contradiction, the central control system aborts the boot sequence and alerts the engineering team.

## Input
The first line provides the profile dimensions: two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the subsequent $m$ lines corresponds to a relief channel discovered during Phase I. It contains two non-zero integers $l_1$ and $l_2$, where $|l_i| \le n$. These represent the two regulator conditions coupled to that channel.

## Output
If Phase II determines that no valid assignment is possible, print a single line containing `NO`.
If a valid assignment exists, print `YES` on the first line. On the second line, print $n$ integers $s_1 \ s_2 \ \dots \ s_n$ separated by spaces, representing the modes of regulators 1 through $n$ respectively. Output $1$ for active and $0$ for dormant. 

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
If multiple valid configurations are possible, your module may output any of them. Multiple channels may depend on the same regulator condition.
