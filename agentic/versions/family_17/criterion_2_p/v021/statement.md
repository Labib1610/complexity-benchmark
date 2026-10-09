# Problem B — Layered Signal Routing

Time limit: 2 s   Memory limit: 256 MB

## Description
A high-frequency signal processor relies on a dual-layer routing architecture. There are $2q$ terminal nodes in total. Nodes $1$ through $q$ are transmitters located on the primary layer. Nodes $q+1$ through $2q$ are receivers located on the secondary layer.

To initialize the processor, you must establish exactly $q$ independent signal bridges. A signal bridge must link one transmitter to one receiver. 

The processor's physical layout only permits bridges to be formed along $t$ specific interference-free channels. Each channel links a specific primary-layer transmitter to a specific secondary-layer receiver. 

A successful initialization requires selecting a subset of these channels such that every terminal node (all transmitters and all receivers) is incorporated into exactly one signal bridge. A node cannot be left out, nor can it be linked to multiple bridges.

Evaluate the provided list of interference-free channels and determine if a complete initialization is possible. 

## Input
The first line provides two integers $q$ and $t$ (1 ≤ $q$ ≤ 100000, 0 ≤ $t$ ≤ 400000) — the number of nodes per layer and the number of interference-free channels.
The next $t$ lines each provide two integers $a$ and $b$ (1 ≤ $a$ ≤ $q$ < $b$ ≤ $2q$), representing an available channel between transmitter $a$ and receiver $b$.

## Output
If a complete initialization can be achieved, print `YES` on the first line, followed by $q$ lines detailing the chosen channels (each line containing the two node IDs of the bridge). If it is impossible to incorporate every node, print `NO`.

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
