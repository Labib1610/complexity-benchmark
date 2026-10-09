# Diagnostic Sequencing for Exchange Fabrics

Time limit: 2 s
Memory limit: 256 MB

## Description
The automated maintenance pipeline for a high-capacity exchange fabric operates by mapping and testing physical wires. The hardware incorporates two distinct groups of endpoints: transmitters and receivers. A low-level scanner compiles a manifest of wires, where each wire spans from a specific transmitter to a specific receiver.

Your module must schedule a diagnostic test for every wire in the manifest. During a test, a wire is temporarily taken offline and assigned a specific phase number. To prevent cascading isolation failures, the hardware controller enforces a strict operational rule: no endpoint (whether a transmitter or a receiver) may have more than one of its connected wires offline during the same phase. In other words, if two wires share a common endpoint, they must be assigned different phases.

To ensure the fabric returns to full capacity as quickly as possible, the total number of distinct diagnostic phases used must not exceed the absolute minimum required. The endpoint with the highest number of attached wires dictates this lower bound. If the busiest endpoint in the system has $D$ wires attached to it, the schedule must use exactly $D$ phases. 

Your task is to assign each wire a phase from $1$ to $D$. The architecture of the exchange fabric guarantees that such an assignment is always possible.

## Input
The first line contains three integers $N_{in}$, $N_{out}$, and $M$ ($1 \le N_{in}, N_{out} \le 100000$, $0 \le M \le 400000$).
The following $M$ lines each contain two integers $u$ and $v$ ($1 \le u \le N_{in}$, $1 \le v \le N_{out}$), representing a wire between transmitter $u$ and receiver $v$.

## Output
Print `YES` on the first line.
On the second line, print $M$ space-separated integers representing the phase assignments for each wire in the order they appeared in the input. Each integer must be between $1$ and $D$ inclusive, where $D$ is the maximum number of wires attached to any single endpoint (transmitter or receiver). If multiple valid assignments exist, you may output any of them.

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
