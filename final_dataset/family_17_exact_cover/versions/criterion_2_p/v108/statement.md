# Stage 2: Uplink Synchronization

Time limit: 2 s   Memory limit: 256 MB

## Description
The satellite network initialization sequence is underway. The telemetry system has just completed its preliminary sweep, producing a catalog of stable transmission corridors. Each corridor connects exactly one surface module (from a set indexed $1$ through $q$) to exactly one orbital module (from a set indexed $q+1$ through $2q$). 

For the network to reach its required operational capacity, you must select a subset of these stable corridors to lock in. The hardware constraints dictate that an operational state is only achieved when every single surface module and every single orbital module is actively utilizing exactly one selected corridor. A module cannot be left dormant, nor can it handle multiple corridors simultaneously.

Determine whether it is possible to select a set of corridors that satisfies these operational requirements. If such a state can be reached, output any valid set of selected corridors so they can be processed by the cryptographic key generator in the next stage. If no such state is possible, the initialization sequence must be aborted.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$). The integer $q$ represents the number of surface modules (and also the number of orbital modules). The integer $t$ represents the total number of stable corridors identified during the preliminary sweep. 

The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a stable corridor between surface module $a$ and orbital module $b$.

## Output
If the required operational state can be achieved, output `YES` on the first line. On the following $q$ lines, output the two module indices for each selected corridor. If the requirements cannot be met, output `NO`.

## Example

**Input:**
```
3 4
1 4
2 5
3 5
2 6
```

**Output:**
```
YES
1 4
3 5
2 6
```
