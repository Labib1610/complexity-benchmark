# Problem B — Multiplexer Stage Execution

Time limit: 2 s   Memory limit: 256 MB

## Description
The operation of a high-throughput multiplexer requires completing three sequential stages: calibration, pairing, and routing.

During the initial calibration stage, diagnostic routines test the signal integrity between the device's $q$ input terminals (numbered $1$ to $q$) and $q$ output terminals (numbered $q+1$ to $2q$). This stage has already finished, identifying exactly $t$ viable pathways. Each pathway connects a specific input terminal to a specific output terminal without signal degradation.

Your program is strictly responsible for the second stage: pairing. You must select a subset of the viable pathways to activate. The strict requirement for this stage is that every single terminal—all input terminals and all output terminals—must be assigned to exactly one active pathway. No terminal may be left unassigned, and no terminal may be assigned to multiple activated pathways.

If your program successfully computes a valid configuration, the system automatically advances to the routing stage, relying on your selected pathways to transmit data. If the strict requirement cannot be met, the pairing stage fails and the multiplexer must reboot.

Evaluate the calibration data and execute the pairing stage.

## Input
The first line provides two integers $q$ and $t$ (1 ≤ $q$ ≤ 100000, 0 ≤ $t$ ≤ 400000) — the number of terminals of each type, and the number of viable pathways identified during calibration.
The next $t$ lines each provide two integers $a$ and $b$ (1 ≤ $a$ ≤ $q$ < $b$ ≤ $2q$), representing a viable pathway between input terminal $a$ and output terminal $b$.

## Output
If the pairing stage can be completed successfully, print `YES` on the first line. Then, print $q$ lines detailing the activated pathways (each line containing the two terminal IDs of the pathway). If it is impossible to assign every terminal, print `NO`.

## Example 1

### Input
```
3 4
1 4
2 5
3 5
3 6
```

### Output
```
YES
1 4
2 5
3 6
```

## Example 2

### Input
```
2 2
1 3
2 3
```

### Output
```
NO
```
