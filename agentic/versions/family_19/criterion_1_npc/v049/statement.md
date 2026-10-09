# Harmonic Resonance Tuning

Time limit: 5 s
Memory limit: 256 MB

## Description
An ancient arcane apparatus is built from $n$ focal crystals (numbered $1$ to $n$), which are interconnected by $m$ one-way resonance beams. Each beam is directed from one specific crystal to another and is rated with a strict structural threshold.

When energetic pulses are routed through the apparatus, they must adhere to several physical laws:
- Pulses are indivisible; the number of pulses of any type assigned to any beam must be a non-negative integer.
- Pulses come in $k$ distinct harmonic signatures.
- All pulses share the resonance beams. The structural threshold of any single beam dictates the absolute maximum sum of all pulses, regardless of their signature, that can traverse it simultaneously.
- The crystals themselves are purely transit points; they cannot store, alter, or convert the harmonic signatures. For any given signature, at any crystal that is neither its designated origin nor its designated terminus, the total number of incoming pulses must exactly match the total number of outgoing pulses of that same signature.

The apparatus is currently subject to $k$ active transmission contracts. Each contract specifies a harmonic signature, its originating crystal, its terminating crystal, and the exact required volume of pulses. For each signature, at its originating crystal, the outgoing pulses must exceed the incoming pulses by exactly the required volume. Conversely, at its terminating crystal, the incoming pulses must exceed the outgoing pulses by exactly that same required volume.

Your task is to determine whether there is a valid routing configuration of pulses across the resonance beams that fulfills all $k$ transmission contracts without breaching the structural threshold of any beam. If such a configuration is possible, you must also provide the exact breakdown of pulses for each signature on every beam.

## Input
Line 1: Three integers $n$, $m$, and $k$ — the number of crystals, beams, and harmonic signatures.
Next $k$ lines: Three integers $s_i$, $t_i$, and $d_i$, specifying the originating crystal, terminating crystal, and required pulse volume for harmonic signature $i$.
Next $m$ lines: Three integers $u$, $v$, and $cap$, specifying a one-way resonance beam from crystal $u$ to crystal $v$ with a structural threshold of $cap$ total pulses.

## Output
If a valid configuration exists, print `YES` on the first line. Then print $k$ lines. The $i$-th line should contain $m$ integers, where the $j$-th integer is the number of pulses of harmonic signature $i$ assigned to the $j$-th resonance beam (in the order the beams are listed in the input).
If no such configuration is possible, print `NO`.

## Example

**Input**
```text
4 4 2
1 4 1
1 4 1
1 2 1
1 3 1
2 4 1
3 4 1
```

**Output**
```text
YES
1 0 1 0
0 1 0 1
```
