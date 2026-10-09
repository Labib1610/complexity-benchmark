# Diagnostic Scheduling on a Cross-Group Router

Time limit: 2 s   Memory limit: 256 MB

## Description
A signal routing system consists of a set of inbound interfaces and a set of outbound interfaces. Every routing link in the system connects one inbound interface to one outbound interface. Links never connect two inbound interfaces, nor do they connect two outbound interfaces.

Diagnostic testing is performed in sequential cycles numbered 1, 2, 3, …, and testing a link requires exactly one full cycle. The strict hardware limitation is that two links sharing any common interface (whether inbound or outbound) cannot be tested during the same cycle. An interface cannot process multiple concurrent link diagnostics.

The interface with the absolute highest number of connected links dictates the baseline for the testing schedule. Let this maximum link count be $D$. Because this heavily-loaded interface requires $D$ distinct cycles for its links, the entire system must use at least $D$ cycles. Your objective is to assign every link to exactly one cycle from $1$ to $D$, guaranteeing that no interface has multiple links assigned to the same cycle. (Because of the strictly cross-group topology, it is a guaranteed property of the system that a schedule using exactly $D$ cycles is always possible.)

Additionally, the system guarantees two operational constraints:
- The sum of the link counts across all interfaces (both inbound and outbound) exactly equals twice the total number of links.
- No single interface connects to more than $400,000$ links.

## Input
First line: three integers $N_{in}$, $N_{out}$, $M$ ($1 \le N_{in}, N_{out} \le 100,000$, $0 \le M \le 400,000$).
Next $M$ lines: two integers $u$ and $v$ ($1 \le u \le N_{in}$, $1 \le v \le N_{out}$), representing a link between inbound interface $u$ and outbound interface $v$.

## Output
Print `YES`, then a second line containing $M$ integers in the range $1 \dots D$, representing the assigned diagnostic cycle for each link in the exact order they were given in the input.

## Example

**Input**
```text
3 4 5
1 1
1 2
2 2
2 3
3 4
```

**Output**
```text
YES
1 2 1 2 1
```
