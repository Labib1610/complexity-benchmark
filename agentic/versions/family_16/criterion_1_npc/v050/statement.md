# Problem A — Alchemical Concoctions

Time limit: 5 s   Memory limit: 256 MB

## Description

An alchemist is synthesizing $N$ distinct compounds using $K$ elemental crystals. Each compound requires a strict progression of stages. During each stage, the compound must be exposed to a specific crystal for a predetermined number of minutes. The physical laws of this process dictate:

- The stages for a given compound must be performed in the exact sequence specified. A stage can only begin after the prior stage for that same compound has fully concluded.
- A crystal can only be actively exposing one compound at any given moment.
- Once a crystal begins a stage, the exposure must continue uninterrupted until the required number of minutes has passed.

Coordinate the synthesis of all compounds such that the minute at which the final stage of the final compound concludes is as small as possible. Report this minimum completion time.

## Input

The first line contains two integers $N$ and $K$ ($1 \le N \le 10$, $1 \le K \le 10$).
Each of the next $N$ lines outlines the requirements for one compound: an integer $S$ (the number of stages) followed by $S$ pairs of integers `crystal duration` ($1 \le \text{crystal} \le K$, $1 \le \text{duration} \le 1000$), detailing the compound's stages in order.
The total number of stages across all compounds is at most 50.

## Output

Print a single integer: the earliest possible minute by which all compounds are completely synthesized.

## Examples

### Example 1

**Input**
```
2 3
3 1 2 2 2 3 2
3 1 2 2 2 3 2
```

**Output**
```
8
```

### Example 2

**Input**
```
1 3
3 1 5 2 3 3 2
```

**Output**
```
10
```

### Example 3

**Input**
```
2 3
1 1 4
1 2 3
```

**Output**
```
4
```

## Note

In Example 1, two identical compounds each require crystals 1, 2, and 3 in succession (2 minutes each); the second compound must wait for the first to finish with crystal 1, trailing it through the progression and finishing at 8 minutes. In Example 3, the two compounds use different crystals and can be exposed simultaneously, finishing at 4 minutes.
