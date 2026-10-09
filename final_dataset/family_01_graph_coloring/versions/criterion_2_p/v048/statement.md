# Problem B — Initialization Sequence: Phase Assignment

Time limit: 1 s   Memory limit: 256 MB

The automated diagnostic system of an orbital station runs a three-stage initialization sequence for its $n$ life-support modules.

**Stage 1: Topology Scan.** The system identifies $m$ mutual interference pairs among the modules. If two modules form an interference pair, they cannot operate on the same phase of the station's alternating current supply.

**Stage 2: Phase Separation Assignment.** The system must assign each module to exactly one of two available power phases, designated as phase 1 and phase 2. The assignment must ensure that no two modules in any interference pair share the same phase. To guarantee reproducible behavior for Stage 3, if multiple valid assignments exist, the system must generate the one that is lexicographically smallest when reading the phase assignments (1 or 2) of modules $1$ through $n$ in sequence.

**Stage 3: Hardware Initialization.** The system sends the phase configuration to the power distributor to physically switch the relays. If Stage 2 cannot find a valid assignment, Stage 3 is aborted and the system triggers a manual override.

Your task is to implement the Stage 2 software module.

## Input
The first line of the input contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$) — the number of modules and the number of interference pairs identified in Stage 1.
Each of the next $m$ lines contains two integers $u$ and $v$ — an interference pair between module $u$ and module $v$.

## Output
If Stage 2 cannot find a way to assign the phases without violating the separation rules, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers separated by spaces, where the $i$-th integer is the phase (1 or 2) assigned to the $i$-th module, representing the lexicographically smallest valid configuration.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
