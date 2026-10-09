# Emergency Protocol: Kernel Isolation

Time limit: 2 s   Memory limit: 256 MB

## Description
A severe zero-day intrusion has been detected in a high-performance computing cluster. The cluster consists of multiple processing cores linked by bidirectional data buses.

The automated defense system has identified the exact core where the intrusion originated, as well as the core hosting the central kernel module. To prevent a complete system takeover, the kernel core must be absolutely isolated from the compromised core. This means no sequence of active data buses can exist that would allow malicious data to propagate from the origin to the kernel.

You have been granted emergency authorization to permanently disable a selection of data buses. However, disabling a bus requires sending a stream of hardware-level interference signals, which causes temporary cluster-wide lag. Each data bus has a specific interference duration required to permanently burn out its connection. The total lag caused by your selections is simply the sum of the interference durations of all the disabled buses.

The cluster's watchdog timer will trigger a hard reset if the total lag exceeds a strict threshold. You must select a set of data buses to disable such that the total interference duration does not exceed this threshold, and the kernel core is completely separated from the compromised core. Whether other cores remain connected to the compromised core or the kernel core does not matter, provided the malicious data cannot traverse from the origin to the kernel.

## Input
Line 1: five integers $n$ (the number of processing cores), $m$ (the number of data buses), $s$ and $t$ (the identifiers of the compromised core and the kernel core, respectively), and $B$ (the maximum permitted lag threshold).
The next $m$ lines each contain three integers $u$, $v$, and $w$, indicating a bidirectional data bus between core $u$ and core $v$ that requires $w$ units of lag to disable. 
Cores are numbered from $1$ to $n$. 

## Output
If a valid set of buses can be disabled without exceeding the lag threshold $B$, print `YES`. On the next line, print the number of buses to disable, $c$. Then, output $c$ lines, each containing two integers $u$ and $v$ representing a bus to be disabled. If there are multiple valid configurations within the threshold, any valid set of buses is acceptable.
If it is impossible to separate the kernel core from the compromised core without exceeding the threshold, print `NO`.

## Example
### Input
```text
4 5 1 4 10
1 2 4
1 3 5
2 3 2
2 4 4
3 4 5
```

### Output
```text
YES
2
1 2
1 3
```
