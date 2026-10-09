# Orbital Telemetry Synchronization

Time limit: 2 s
Memory limit: 256 MB

## Description
A space agency manages a communication network consisting of orbital probes and terrestrial ground stations. During a given time window, a schedule of data transfers must be executed, where each transfer connects exactly one orbital probe to exactly one terrestrial ground station.

To execute these transfers without signal interference, every transfer must be assigned a specific frequency band. An orbital probe can participate in multiple transfers over the window, but to avoid transmitter overlap, all transfers involving the same probe must be assigned distinct frequency bands. Similarly, a terrestrial ground station can receive multiple transfers, but all transfers directed to the same ground station must use distinct frequency bands.

Let the peak congestion level, $K$, be the maximum number of transfers that involve any single orbital probe or any single terrestrial ground station. The system is equipped with exactly $K$ frequency bands, numbered 1 through $K$. The two-sided architecture of the network guarantees that a valid assignment using only these $K$ bands is always mathematically possible.

Your objective is to provide a valid band assignment for every scheduled transfer such that no frequency collisions occur at any probe or ground station.

## Input
The first line contains three integers $n_L$, $n_R$, and $m$ ($1 \le n_L, n_R \le 100000$, $0 \le m \le 400000$), representing the number of orbital probes, the number of terrestrial ground stations, and the total number of scheduled transfers, respectively.

The next $m$ lines each contain two integers $u$ and $v$ ($1 \le u \le n_L$, $1 \le v \le n_R$), indicating a scheduled transfer between orbital probe $u$ and terrestrial ground station $v$.

## Output
Print `YES` on the first line. On the second line, print $m$ integers from $1$ to $K$, representing the frequency band assigned to each transfer in the order they appeared in the input.

## Example

### Input
```text
3 3 5
1 1
1 2
2 2
2 3
3 3
```

### Output
```text
YES
1 2 1 2 1
```
