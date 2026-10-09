# Problem A — Thermal Chamber Wiring

Time limit: 5 s
Memory limit: 256 MB

## Description
The laboratory inventory contains a maximum of $B$ meters of wire. You must determine if this is sufficient to fully wire $n$ prototype sensor modules inside a linear thermal chamber.

The thermal chamber contains $n$ test bays positioned one meter apart in a single row, indexed from $1$ to $n$. The testing protocol dictates that each of the $n$ modules is locked into a unique bay, leaving no bay empty.

Furthermore, the protocol specifies $m$ telemetry links that must operate concurrently. Each link requires a direct physical wire between a specific pair of modules. When two linked modules are locked into bay $i$ and bay $j$, the wire stretched between them spans exactly $|i - j|$ meters. The total length of all installed wires cannot exceed the $B$ meters available.

Find whether a valid placement of modules into bays exists, and if so, output the bay index assigned to each module.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the following $m$ lines contains two integers $x$ and $y$, indicating that module $x$ and module $y$ require a telemetry link. Modules are numbered from $1$ to $n$.

## Output
If the placement is possible, print `YES` on the first line. On the second line, print $n$ integers separated by spaces, where the $k$-th integer represents the bay index (from $1$ to $n$) assigned to module $k$.
If it is impossible, print `NO`.

## Example

### Input
```
4 3 4
1 2
1 3
1 4
```

### Output
```
YES
2 1 3 4
```
