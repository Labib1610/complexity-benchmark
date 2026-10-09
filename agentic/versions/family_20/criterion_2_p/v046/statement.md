# Scheduled Offline Windows for Dual-Bank Switches

Time limit: 2 s   Memory limit: 256 MB

## Description
A data center switch consists of two distinct hardware banks: an ingress bank and an egress bank. Fiber optic links are installed such that every link connects an ingress port to an egress port. Due to the physical separation of the banks, no link ever joins two ingress ports or two egress ports.

During scheduled maintenance, individual links must be taken offline. The maintenance period is divided into discrete operational windows. Taking a link offline requires exactly one full window. To maintain partial connectivity, a port's hardware controller cannot handle the simultaneous disconnection of more than one of its installed links. Consequently, any two links that terminate at the same port must be assigned to different windows.

The duration of the maintenance period is dictated by the most heavily utilized port in the switch. If the port with the highest number of installed links has $\Delta$ links, the maintenance requires at least $\Delta$ windows. To minimize downtime, the operations team mandates that the schedule uses exactly $\Delta$ windows. You must assign each link to a window from $1$ to $\Delta$ ensuring no port has multiple links offline during the same window. The dual-bank architecture ensures this minimal schedule is always mathematically possible.

## Input
The first line contains three integers $n_{in}$, $n_{out}$, and $m$ ($1 \le n_{in}, n_{out} \le 100000$, $0 \le m \le 400000$), representing the number of ingress ports, egress ports, and installed links.
The next $m$ lines each contain two integers $u$ and $v$ ($1 \le u \le n_{in}$, $1 \le v \le n_{out}$), indicating a link connecting ingress port $u$ to egress port $v$.

## Output
Print `YES` on the first line. On the second line, print $m$ integers separated by spaces, where the $i$-th integer (from $1$ to $\Delta$) represents the maintenance window assigned to the $i$-th link in the input.

## Example

### Input
```text
2 2 3
1 1
1 2
2 1
```

### Output
```text
YES
1 2 2
```
