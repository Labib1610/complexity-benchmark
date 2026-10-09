# Problem B — Diagnostics on an Exchange Fabric

Time limit: 2 s   Memory limit: 256 MB

## Description
A datacenter routing system comprises two distinct sets of devices: transmitters and receivers. Every optical connection in the system joins one transmitter to one receiver. There are absolutely no connections between any two transmitters, nor between any two receivers.

Each connection must undergo a diagnostic protocol that occupies a single time window. To prevent hardware faults, any individual device—whether a transmitter or a receiver—can participate in at most one connection's diagnostic protocol during any given time window. 

We define $K$ as the maximum number of connections attached to any single device in the entire system. The diagnostics must be fully completed using exactly $K$ time windows. 

Your objective is to allocate a time window (labeled 1 to $K$) to each connection. The fact that connections only occur between a transmitter and a receiver guarantees that completing all diagnostics within $K$ windows is always possible.

## Input
The first line provides three integers $N_T$, $N_R$, and $M$ (1 ≤ $N_T$, $N_R$ ≤ 100000, 0 ≤ $M$ ≤ 400000), representing the number of transmitters, the number of receivers, and the total number of optical connections, respectively.
The following $M$ lines each contain two integers $u$ and $v$ (1 ≤ $u$ ≤ $N_T$, 1 ≤ $v$ ≤ $N_R$), indicating a connection joining transmitter $u$ to receiver $v$.

## Output
Print `YES` on the first line.
On the second line, print $M$ space-separated integers, each between 1 and $K$, indicating the time window allocated to each connection, corresponding to the sequence provided in the input.

## Example

### Input
```text
3 3 4
1 1
1 2
2 2
3 3
```

### Output
```text
YES
1 2 1 1
```
