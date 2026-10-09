# Problem B — Diagnostic Sequencing for Exchange Fabrics

Time limit: 2 s   Memory limit: 256 MB

## Description
The automated maintenance pipeline for a high-capacity exchange fabric operates in three distinct stages:

**Stage 1: Topology Discovery.** A low-level scanner maps the physical connections within the fabric. The hardware consists of a bank of ingress terminals and a bank of egress terminals. Connections only ever link an ingress terminal to an egress terminal; terminals of the same type are never directly linked. The scanner compiles these connections into a manifest, which is provided to your module.

**Stage 2: Diagnostic Sequencing (Your Task).** You must schedule a diagnostic phase for each connection in the manifest. During a phase, a connection is temporarily taken offline. The hardware strictly requires that no terminal (whether ingress or egress) has more than one of its connections taken offline during the same phase, to prevent cascading isolation failures. 

To ensure the fabric returns to full capacity as quickly as possible, the total number of distinct diagnostic phases used must not exceed the absolute minimum required. The terminal with the highest number of attached connections dictates this lower bound—if a terminal has $D$ connections, at least $D$ phases are required. Because of the strictly cross-bank nature of the connections, it is a guaranteed property of the system that a valid schedule using exactly $D$ phases always exists. Your task is to assign each connection a phase from $1$ to $D$.

**Stage 3: Execution.** A downstream controller receives your schedule, sequentially executes the diagnostic phases, and generates the final compliance report. You do not need to handle this stage.

## Input
The first line contains three integers $N_{in}$, $N_{out}$, and $M$ ($1 \le N_{in}, N_{out} \le 100000$, $0 \le M \le 400000$).
The following $M$ lines each contain two integers $u$ and $v$ ($1 \le u \le N_{in}$, $1 \le v \le N_{out}$), representing a connection between ingress terminal $u$ and egress terminal $v$.

## Output
Print `YES` on the first line.
On the second line, print $M$ space-separated integers representing the phase assignments for each connection in the order they appeared in the input. Each integer must be between $1$ and $D$ inclusive, where $D$ is the maximum number of connections attached to any single terminal. If multiple valid assignments exist, you may output any of them.

## Example
### Input
```text
4 4 6
1 1
1 2
2 2
3 3
3 4
4 4
```
### Output
```text
YES
1 2 1 1 2 1
```
