# Problem B — Frequency Tuning on a Bridging Matrix

Time limit: 2 s
Memory limit: 256 MB

## Description
Data flows through a bridging matrix that isolates sources from destinations. The matrix consists of a set of input terminals and a set of output terminals. A circuit is formed by physically wiring one input terminal to one output terminal. Direct wiring between two input terminals or two output terminals is physically impossible due to connector shapes.

To prevent interference, each circuit must be tuned to a specific frequency channel, identified by an integer 1, 2, 3, and so on. A terminal lacks multiplexing capabilities, meaning if multiple circuits are wired to the same terminal—whether it is an input or an output—every one of those circuits must operate on a distinctly different frequency channel.

Let $D$ be the maximum number of circuits connected to any single terminal in the entire matrix. Clearly, at least $D$ distinct frequency channels are required just to handle that specific terminal. The engineering requirement is to configure the entire matrix using no more than those $D$ channels. You must assign a channel from the range 1 to $D$ to every circuit such that no terminal is forced to process two circuits on the same channel. (The strict connector shape rule ensures this compact $D$-channel configuration is always mathematically possible.)

## Input
The first line contains three integers $N_{in}$, $N_{out}$, and $M$ ($1 \le N_{in}, N_{out} \le 100000$, $0 \le M \le 400000$).
The following $M$ lines each contain two integers $u$ and $v$ ($1 \le u \le N_{in}$, $1 \le v \le N_{out}$), representing a circuit wired between input terminal $u$ and output terminal $v$.

## Output
Print `YES`, then a line containing $M$ integers in the range 1 to $D$ — the assigned frequency channel of circuit $i$ in input order. (Circuits sharing any terminal must have different channels). Here, $D$ is the number of circuits at the most heavily loaded terminal.

## Example

**Input:**
```
3 3 4
1 1
1 2
2 2
3 3
```

**Output:**
```
YES
1 2 1 1
```
